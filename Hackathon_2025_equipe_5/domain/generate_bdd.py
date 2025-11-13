import pandas as pd
import numpy as np
import uuid
import random
# === 1. Chargement du CSV des arrêts/lignes ===
df_arrets = pd.read_csv("./data/arrets-lignes.csv", sep=";")
# Vérification minimale
cols = {"id", "route_long_name", "stop_name"}
if not cols.issubset(df_arrets.columns):
    raise ValueError(f"Le fichier CSV doit contenir les colonnes : {cols}")
# Dictionnaire : {id_ligne -> {nom_ligne, arrêts associés}}
lines_dict = (
    df_arrets.groupby("id")
    .apply(lambda x: {
        "nom_ligne": x["route_long_name"].iloc[0],
        "arrets": list(set(x["stop_name"]))
    })
    .to_dict()
)
# Liste des IDs de ligne disponibles
line_ids = list(lines_dict.keys())
# === 2. Fonctions de génération ===
def generate_id():
    return str(uuid.uuid4())
def generate_favoris():
    """Favoris = quelques lignes (par ID) issues du CSV"""
    return random.sample(line_ids, k=random.randint(2, 4))
def generate_voiture():
    return np.random.choice([True, False], p=[0.4, 0.6])
def generate_pmr():
    return np.random.choice([True, False], p=[0.05, 0.95])
def generate_home_location():
    """Coordonnées simulées en Île-de-France"""
    lat = np.random.uniform(48.70, 49.05)
    lon = np.random.uniform(2.10, 2.55)
    return lat, lon
def generate_entreprise_siret():
    return "".join(str(random.randint(0, 9)) for _ in range(14))
# === 3. Génération des utilisateurs ===
n_users = 1000
data = {
    "id_unique": [generate_id() for _ in range(n_users)],
    "Favoris": [generate_favoris() for _ in range(n_users)],
    "Voiture": [generate_voiture() for _ in range(n_users)],
    "PMR": [generate_pmr() for _ in range(n_users)],
    "Entreprise_SIRET": [generate_entreprise_siret() for _ in range(n_users)],
    "home_lat": [],
    "home_lon": [],
}
for _ in range(n_users):
    lat, lon = generate_home_location()
    data["home_lat"].append(lat)
    data["home_lon"].append(lon)
df_users = pd.DataFrame(data)
# === 4. Création de groupes d’amis symétriques ===
def generate_friendships(user_ids, avg_friends=3):
    friends_map = {uid: set() for uid in user_ids}
    all_ids = user_ids.copy()
    for uid in user_ids:
        n_friends = np.random.randint(1, avg_friends + 2)
        potential_friends = [u for u in all_ids if u != uid]
        chosen = random.sample(potential_friends, k=min(n_friends, len(potential_friends)))
        for friend in chosen:
            friends_map[uid].add(friend)
            friends_map[friend].add(uid)  # symétrie
    return {uid: list(fset) for uid, fset in friends_map.items()}
friend_dict = generate_friendships(df_users["id_unique"].tolist())
df_users["Groupe_amis"] = df_users["id_unique"].map(friend_dict)
print(df_users.head())
print(f"\n:coche_blanche: {len(df_users)} utilisateurs générés avec favoris basés sur les ID de lignes du CSV.")
# Optionnel : sauvegarde
# df_users.to_csv("bdd_users.csv", index=False, encoding="utf-8")