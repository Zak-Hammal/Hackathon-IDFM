# 🚊 Mobi'score - Guide d'utilisation

## 🎨 Interface Île-de-France Mobilités

L'interface a été redessinée aux couleurs d'**Île-de-France Mobilités** :
- **Bleu principal** : #4B91DA (bleu clair IDFM)
- **Bleu foncé** : #2A5E9D (pour les hover et accents)
- **Fond blanc** : Cartes et zones d'information
- **Dégradé** : Bleu clair vers bleu plus clair pour le fond

## 📊 Système de notation par catégories

Le Mobi'score évalue vos trajets selon **4 catégories** avec un code couleur intuitif :

### 🌟 Excellent (≥ 180 points)
- **Couleur** : Vert foncé
- **Profil** : Trajet très écologique
- **Exemples** :
  - Vélo seul (253 pts)
  - Vélo + train (196.9 pts)

**Caractéristiques** :
- Utilisation du vélo sur longue distance
- Aucune émission de CO2 ou très faibles
- Modes de transport actifs privilégiés

---

### ✅ Bon (120-179 points)
- **Couleur** : Vert clair
- **Profil** : Trajet écologique
- **Exemples** :
  - Transports en commun + marche (140.5 pts)
  - Covoiturage (138.7 pts)

**Caractéristiques** :
- Pas de voiture individuelle
- Transports en commun ou covoiturage
- Émissions de CO2 modérées

---

### ⚠️ Moyen (60-119 points)
- **Couleur** : Orange
- **Profil** : Trajet avec impact environnemental modéré
- **Exemples** :
  - Trajet multimodal avec voiture (60.8 pts)

**Caractéristiques** :
- Utilisation de la voiture combinée à d'autres modes
- Bonus multimodal actif
- Émissions de CO2 moyennes

---

### ❌ Faible (< 60 points)
- **Couleur** : Rouge
- **Profil** : Trajet peu écologique
- **Exemples** :
  - Voiture seule (16.5 pts)

**Caractéristiques** :
- Utilisation exclusive de la voiture
- Émissions de CO2 élevées
- Aucun mode de transport écologique

---

## 🎯 Comment améliorer son score ?

### Top 5 des actions les plus impactantes

1. **🚴 Utilisez le vélo** (+15 pts/km)
   - Le mode le plus valorisé
   - Zéro émission
   - Bonus santé !

2. **🚗👥 Privilégiez le covoiturage** (+40 pts)
   - Divise les émissions par le nombre de passagers
   - Bonus immédiat de 40 points
   - Convivialité en plus

3. **🚇 Évitez la voiture individuelle** (+50 pts)
   - Bonus majeur pour les trajets sans voiture
   - Préférez les transports en commun

4. **🚶 Marchez quand c'est possible** (+10 pts/km)
   - Bon pour la santé
   - Zéro émission
   - Chaque kilomètre compte

5. **🚌 Combinez plusieurs modes** (+30 pts)
   - Voiture + train/bus = bonus multimodal
   - Optimisez vos trajets

---

## 📈 Barème de notation

### Composition du score

```
Score total = 
  + Bonus pas de voiture (0-50 pts)
  + Points marche (10 pts/km)
  + Points vélo (15 pts/km)
  + Bonus covoiturage (0-40 pts)
  + Bonus multimodal (0-30 pts)
  + Points CO2 (variable selon émissions)
  + Bonus tag écologique (0-20 pts)
```

### Valeurs par défaut

| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| x_voiture | 50 pts | Bonus si pas de voiture |
| x_marche | 10 pts/km | Points par km à pied |
| x_velo | 15 pts/km | Points par km à vélo |
| x_covoiturage | 40 pts | Bonus covoiturage |
| x_report_modal | 30 pts | Bonus multimodal |
| x_co2 | 100 | Coefficient CO2 |
| x_penalite_co2 | 2.0 | Pénalité CO2 |
| x_tag | 20 pts | Bonus tag écologique |

---

## 🎨 Design responsive

L'interface s'adapte à tous les écrans :
- **Desktop** : 2 colonnes (paramètres + résultats)
- **Mobile** : 1 colonne empilée
- **Tablette** : Adaptation automatique

---

## 💡 Astuces

### Pour maximiser votre score :

1. **Planifiez vos trajets** avec plusieurs modes de transport
2. **Utilisez le vélo** pour les trajets < 10 km
3. **Covoiturez** pour les trajets longue distance en voiture
4. **Privilégiez les transports en commun** pour les trajets urbains
5. **Marchez** pour les courtes distances

### Exemples de scores réels :

| Trajet | Modes | Distance | Score | Catégorie |
|--------|-------|----------|-------|-----------|
| Paris intra-muros | Vélo | 5.7 km | **253** | 🌟 Excellent |
| Paris-Fontainebleau | Vélo+Train | 61.5 km | **197** | 🌟 Excellent |
| Paris Centre | Métro+Marche | 9.0 km | **141** | ✅ Bon |
| Paris-Versailles | Covoiturage | 16.5 km | **139** | ✅ Bon |
| Paris-Disneyland | Voiture+Train+Bus | 44.0 km | **61** | ⚠️ Moyen |
| Paris-CDG | Voiture seule | 18.8 km | **17** | ❌ Faible |

---

## 🔧 Personnalisation

Vous pouvez ajuster tous les paramètres en temps réel avec les curseurs :
- Les résultats se mettent à jour automatiquement
- Testez différentes configurations
- Trouvez l'équilibre parfait pour votre politique de mobilité

---

## 📱 Contact & Support

**Mobi'score** - Île-de-France Mobilités  
Hackathon IDFM 2025

Pour toute question ou suggestion, consultez le fichier README.md

