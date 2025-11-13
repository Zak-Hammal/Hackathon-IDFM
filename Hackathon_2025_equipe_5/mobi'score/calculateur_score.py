"""
Calculateur de score de mobilité
Ce module calcule un score de mobilité basé sur différents critères écologiques
"""

import json
from typing import Dict, List


def charger_itineraire(fichier_json: str) -> Dict:
    """
    Charge un fichier JSON d'itinéraire
    
    Args:
        fichier_json: Chemin vers le fichier JSON
        
    Returns:
        Dictionnaire contenant les données de l'itinéraire
    """
    with open(fichier_json, 'r', encoding='utf-8') as f:
        return json.load(f)


def a_voiture(itineraire: Dict) -> bool:
    """
    Vérifie si l'itinéraire contient un segment en voiture
    
    Args:
        itineraire: Dictionnaire de l'itinéraire
        
    Returns:
        True si l'itinéraire contient la voiture, False sinon
    """
    for segment in itineraire.get('segments', []):
        if segment.get('mode', '').lower() == 'voiture':
            return True
    return False


def calculer_distance_marche(itineraire: Dict) -> float:
    """
    Calcule la distance totale de marche en km
    
    Args:
        itineraire: Dictionnaire de l'itinéraire
        
    Returns:
        Distance totale de marche en km
    """
    distance = 0.0
    for segment in itineraire.get('segments', []):
        if segment.get('mode', '').lower() == 'walk':
            distance += segment.get('distance_km', 0.0)
    return distance


def calculer_distance_velo(itineraire: Dict) -> float:
    """
    Calcule la distance totale en vélo en km
    
    Args:
        itineraire: Dictionnaire de l'itinéraire
        
    Returns:
        Distance totale en vélo en km
    """
    distance = 0.0
    for segment in itineraire.get('segments', []):
        mode = segment.get('mode', '').lower()
        if mode in ['velo', 'vélo', 'bike', 'bicycle']:
            distance += segment.get('distance_km', 0.0)
    return distance


def a_covoiturage(itineraire: Dict) -> bool:
    """
    Vérifie si l'itinéraire contient un segment en covoiturage
    
    Args:
        itineraire: Dictionnaire de l'itinéraire
        
    Returns:
        True si l'itinéraire contient du covoiturage, False sinon
    """
    for segment in itineraire.get('segments', []):
        mode = segment.get('mode', '').lower()
        if mode in ['covoiturage', 'carpool', 'carpooling']:
            return True
    return False


def est_multimodal(itineraire: Dict) -> bool:
    """
    Vérifie si l'itinéraire est multimodal (voiture + autre mode non-marche)
    
    Args:
        itineraire: Dictionnaire de l'itinéraire
        
    Returns:
        True si multimodal avec voiture, False sinon
    """
    modes = set()
    for segment in itineraire.get('segments', []):
        mode = segment.get('mode', '').lower()
        if mode != 'walk':
            modes.add(mode)
    
    return 'voiture' in modes and len(modes) > 1


def a_tag_ecologique(itineraire: Dict) -> bool:
    """
    Vérifie si l'itinéraire a un tag écologique
    
    Args:
        itineraire: Dictionnaire de l'itinéraire
        
    Returns:
        True si tag "ecologic" ou "walk" présent, False sinon
    """
    tags = itineraire.get('tags', [])
    return 'ecologic' in tags or 'walk' in tags


def calculer_score_mobilite(
    itineraire: Dict,
    x_voiture: float = 50.0,
    x_marche: float = 10.0,
    x_report_modal: float = 30.0,
    x_co2: float = 100.0,
    x_penalite_co2: float = 2.0,
    x_tag: float = 20.0,
    x_velo: float = 15.0,
    x_covoiturage: float = 40.0
) -> Dict:
    """
    Calcule le score de mobilité d'un itinéraire
    
    Args:
        itineraire: Dictionnaire de l'itinéraire
        x_voiture: Points bonus si pas de voiture
        x_marche: Points par km de marche
        x_report_modal: Points bonus si multimodal avec voiture
        x_co2: Coefficient pour le calcul CO2
        x_penalite_co2: Pénalité CO2
        x_tag: Points bonus pour tag écologique
        x_velo: Points par km de vélo
        x_covoiturage: Points bonus si covoiturage
        
    Returns:
        Dictionnaire contenant le score et les détails
    """
    score = 0.0
    details = {}
    
    # Bonus pas de voiture
    pas_voiture = not a_voiture(itineraire)
    if pas_voiture:
        score += x_voiture
        details['bonus_pas_voiture'] = x_voiture
    else:
        details['bonus_pas_voiture'] = 0
    
    # Points pour la marche
    distance_marche = calculer_distance_marche(itineraire)
    points_marche = x_marche * distance_marche
    score += points_marche
    details['distance_marche_km'] = round(distance_marche, 2)
    details['points_marche'] = round(points_marche, 2)
    
    # Points pour le vélo
    distance_velo = calculer_distance_velo(itineraire)
    points_velo = x_velo * distance_velo
    score += points_velo
    details['distance_velo_km'] = round(distance_velo, 2)
    details['points_velo'] = round(points_velo, 2)
    
    # Bonus covoiturage
    covoiturage = a_covoiturage(itineraire)
    if covoiturage:
        score += x_covoiturage
        details['bonus_covoiturage'] = x_covoiturage
    else:
        details['bonus_covoiturage'] = 0
    
    # Bonus multimodal
    multimodal = est_multimodal(itineraire)
    if multimodal:
        score += x_report_modal
        details['bonus_multimodal'] = x_report_modal
    else:
        details['bonus_multimodal'] = 0
    
    # Calcul CO2
    co2_total = itineraire.get('co2_total_kg', 0.0)
    if co2_total > 0:
        points_co2 = x_co2 / (co2_total * x_penalite_co2 + 1)
    else:
        points_co2 = x_co2  # Bonus maximum si pas de CO2
    
    score += points_co2
    details['co2_total_kg'] = round(co2_total, 2)
    details['points_co2'] = round(points_co2, 2)
    
    # Bonus tag écologique
    tag_eco = a_tag_ecologique(itineraire)
    if tag_eco:
        score += x_tag
        details['bonus_tag_ecologique'] = x_tag
    else:
        details['bonus_tag_ecologique'] = 0
    
    return {
        'score_total': round(score, 2),
        'details': details,
        'itineraire_id': itineraire.get('itineraire_id', 'N/A'),
        'depart': itineraire.get('depart', 'N/A'),
        'arrivee': itineraire.get('arrivee', 'N/A')
    }


def afficher_score(resultat: Dict) -> None:
    """
    Affiche le score de manière formatée
    
    Args:
        resultat: Résultat du calcul de score
    """
    print(f"\n{'='*60}")
    print(f"SCORE DE MOBILITÉ - {resultat['itineraire_id']}")
    print(f"{'='*60}")
    print(f"De: {resultat['depart']}")
    print(f"À: {resultat['arrivee']}")
    print(f"\n{'-'*60}")
    print(f"SCORE TOTAL: {resultat['score_total']} points")
    print(f"{'-'*60}")
    
    details = resultat['details']
    print(f"\nDétails:")
    print(f"  • Bonus pas de voiture: {details['bonus_pas_voiture']} pts")
    print(f"  • Distance marche: {details['distance_marche_km']} km")
    print(f"  • Points marche: {details['points_marche']} pts")
    print(f"  • Distance vélo: {details['distance_velo_km']} km")
    print(f"  • Points vélo: {details['points_velo']} pts")
    print(f"  • Bonus covoiturage: {details['bonus_covoiturage']} pts")
    print(f"  • Bonus multimodal: {details['bonus_multimodal']} pts")
    print(f"  • CO2 total: {details['co2_total_kg']} kg")
    print(f"  • Points CO2: {details['points_co2']} pts")
    print(f"  • Bonus tag écologique: {details['bonus_tag_ecologique']} pts")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    # Test avec les exemples
    fichiers = [
        'exemple_itineraire.json',
        'exemple_itineraire_voiture.json',
        'exemple_itineraire_multimodal.json',
        'exemple_itineraire_velo.json',
        'exemple_itineraire_covoiturage.json',
        'exemple_itineraire_velo_train.json'
    ]
    
    for fichier in fichiers:
        try:
            itineraire = charger_itineraire(fichier)
            resultat = calculer_score_mobilite(itineraire)
            afficher_score(resultat)
        except FileNotFoundError:
            print(f"Fichier {fichier} non trouvé")

