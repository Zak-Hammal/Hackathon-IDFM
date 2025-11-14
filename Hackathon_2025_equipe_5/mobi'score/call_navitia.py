import requests

# ==========================
# CONFIG
# ==========================

NAVITIA_TOKEN = "TON_TOKEN_ICI"  # <-- remplace par ton token Navitia
BASE_URL = "https://api-cus.go.navitia.io/v1/coverage/fr-idf/journeys"

# Paramètres communs à tous les appels
COMMON_PARAMS = {
    "from": "admin:fr:78545",          # à adapter
    "to": "poi:osm:way:69221075",      # à adapter
    "datetime": "20251113T152155",
    "datetime_represents": "departure",
    "data_freshness": "realtime",
    "max_nb_journeys": 5,              # par défaut
}

# ==========================
# UTILITAIRES KPIs
# ==========================

def compute_car_cost(distance_m, cons_l_100=6.5, price_per_l=1.90):
    """
    Coût estimé du trajet voiture en euros à partir de la distance en mètres.
    cons_l_100 : L / 100km
    price_per_l : €/L
    """
    if not distance_m:
        return None
    km = distance_m / 1000.0
    litres = km * cons_l_100 / 100.0
    return round(litres * price_per_l, 2)


def compute_kcal(durations, walk_kcal_per_min=4.0, bike_kcal_per_min=8.0):
    """
    Estime les kcal dépensées sur le trajet à partir des durées
    de marche et de vélo (en secondes).

    On considère :
      - walking
      - bike
      - bss (vélo en libre-service) comme du vélo
    """
    walking_s = durations.get("walking", 0) or 0
    bike_s = (durations.get("bike", 0) or 0) + (durations.get("bss", 0) or 0)

    walking_min = walking_s / 60.0
    bike_min = bike_s / 60.0

    kcal = walking_min * walk_kcal_per_min + bike_min * bike_kcal_per_min
    return round(kcal, 1)


def extract_lines_used(journey):
    """
    Récupère la liste des lignes empruntées à partir des sections
    de type 'public_transport'.
    """
    lines = []
    for sec in journey.get("sections", []):
        if sec.get("type") != "public_transport":
            continue
        di = sec.get("display_informations", {}) or {}
        label = (
            di.get("label")
            or di.get("code")
            or di.get("headsign")
            or di.get("commercial_mode")
        )
        if label and label not in lines:
            lines.append(label)
    return lines


def extract_sections_detail(journey):
    """
    Retourne une liste structurée des sections de l'itinéraire :
    - mode : car, walking, bike, bss, public_transport, transfer, waiting, etc.
    - label : nom de la ligne (RER A, Métro 9...) ou le mode (car, walking)
    """
    sections_info = []

    for sec in journey.get("sections", []):
        sec_type = sec.get("type")

        # Cas 1 : Transport public
        if sec_type == "public_transport":
            di = sec.get("display_informations", {}) or {}
            label = (
                di.get("label")
                or di.get("code")
                or di.get("headsign")
                or di.get("commercial_mode")
            )
            if not label:
                label = "public_transport"
            sections_info.append({
                "mode": "public_transport",
                "label": label
            })

        # Cas 2 : Marche
        elif sec_type == "walking":
            sections_info.append({
                "mode": "walking",
                "label": "walking"
            })

        # Cas 3 : Voiture / vélo / bss → moteur street_network
        elif sec_type == "street_network":
            mode = sec.get("mode")  # car / bike / bss / walking...
            mode_label = mode or "street_network"
            sections_info.append({
                "mode": mode_label,
                "label": mode_label
            })

        # Cas 4 : Attente / transfert
        elif sec_type in ["transfer", "waiting"]:
            sections_info.append({
                "mode": sec_type,
                "label": sec_type
            })

        # Cas fallback
        else:
            sections_info.append({
                "mode": sec_type or "unknown",
                "label": sec_type or "unknown"
            })

    return sections_info

# ==========================
# STRATÉGIES DE SÉLECTION D'ITINÉRAIRE
# ==========================

def pick_first(journeys):
    """Prend simplement le premier itinéraire renvoyé."""
    return journeys[0] if journeys else None


def pick_min_transfers(journeys):
    """
    Choisit le trajet avec le moins de correspondances (nb_transfers).
    En cas d'égalité, on prend le plus court en durée totale.
    """
    if not journeys:
        return None
    best = min(
        journeys,
        key=lambda j: (j.get("nb_transfers", 0), j.get("duration", 10**9))
    )
    return best


def pick_max_walking(journeys):
    """
    Choisit le trajet où la marche est la plus longue.
    En cas d'égalité, on prend le plus court en durée totale.
    """
    if not journeys:
        return None

    def walking_key(j):
        durations = j.get("durations", {})
        walking = durations.get("walking", 0)
        # on trie par marche décroissante puis durée croissante
        return (-walking, j.get("duration", 10**9))

    best = sorted(journeys, key=walking_key)[0]
    return best

# ==========================
# EXTRACTION DES KPIs D'UN JOURNEY
# ==========================

def extract_kpis(persona_name, j):
    """Extrait les indicateurs clés d'un journey Navitia."""
    if not j:
        print(f"[{persona_name}] Aucun itinéraire sélectionné.")
        return None

    co2 = j.get("co2_emission", {}).get("value")          # gEC
    durations = j.get("durations", {})
    distances = j.get("distances", {})

    walking_time = durations.get("walking")               # secondes
    bike_time = (durations.get("bike", 0) or 0) + (durations.get("bss", 0) or 0)
    total_time = j.get("duration")                        # secondes
    car_distance = distances.get("car")                   # mètres

    car_cost = compute_car_cost(car_distance)
    kcal = compute_kcal(durations)
    lines_used = extract_lines_used(j)
    sections_detail = extract_sections_detail(j)

    return {
        "persona": persona_name,
        "co2_gEC": co2,
        "walking_time_s": walking_time,
        "bike_time_s": bike_time,
        "total_time_s": total_time,
        "car_distance_m": car_distance,
        "car_cost_eur": car_cost,
        "nb_transfers": j.get("nb_transfers"),
        "kcal": kcal,
        "lines_used": lines_used,
        "sections_detail": sections_detail,
        "tags": j.get("tags", []),
    }

# ==========================
# APPEL NAVITIA
# ==========================

def call_navitia(persona_name, extra_params, selector=pick_first):
    """
    Appelle Navitia pour un persona donné, applique un 'selector'
    pour choisir le bon journey, puis extrait les KPIs.
    """
    params = COMMON_PARAMS.copy()
    params.update(extra_params)

    response = requests.get(
        BASE_URL,
        params=params,
        auth=(NAVITIA_TOKEN, "")
    )
    response.raise_for_status()
    data = response.json()

    journeys = data.get("journeys", [])
    if not journeys:
        print(f"[{persona_name}] Aucun itinéraire renvoyé.")
        return None

    chosen = selector(journeys)
    return extract_kpis(persona_name, chosen)

# ==========================
# MAIN : DÉFINITION DES PERSONAS & RUN
# ==========================

def main():
    results = []

    # 1. Le plus rapide en TC (Navitia renvoie déjà le "best" en premier)
    results.append(call_navitia(
        "fastest_tc",
        {
            "direct_path": "none",
            "first_section_mode[]": "walking",
            "last_section_mode[]": "walking",
            "max_nb_journeys": 5,
        },
        selector=pick_first
    ))

    # 2. Que la voiture (trajet voiture uniquement)
    results.append(call_navitia(
        "car_only",
        {
            "direct_path": "only",
            "direct_path_mode[]": "car",
            "max_nb_journeys": 1,
        },
        selector=pick_first
    ))

    # 3. Voiture au début, marche à la fin
    results.append(call_navitia(
        "car_then_walk",
        {
            "direct_path": "indifferent",
            "first_section_mode[]": "car",
            "last_section_mode[]": "walking",
            "max_nb_journeys": 5,
        },
        selector=pick_first
    ))

    # 4. Bike au début, marche à la fin
    results.append(call_navitia(
        "bike_then_walk",
        {
            "direct_path": "indifferent",
            "first_section_mode[]": "bike",
            "last_section_mode[]": "walking",
            "max_nb_journeys": 5,
        },
        selector=pick_first
    ))

    # 5. Que bike (trajet 100% vélo)
    results.append(call_navitia(
        "bike_only",
        {
            "direct_path": "only",
            "direct_path_mode[]": "bike",
            "max_nb_journeys": 1,
        },
        selector=pick_first
    ))

    # 6. Celui avec le moins de changements (confort)
    results.append(call_navitia(
        "fewest_transfers",
        {
            "direct_path": "none",
            "first_section_mode[]": "walking",
            "last_section_mode[]": "walking",
            "max_nb_journeys": 10,
        },
        selector=pick_min_transfers
    ))

    # 7. Celui qui marche le plus (mode "sportif")
    results.append(call_navitia(
        "most_walking",
        {
            "direct_path": "none",
            "first_section_mode[]": "walking",
            "last_section_mode[]": "walking",
            "max_nb_journeys": 10,
        },
        selector=pick_max_walking
    ))

    # ===== Affichage console (pour debug / démo) =====
    print("\n=== Résumé KPIs ===")
    for r in results:
        if not r:
            continue
        print(
            f"\n[{r['persona']}]"
            f"\n  CO2 : {r['co2_gEC']} gEC"
            f"\n  Walking time : {r['walking_time_s']} s"
            f"\n  Bike time : {r['bike_time_s']} s"
            f"\n  Total time : {r['total_time_s']} s"
            f"\n  Distance voiture : {r['car_distance_m']} m"
            f"\n  Coût voiture estimé : {r['car_cost_eur']} €"
            f"\n  Nb changements : {r['nb_transfers']}"
            f"\n  Kcal estimées : {r['kcal']} kcal"
            f"\n  Lignes empruntées : {', '.join(r['lines_used']) if r['lines_used'] else 'Aucune'}"
            f"\n  Tags Navitia : {r['tags']}"
        )
        print("  Sections :")
        for idx, s in enumerate(r["sections_detail"], start=1):
            print(f"    {idx}. {s['mode']} → {s['label']}")


if __name__ == "__main__":
    main()
