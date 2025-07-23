# Focus & discussions
ID : section_focus_discussion  

## Objectif  
Offrir une respiration éditoriale en valorisant des jeux de données sélectionnés manuellement ou semi-automatiquement (jeu du mois, données structurantes), tout en favorisant les échanges autour des données culturelles via des liens vers la communauté. Ce bloc renforce l'engagement et la compréhension en croisant contenus phares et interactions.

## Automatisation  
Partiellement automatisé : certaines cards sont éditoriales (jeu du mois), d'autres issues de tags ou liens dynamiques.

## Périodicité d’actualisation  
Mensuelle pour l’éditorial (jeu du mois)  
Dynamique pour les autres sources

## Contenu  
- titre de la section :  
- chaque carte présente :  
  - un titre (exemple : "💬 Participez aux discussions")  
  - une image (disponible au sein du répertoire asset)  
  - une description  
  - redirection vers la source (page jeu, liste ou forum)

## Composant DSFR  
Type : Card ou Card contenu enrichi  
Style : `fr-card`, `fr-card--horizontal`, `fr-card--sm`

## Spécifications des cards

| Élément               | Emoji | Type de source                                                            | Nombre   | Objectif                                               |
|-----------------------|:-----:|----------------------------------------------------------------------------|----------|--------------------------------------------------------|
| Jeu du mois           | ✨     | Éditorial / semi-automatisé                                               | 1        | Donner un coup de projecteur mensuel                  |
| Données de référence  | 🧽     | `tag=base-reference`                                                      | illimité | Mettre en avant les bases structurantes du ministère  |
| Dernières discussions | 💬     | [forum.data.gouv.fr/tag/culture](https://forum.data.gouv.fr/tag/culture) | -        | Créer du lien avec la communauté et ses usages réels  |

---

## Code YAML

```yaml
- title: Focus & discussions
  id: section_focus_discussion
  content:
    sub_section_datasets:
    sub_section_cards:
      title:
      cards:
        - name: '✨ Jeu du mois'
          description: 'Chaque mois, découvrez un jeu de données mis à l’honneur pour sa pertinence ou son impact.'
          url: '/datasets/jeu-du-mois'
          image_url: '/culture/assets/jeu_mois.png'
        - name: '🧽 Données de référence'
          description: 'Explorez les bases de données structurantes du ministère de la Culture.'
          url: 'datasets?tag=base-reference'
          image_url: '/culture/assets/bases_reference.png'
        - name: '💬 Discussions en cours'
          description: 'Participez aux échanges autour des données culturelles sur le forum.'
          url: 'https://forum.data.gouv.fr/tag/culture'
          image_url: '/culture/assets/forum.png'
    sub_section_tiles:
    sub_section_buttons:
```
