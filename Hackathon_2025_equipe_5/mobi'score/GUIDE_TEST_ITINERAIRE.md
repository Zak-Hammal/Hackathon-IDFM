# 🧪 Guide de test - Visualisation d'itinéraire

## ✅ Checklist de test

### 1. Démarrage de l'application
```bash
python app.py
```
✅ L'application démarre sur http://localhost:5000

### 2. Affichage initial
- ✅ Le titre affiche "🚊 Mobi'score"
- ✅ Les couleurs sont bleu IDFM (fond bleu clair)
- ✅ Le menu déroulant contient 6 itinéraires

### 3. Sélection d'un itinéraire

#### Test 1 : Itinéraire métro (itin_001)
**Action** : Sélectionner "itin_001 - Gare du Nord, Paris → La Défense, Paris"

**Résultats attendus** :
- ✅ Section "🗺️ Parcours détaillé" apparaît
- ✅ Départ : "📍 Gare du Nord, Paris"
- ✅ Arrivée : "🎯 La Défense, Paris"
- ✅ 3 segments affichés :
  1. 🚶 walk • 0.5 km • 6 min
  2. → (flèche)
  3. 🚇 metro • 8.2 km • 15 min
  4. → (flèche)
  5. 🚶 walk • 0.3 km • 4 min
- ✅ Score : 140.5 pts avec badge "✅ Bon" (fond vert clair)

#### Test 2 : Itinéraire vélo (itin_004)
**Action** : Sélectionner "itin_004 - Bastille, Paris → Bois de Vincennes"

**Résultats attendus** :
- ✅ 3 segments affichés :
  1. 🚶 walk • 0.3 km • 4 min
  2. → (flèche)
  3. 🚴 velo • 5.2 km • 18 min
  4. → (flèche)
  5. 🚶 walk • 0.2 km • 3 min
- ✅ Score : 253.0 pts avec badge "🌟 Excellent" (fond vert foncé)

#### Test 3 : Itinéraire multimodal (itin_003)
**Action** : Sélectionner "itin_003 - Versailles → Disneyland Paris"

**Résultats attendus** :
- ✅ 5 segments affichés :
  1. 🚶 walk • 0.4 km • 5 min
  2. → 🚗 voiture • 5.0 km • 10 min
  3. → 🚂 train • 35.0 km • 40 min
  4. → 🚌 bus • 3.0 km • 8 min
  5. → 🚶 walk • 0.6 km • 7 min
- ✅ Score : 60.8 pts avec badge "⚠️ Moyen" (fond orange)

#### Test 4 : Itinéraire covoiturage (itin_005)
**Action** : Sélectionner "itin_005 - Montparnasse, Paris → Château de Versailles"

**Résultats attendus** :
- ✅ 3 segments affichés :
  1. 🚶 walk • 0.4 km • 5 min
  2. → 🚗👥 covoiturage • 15.8 km • 35 min
  3. → 🚶 walk • 0.3 km • 4 min
- ✅ Icône covoiturage : 🚗👥 (voiture + personnes)
- ✅ Score : 138.7 pts avec badge "✅ Bon"

#### Test 5 : Itinéraire vélo + train (itin_006)
**Action** : Sélectionner "itin_006 - Chatelet, Paris → Fontainebleau"

**Résultats attendus** :
- ✅ 3 segments affichés :
  1. 🚴 velo • 2.5 km • 10 min
  2. → 🚂 train • 55.0 km • 45 min
  3. → 🚴 velo • 4.0 km • 15 min
- ✅ Vélo au début et à la fin
- ✅ Score : 196.9 pts avec badge "🌟 Excellent"

#### Test 6 : Itinéraire voiture (itin_002)
**Action** : Sélectionner "itin_002 - Neuilly-sur-Seine → Aéroport CDG"

**Résultats attendus** :
- ✅ 3 segments affichés :
  1. 🚶 walk • 0.2 km • 3 min
  2. → 🚗 voiture • 18.5 km • 25 min
  3. → 🚶 walk • 0.1 km • 2 min
- ✅ Score : 16.5 pts avec badge "❌ Faible" (fond rouge)

### 4. Interactions

#### Test Hover sur segment
**Action** : Passer la souris sur un segment

**Résultats attendus** :
- ✅ Le segment se soulève légèrement
- ✅ L'ombre devient plus marquée
- ✅ Animation fluide (transition 0.2s)

#### Test Changement d'itinéraire
**Action** : Changer plusieurs fois d'itinéraire

**Résultats attendus** :
- ✅ Les segments se mettent à jour instantanément
- ✅ Le nombre de segments varie selon l'itinéraire
- ✅ Les flèches s'affichent correctement entre segments
- ✅ Pas de flèche après le dernier segment

### 5. Responsive

#### Test Desktop (> 968px)
**Action** : Fenêtre en plein écran

**Résultats attendus** :
- ✅ Segments alignés horizontalement
- ✅ Flèches horizontales entre segments
- ✅ Tout tient sur une ligne (ou deux si beaucoup de segments)

#### Test Tablet (~ 768px)
**Action** : Réduire la fenêtre à ~768px

**Résultats attendus** :
- ✅ Grille passe en 1 colonne
- ✅ Segments s'adaptent avec retour à la ligne
- ✅ Lisibilité préservée

#### Test Mobile (< 576px)
**Action** : Réduire la fenêtre à taille mobile

**Résultats attendus** :
- ✅ Segments passent en colonne si nécessaire
- ✅ Textes restent lisibles
- ✅ Zones tactiles suffisantes

### 6. Paramètres et calcul

#### Test Modification paramètres
**Action** : Modifier un curseur (ex: vélo de 15 à 25 pts/km)

**Résultats attendus** :
- ✅ Le score se recalcule automatiquement
- ✅ La couleur de la carte change si le seuil est franchi
- ✅ Le badge se met à jour
- ✅ Les segments restent affichés correctement

### 7. Tests de robustesse

#### Test itinéraire sans segments
**Action** : Créer un JSON sans champ "segments"

**Résultat attendu** :
- ✅ Aucune erreur JavaScript
- ✅ Message ou section vide
- ✅ Le reste de l'application fonctionne

#### Test mode inconnu
**Action** : Ajouter un segment avec mode "avion"

**Résultat attendu** :
- ✅ Icône par défaut affichée (🚶)
- ✅ Le nom "avion" s'affiche quand même
- ✅ Calcul du score fonctionne

### 8. Accessibilité

#### Test Contraste
**Action** : Vérifier les contrastes

**Résultats attendus** :
- ✅ Textes noirs sur fond blanc : contraste > 7:1
- ✅ Textes sur badges : contraste > 4.5:1
- ✅ Icônes + texte pour tous les modes (pas que icônes)

#### Test Navigation clavier
**Action** : Naviguer avec Tab

**Résultats attendus** :
- ✅ Menu déroulant accessible
- ✅ Boutons accessibles
- ✅ Curseurs accessibles
- ✅ Focus visible

### 9. Performance

#### Test Temps de chargement
**Action** : Chronométrer le chargement de la page

**Résultat attendu** :
- ✅ Page chargée en < 1 seconde (local)
- ✅ Itinéraires chargés en < 100ms
- ✅ Changement d'itinéraire instantané (< 50ms)

#### Test Changements rapides
**Action** : Changer rapidement d'itinéraire plusieurs fois

**Résultat attendu** :
- ✅ Aucun lag
- ✅ Aucune erreur console
- ✅ Affichage fluide

## 🐛 Bugs potentiels à surveiller

### Bug 1 : Flèche en trop
**Symptôme** : Flèche après le dernier segment  
**Cause** : Condition `index < length - 1` mal gérée  
**Fix** : Vérifier la condition dans la boucle

### Bug 2 : Segments qui débordent
**Symptôme** : Segments sortent du container sur mobile  
**Cause** : Flex-wrap non activé  
**Fix** : `flex-wrap: wrap` dans `.parcours-container`

### Bug 3 : Double chargement
**Symptôme** : Segments affichés deux fois  
**Cause** : Fonction appelée plusieurs fois  
**Fix** : Vérifier les event listeners

### Bug 4 : Icône manquante
**Symptôme** : Emoji non affiché  
**Cause** : Mode mal orthographié ou non reconnu  
**Fix** : Vérifier le mapping dans `getModeIcon()`

## ✅ Validation finale

Une fois tous les tests passés :

- [ ] Tous les itinéraires affichent correctement leurs segments
- [ ] Les icônes correspondent aux bons modes
- [ ] Les distances et durées sont affichées
- [ ] Les flèches sont bien placées
- [ ] Le hover fonctionne
- [ ] Le responsive est OK
- [ ] Pas d'erreur console
- [ ] Les couleurs sont IDFM
- [ ] L'accessibilité est respectée

## 📝 Rapport de test

### Template
```
Date : ____________
Testeur : ____________
Version : 2.1

Résultats :
- Tests fonctionnels : __ / 6 passés
- Tests interactions : __ / 2 passés
- Tests responsive : __ / 3 passés
- Tests robustesse : __ / 2 passés
- Tests accessibilité : __ / 2 passés
- Tests performance : __ / 2 passés

Total : __ / 17 tests passés

Bugs trouvés : ____________
Améliorations suggérées : ____________
```

---

**Happy Testing! 🎉**

