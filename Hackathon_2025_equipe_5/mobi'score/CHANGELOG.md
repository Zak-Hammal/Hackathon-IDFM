# Historique des modifications

## Version 2.0 - Ajout des critères vélo et covoiturage

### ✨ Nouvelles fonctionnalités

#### 1. **Critère Vélo** 🚴
- Ajout du calcul de points basé sur la distance parcourue à vélo
- Formule : `x_velo × distance_velo`
- Valeur par défaut : **15 points/km**
- Modes reconnus : `velo`, `vélo`, `bike`, `bicycle`

#### 2. **Critère Covoiturage** 🚗👥
- Ajout d'un bonus si l'itinéraire utilise le covoiturage
- Valeur par défaut : **40 points**
- Modes reconnus : `covoiturage`, `carpool`, `carpooling`

### 📝 Modifications

#### Backend (`calculateur_score.py`)
- Ajout de la fonction `calculer_distance_velo()` : calcule la distance totale en vélo
- Ajout de la fonction `a_covoiturage()` : détecte la présence de covoiturage
- Mise à jour de `calculer_score_mobilite()` : intégration des deux nouveaux paramètres
- Mise à jour de `afficher_score()` : affichage des nouvelles métriques

#### API (`app.py`)
- Ajout des paramètres `x_velo` et `x_covoiturage` dans l'endpoint `/api/calculer`
- Mise à jour de la liste des fichiers d'exemples

#### Interface Web (`templates/index.html`)
- Ajout de 2 nouveaux curseurs interactifs :
  - **Points par km de vélo** (0-50 pts/km, défaut: 15)
  - **Bonus covoiturage** (0-100 pts, défaut: 40)
- Mise à jour de l'affichage des résultats avec les nouvelles cartes vélo et covoiturage
- Ajout des event listeners pour les nouveaux curseurs
- Grille de résultats étendue à 7 éléments

### 📦 Nouveaux exemples

#### `exemple_itineraire_velo.json`
- Trajet : Bastille → Bois de Vincennes
- Mode principal : Vélo (5.2 km)
- Score : **253 points** 🏆
- Tags : ecologic, velo, sport

#### `exemple_itineraire_covoiturage.json`
- Trajet : Montparnasse → Château de Versailles
- Mode principal : Covoiturage (15.8 km)
- Score : **138.67 points**
- Émissions CO2 réduites par le partage

#### `exemple_itineraire_velo_train.json`
- Trajet : Chatelet → Fontainebleau
- Modes : Vélo + Train + Vélo
- Distance vélo : 6.5 km
- Score : **196.91 points**
- Tags : ecologic, velo, multimodal

### 🧮 Formule de calcul mise à jour

```
Score = Bonus_pas_voiture 
      + (x_marche × distance_marche)
      + (x_velo × distance_velo)              [NOUVEAU]
      + Bonus_covoiturage                      [NOUVEAU]
      + Bonus_multimodal 
      + (x_co2 / (co2_total × x_penalite_co2 + 1)) 
      + Bonus_tag_écologique
```

### 📊 Comparaison des scores

| Itinéraire | Score | Points forts |
|------------|-------|--------------|
| Vélo seul (itin_004) | 253.0 | 🥇 Meilleur score ! Zéro émission |
| Vélo + Train (itin_006) | 196.91 | 🥈 Excellent multimodal écologique |
| Écologique métro (itin_001) | 140.5 | 🥉 Bon score transport en commun |
| Covoiturage (itin_005) | 138.67 | 👥 Partage = moins d'émissions |
| Multimodal (itin_003) | 60.83 | 🚌 Bonus multimodal actif |
| Voiture seule (itin_002) | 16.51 | ⚠️ Score le plus faible |

### 🎯 Impact

Les nouveaux critères encouragent fortement :
- **Le vélo** : 15 pts/km (vs 10 pts/km pour la marche)
- **Le covoiturage** : 40 pts de bonus (vs 50 pts pour éviter totalement la voiture)

Le vélo devient le mode de transport le plus valorisé, suivi du covoiturage comme alternative écologique à la voiture individuelle.

---

## Version 1.0 - Version initiale

### Fonctionnalités de base
- Calcul du score de mobilité
- 5 critères : pas de voiture, marche, multimodal, CO2, tags écologiques
- Interface web interactive
- 3 exemples d'itinéraires

