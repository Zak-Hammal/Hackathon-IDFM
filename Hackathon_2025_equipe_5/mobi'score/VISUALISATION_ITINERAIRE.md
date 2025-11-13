# 🗺️ Visualisation des itinéraires - Mobi'score

## 📍 Nouvelle fonctionnalité : Parcours détaillé

Chaque itinéraire affiche maintenant une **visualisation interactive** de tous les segments du trajet avec :
- Les modes de transport utilisés
- Les distances de chaque segment
- Les durées pour chaque mode
- Les points de départ et d'arrivée

## 🎨 Interface visuelle

### Composants

```
┌─────────────────────────────────────────────────────────────┐
│ 🗺️ Parcours détaillé                                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│ 📍 Départ : Gare du Nord, Paris                             │
│ 🎯 Arrivée : La Défense, Paris                              │
│                                                               │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌────────┐    →    ┌────────┐    →    ┌────────┐         │
│  │   🚶   │         │   🚇   │         │   🚶   │         │
│  │  walk  │         │  metro │         │  walk  │         │
│  │ 0.5 km │         │ 8.2 km │         │ 0.3 km │         │
│  │ 6 min  │         │ 15 min │         │ 4 min  │         │
│  └────────┘         └────────┘         └────────┘         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## 🚶🚴🚗 Modes de transport supportés

| Mode | Icône | Variations acceptées |
|------|-------|---------------------|
| **Marche** | 🚶 | walk |
| **Vélo** | 🚴 | velo, vélo, bike, bicycle |
| **Voiture** | 🚗 | voiture, car |
| **Covoiturage** | 🚗👥 | covoiturage, carpool, carpooling |
| **Métro** | 🚇 | metro, subway |
| **Train** | 🚂 | train |
| **Bus** | 🚌 | bus |
| **Tram** | 🚊 | tram, tramway |

## 📊 Exemples d'itinéraires

### Exemple 1 : Trajet écologique (métro)
**Fichier** : `exemple_itineraire.json`

```
📍 Gare du Nord, Paris → 🎯 La Défense, Paris

🚶 walk     →  🚇 metro    →  🚶 walk
0.5 km           8.2 km          0.3 km
6 min            15 min          4 min

Total : 9.0 km • 25 min • 0.3 kg CO2
Score : 140.5 pts ✅ Bon
```

### Exemple 2 : Trajet vélo
**Fichier** : `exemple_itineraire_velo.json`

```
📍 Bastille, Paris → 🎯 Bois de Vincennes

🚶 walk     →  🚴 velo     →  🚶 walk
0.3 km           5.2 km          0.2 km
4 min            18 min          3 min

Total : 5.7 km • 25 min • 0 kg CO2
Score : 253.0 pts 🌟 Excellent
```

### Exemple 3 : Trajet multimodal
**Fichier** : `exemple_itineraire_multimodal.json`

```
📍 Versailles → 🎯 Disneyland Paris

🚶 walk  →  🚗 voiture  →  🚂 train  →  🚌 bus  →  🚶 walk
0.4 km       5.0 km         35.0 km      3.0 km      0.6 km
5 min        10 min         40 min       8 min       7 min

Total : 44.0 km • 70 min • 1.9 kg CO2
Score : 60.8 pts ⚠️ Moyen
```

### Exemple 4 : Vélo + Train
**Fichier** : `exemple_itineraire_velo_train.json`

```
📍 Chatelet, Paris → 🎯 Fontainebleau

🚴 velo     →  🚂 train    →  🚴 velo
2.5 km           55.0 km         4.0 km
10 min           45 min          15 min

Total : 61.5 km • 70 min • 1.2 kg CO2
Score : 196.9 pts 🌟 Excellent
```

### Exemple 5 : Covoiturage
**Fichier** : `exemple_itineraire_covoiturage.json`

```
📍 Montparnasse, Paris → 🎯 Château de Versailles

🚶 walk     →  🚗👥 covoiturage  →  🚶 walk
0.4 km           15.8 km              0.3 km
5 min            35 min               4 min

Total : 16.5 km • 44 min • 0.7 kg CO2
Score : 138.7 pts ✅ Bon
```

### Exemple 6 : Voiture seule
**Fichier** : `exemple_itineraire_voiture.json`

```
📍 Neuilly-sur-Seine → 🎯 Aéroport CDG

🚶 walk     →  🚗 voiture  →  🚶 walk
0.2 km           18.5 km         0.1 km
3 min            25 min          2 min

Total : 18.8 km • 30 min • 3.2 kg CO2
Score : 16.5 pts ❌ Faible
```

## 🎯 Interactions utilisateur

### Hover sur un segment
- Le segment se soulève légèrement (animation)
- L'ombre s'intensifie
- Effet de feedback visuel

### Responsive
- **Desktop** : Segments alignés horizontalement avec flèches
- **Tablet** : Adaptation automatique, retour à la ligne si nécessaire
- **Mobile** : Segments empilés verticalement pour une meilleure lisibilité

## 📝 Format JSON des segments

Chaque segment d'itinéraire doit contenir :

```json
{
  "mode": "velo",                    // Type de transport
  "distance_km": 5.2,                // Distance en kilomètres
  "duree_minutes": 18,               // Durée en minutes
  "co2_kg": 0,                       // Émissions CO2 en kg
  "note": "Optionnel"                // Note descriptive (optionnel)
}
```

### Champs requis
- ✅ `mode` : string (nom du mode de transport)
- ✅ `distance_km` : number (distance en km)
- ✅ `duree_minutes` : number (durée en minutes)
- ✅ `co2_kg` : number (émissions en kg)

### Champs optionnels
- ⭕ `note` : string (information supplémentaire)

## 🎨 Styles et couleurs

### Segments
- **Fond** : Blanc (#ffffff)
- **Bordure** : Aucune
- **Ombre** : `0 2px 8px rgba(0,0,0,0.1)`
- **Hover** : `0 4px 12px rgba(0,0,0,0.15)`
- **Padding** : 10px 15px
- **Min-width** : 100px

### Flèches
- **Couleur** : Bleu IDFM (#4B91DA)
- **Taille** : 1.5em
- **Espacement** : 5px de chaque côté

### Icônes de modes
- **Taille** : 2em
- **Espacement** : 5px en dessous

### Lieu (départ/arrivée)
- **Fond** : Blanc (#ffffff)
- **Padding** : 8px 12px
- **Border-radius** : 6px

## 🔧 Configuration technique

### JavaScript
La fonction `afficherItineraireVisuel(fichier)` :
1. Charge le fichier JSON de l'itinéraire
2. Extrait les segments
3. Génère les éléments DOM pour chaque segment
4. Ajoute les flèches entre les segments
5. Affiche le parcours complet

### CSS
Classes principales :
- `.itineraire-visuel` : Container principal
- `.parcours-container` : Container flex des segments
- `.segment` : Carte individuelle d'un segment
- `.fleche-segment` : Flèche entre segments
- `.lieu` : Affichage départ/arrivée

## 📱 Accessibilité

### Éléments pris en compte
- ✅ Textes alternatifs via emojis + texte
- ✅ Contrastes WCAG AA respectés
- ✅ Taille de police lisible (min 0.75em)
- ✅ Zones cliquables suffisantes (hover)
- ✅ Structure sémantique HTML

## 🚀 Évolutions futures

### Court terme
1. Afficher le temps d'attente entre segments
2. Indiquer les correspondances
3. Ajouter des infos sur les lignes (numéro de bus, etc.)

### Moyen terme
1. Carte interactive avec tracé du parcours
2. Photos des stations/arrêts
3. Informations trafic en temps réel

### Long terme
1. Animation du trajet
2. Vue 3D du parcours
3. Réalité augmentée pour le guidage

## 💡 Bonnes pratiques

### Pour créer un itinéraire clair
1. **Décomposez** le trajet en segments logiques
2. **Utilisez** les noms standards des modes de transport
3. **Indiquez** précisément les distances et durées
4. **Calculez** le CO2 de manière réaliste

### Calcul du CO2
- Marche : 0 kg
- Vélo : 0 kg
- Métro : ~0.04 kg/km par personne
- Train : ~0.02 kg/km par personne
- Bus : ~0.07 kg/km par personne
- Voiture : ~0.17 kg/km
- Covoiturage : Voiture ÷ nombre de passagers

## 📚 Documentation associée

- `README.md` : Documentation principale
- `GUIDE_MOBISCORE.md` : Guide utilisateur
- `exemple_*.json` : Fichiers d'exemple

---

**Version** : 2.1  
**Date** : Novembre 2025  
**Fonctionnalité** : Visualisation d'itinéraire

