# 🎨 Charte graphique Mobi'score - Île-de-France Mobilités

## Palette de couleurs principales

### Couleurs IDFM
| Nom | Hex | RGB | Usage |
|-----|-----|-----|-------|
| **Bleu principal** | `#4B91DA` | rgb(75, 145, 218) | Boutons, titres, curseurs |
| **Bleu foncé** | `#2A5E9D` | rgb(42, 94, 157) | Hover, accents |
| **Bleu clair** | `#6BB5E8` | rgb(107, 181, 232) | Dégradé de fond |
| **Blanc** | `#FFFFFF` | rgb(255, 255, 255) | Cartes, texte sur fond bleu |

### Couleurs de notation

#### 🌟 Excellent (≥ 180 points)
| Élément | Hex | RGB | Usage |
|---------|-----|-----|-------|
| Fond dégradé début | `#22c55e` | rgb(34, 197, 94) | Carte résultat |
| Fond dégradé fin | `#16a34a` | rgb(22, 163, 74) | Carte résultat |
| Badge fond | `#dcfce7` | rgb(220, 252, 231) | Badge catégorie |
| Badge texte | `#166534` | rgb(22, 101, 52) | Badge catégorie |

#### ✅ Bon (120-179 points)
| Élément | Hex | RGB | Usage |
|---------|-----|-----|-------|
| Fond dégradé début | `#84cc16` | rgb(132, 204, 22) | Carte résultat |
| Fond dégradé fin | `#65a30d` | rgb(101, 163, 13) | Carte résultat |
| Badge fond | `#d9f99d` | rgb(217, 249, 157) | Badge catégorie |
| Badge texte | `#3f6212` | rgb(63, 98, 18) | Badge catégorie |

#### ⚠️ Moyen (60-119 points)
| Élément | Hex | RGB | Usage |
|---------|-----|-----|-------|
| Fond dégradé début | `#f59e0b` | rgb(245, 158, 11) | Carte résultat |
| Fond dégradé fin | `#d97706` | rgb(217, 119, 6) | Carte résultat |
| Badge fond | `#fed7aa` | rgb(254, 215, 170) | Badge catégorie |
| Badge texte | `#9a3412` | rgb(154, 52, 18) | Badge catégorie |

#### ❌ Faible (< 60 points)
| Élément | Hex | RGB | Usage |
|---------|-----|-----|-------|
| Fond dégradé début | `#ef4444` | rgb(239, 68, 68) | Carte résultat |
| Fond dégradé fin | `#dc2626` | rgb(220, 38, 38) | Carte résultat |
| Badge fond | `#fee2e2` | rgb(254, 226, 226) | Badge catégorie |
| Badge texte | `#991b1b` | rgb(153, 27, 27) | Badge catégorie |

## Couleurs neutres

| Nom | Hex | RGB | Usage |
|-----|-----|-----|-------|
| Gris clair | `#f5f7fa` | rgb(245, 247, 250) | Fond info, upload |
| Gris moyen | `#e0e0e0` | rgb(224, 224, 224) | Bordures, sliders |
| Gris texte | `#777777` | rgb(119, 119, 119) | Descriptions |
| Noir texte | `#333333` | rgb(51, 51, 51) | Texte principal |

## Typographie

- **Famille** : 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Titre principal** : 2.5em, bold, text-shadow
- **Sous-titre** : 1.1em
- **Titres cartes** : 1.5em, color: #4B91DA
- **Score** : 4em, bold
- **Labels** : 1em, weight: 600

## Espacements

- **Padding cartes** : 25px
- **Gap grille** : 20px
- **Border-radius cartes** : 15px
- **Border-radius boutons** : 8px
- **Border-radius badges** : 25px

## Ombres

- **Cartes** : `0 10px 30px rgba(0,0,0,0.2)`
- **Boutons hover** : `0 5px 15px rgba(0,0,0,0.2)`
- **Texte header** : `2px 2px 4px rgba(0,0,0,0.3)`

## Transitions

- **Durée standard** : 0.3s
- **Easing** : ease (défaut)
- **Hover boutons** : transform translateY(-2px)

## Responsive

### Breakpoints
- **Mobile** : max-width: 968px
  - Grille : 1 colonne
  - Padding réduit
  
### Desktop
- **Largeur max** : 1200px
- **Grille** : 2 colonnes

## États interactifs

### Boutons
- **Normal** : background #4B91DA
- **Hover** : background #2A5E9D, translateY(-2px)
- **Active** : translateY(0)

### Sliders
- **Normal** : background #4B91DA
- **Hover** : background #2A5E9D

### Inputs
- **Normal** : border #e0e0e0
- **Focus** : border #4B91DA, outline: none

## Accessibilité

- **Contraste texte/fond** : Conforme WCAG AA
- **Taille minimum texte** : 14px (0.85em)
- **Zone cliquable minimum** : 40x40px (sliders, boutons)
- **Labels explicites** : Tous les inputs ont des labels
- **Focus visible** : Changement de bordure au focus

## Emojis utilisés

| Emoji | Unicode | Usage |
|-------|---------|-------|
| 🚊 | U+1F68A | Logo principal |
| 🚗 | U+1F697 | Pas de voiture |
| 🚶 | U+1F6B6 | Marche |
| 🚴 | U+1F6B4 | Vélo |
| 🚗👥 | U+1F697 U+1F465 | Covoiturage |
| 🚌 | U+1F68C | Multimodal |
| 🌱 | U+1F331 | CO2 |
| 🏷️ | U+1F3F7 | Tags |
| 🌟 | U+1F31F | Excellent |
| ✅ | U+2705 | Bon |
| ⚠️ | U+26A0 | Moyen |
| ❌ | U+274C | Faible |

## Exemples d'utilisation

### CSS - Dégradé principal
```css
background: linear-gradient(135deg, #4B91DA 0%, #6BB5E8 100%);
```

### CSS - Carte résultat Excellent
```css
background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
color: white;
```

### CSS - Badge catégorie
```css
.score-category {
    padding: 8px 20px;
    border-radius: 25px;
    font-weight: 600;
}

.category-excellent {
    background: #dcfce7;
    color: #166534;
}
```

---

**Version** : 2.0  
**Date** : Novembre 2025  
**Projet** : Hackathon IDFM 2025

