# 🚊 Mobi'score - Île-de-France Mobilités

Un démonstrateur web interactif pour calculer un score de mobilité basé sur différents critères écologiques d'un itinéraire.

**Design** : Interface aux couleurs d'Île-de-France Mobilités (bleu clair et blanc)  
**Code couleur** : Vert (excellent), Orange (moyen), Rouge (faible)

## 📋 Description

Ce projet permet d'évaluer l'impact écologique d'un trajet en fonction de plusieurs paramètres :

- **Bonus pas de voiture** : Points accordés si l'itinéraire n'utilise pas la voiture
- **Points marche** : Points par kilomètre parcouru à pied
- **Points vélo** : Points par kilomètre parcouru à vélo
- **Bonus covoiturage** : Points accordés si l'itinéraire utilise le covoiturage
- **Bonus multimodal** : Points si l'utilisateur combine la voiture avec un autre mode de transport
- **Score CO2** : Calcul basé sur les émissions de CO2 du trajet
- **Bonus tag écologique** : Points supplémentaires pour les itinéraires marqués comme "ecologic" ou "walk"

## 🎨 Fonctionnalités

- ✅ Sélection d'itinéraires prédéfinis
- ✅ Upload de fichiers JSON d'itinéraires personnalisés
- ✅ **Visualisation du parcours détaillé** : Voir tous les segments de l'itinéraire avec les modes de transport
  - Exemple : 🚶 Marche → 🚇 Métro → 🚶 Marche
  - Distance et durée pour chaque segment
  - Icônes visuelles pour chaque mode
- ✅ Curseurs interactifs pour ajuster les paramètres de calcul en temps réel
- ✅ Calcul automatique du score à chaque modification
- ✅ Interface moderne et responsive aux couleurs IDFM
- ✅ Visualisation détaillée des composantes du score
- ✅ **Code couleur automatique** selon la performance du trajet :
  - 🌟 **Vert** (≥180 pts) : Excellent
  - ✅ **Vert clair** (120-179 pts) : Bon
  - ⚠️ **Orange** (60-119 pts) : Moyen
  - ❌ **Rouge** (<60 pts) : Faible

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur

### Étapes

1. **Cloner le projet** (ou se placer dans le répertoire)

```bash
cd Hackathon_idfm_2025
```

2. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

## 📦 Structure du projet

```
Hackathon_idfm_2025/
├── app.py                              # Application Flask (backend)
├── calculateur_score.py                # Fonctions de calcul du score
├── requirements.txt                    # Dépendances Python
├── README.md                          # Documentation
├── templates/
│   └── index.html                     # Interface web
├── exemple_itineraire.json            # Exemple d'itinéraire écologique (métro)
├── exemple_itineraire_voiture.json    # Exemple avec voiture seule
├── exemple_itineraire_multimodal.json # Exemple multimodal (voiture+train+bus)
├── exemple_itineraire_velo.json       # Exemple avec vélo
├── exemple_itineraire_covoiturage.json # Exemple avec covoiturage
└── exemple_itineraire_velo_train.json # Exemple vélo + train
```

## 🎯 Utilisation

### Démarrer l'application

```bash
python app.py
```

L'application sera accessible à l'adresse : **http://localhost:5000**

### Utiliser l'interface web

1. **Sélectionner un itinéraire** dans le menu déroulant
2. **Ajuster les paramètres** avec les curseurs
3. Le score se calcule **automatiquement** à chaque modification
4. **Uploader un nouveau fichier** JSON si besoin

### Format du fichier JSON d'itinéraire

```json
{
  "itineraire_id": "itin_001",
  "depart": "Point A",
  "arrivee": "Point B",
  "date": "2025-11-13",
  "segments": [
    {
      "mode": "walk",
      "distance_km": 0.5,
      "duree_minutes": 6,
      "co2_kg": 0
    },
    {
      "mode": "metro",
      "distance_km": 8.2,
      "duree_minutes": 15,
      "co2_kg": 0.3
    }
  ],
  "tags": ["ecologic", "rapide"],
  "co2_total_kg": 0.3,
  "distance_totale_km": 9.0,
  "duree_totale_minutes": 25
}
```

**Modes de transport supportés** : `walk`, `voiture`, `velo` (ou `vélo`, `bike`, `bicycle`), `covoiturage` (ou `carpool`, `carpooling`), `metro`, `train`, `bus`, etc.

**Tags supportés** : `ecologic`, `walk`, `velo`, `multimodal`, `rapide`, etc.

## 🧮 Formule de calcul

Le score total est calculé selon la formule suivante :

```
Score = Bonus_pas_voiture 
      + (x_marche × distance_marche)
      + (x_velo × distance_velo)
      + Bonus_covoiturage
      + Bonus_multimodal 
      + (x_co2 / (co2_total × x_penalite_co2 + 1)) 
      + Bonus_tag_écologique
```

### Paramètres par défaut

- `x_voiture` = 50 points
- `x_marche` = 10 points/km
- `x_velo` = 15 points/km
- `x_covoiturage` = 40 points
- `x_report_modal` = 30 points
- `x_co2` = 100
- `x_penalite_co2` = 2.0
- `x_tag` = 20 points

## 🔧 API Endpoints

### `GET /api/itineraires`
Retourne la liste des itinéraires disponibles

### `POST /api/calculer`
Calcule le score d'un itinéraire
```json
{
  "fichier": "exemple_itineraire.json",
  "parametres": {
    "x_voiture": 50,
    "x_marche": 10,
    "x_velo": 15,
    "x_covoiturage": 40,
    "x_report_modal": 30,
    "x_co2": 100,
    "x_penalite_co2": 2.0,
    "x_tag": 20
  }
}
```

### `POST /api/upload`
Upload d'un nouveau fichier d'itinéraire

## 🧪 Test en ligne de commande

Vous pouvez aussi tester les fonctions directement :

```bash
python calculateur_score.py
```

Cela affichera les scores pour tous les exemples d'itinéraires.

## 📊 Système de notation

### Catégories de score

Le Mobi'score classe automatiquement les trajets en 4 catégories :

| Catégorie | Score | Couleur | Emoji | Description |
|-----------|-------|---------|-------|-------------|
| **Excellent** | ≥ 180 | 🟢 Vert foncé | 🌟 | Trajet très écologique (vélo, zéro émission) |
| **Bon** | 120-179 | 🟢 Vert clair | ✅ | Trajet écologique (transports en commun, covoiturage) |
| **Moyen** | 60-119 | 🟠 Orange | ⚠️ | Impact modéré (voiture + autre mode) |
| **Faible** | < 60 | 🔴 Rouge | ❌ | Peu écologique (voiture seule) |

### Exemples de scores réels

| Itinéraire | Score | Catégorie | Modes principaux |
|------------|-------|-----------|------------------|
| 🥇 Vélo urbain (itin_004) | **253.0** | 🌟 Excellent | Vélo |
| 🥈 Vélo + Train (itin_006) | **196.9** | 🌟 Excellent | Vélo + Train |
| 🥉 Métro (itin_001) | **140.5** | ✅ Bon | Métro + Marche |
| Covoiturage (itin_005) | **138.7** | ✅ Bon | Covoiturage |
| Multimodal (itin_003) | **60.8** | ⚠️ Moyen | Voiture + Train + Bus |
| Voiture (itin_002) | **16.5** | ❌ Faible | Voiture seule |

## 🎨 Personnalisation

### Modifier les paramètres par défaut

Éditez le fichier `calculateur_score.py` et modifiez les valeurs dans la fonction `calculer_score_mobilite()`.

### Ajouter de nouveaux itinéraires

Créez un fichier JSON suivant le format décrit ci-dessus et placez-le dans le répertoire racine, ou utilisez la fonction d'upload dans l'interface web.

## 📝 Licence

Projet libre pour le Hackathon IDFM 2025

## 👥 Auteur

Créé pour le Hackathon IDFM 2025

