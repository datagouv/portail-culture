# 🔥 Découvrez les données phares
ID : section_top_data

## Objectif
Mettre en valeur les jeux de données les plus consultés sur la plateforme, afin d’encourager l’exploration des ressources jugées pertinentes ou utiles par la communauté. Ce bloc permet de valoriser les données à fort impact et d'orienter les utilisateurs vers les contenus les plus visités.

## Automatisation
Automatisé, les liens des cards sont des requêtes de l'API avec un tri dynamique selon nombre de vues, réutilisations

## Périodicité d’actualisation
Actualisation dynamique


## Contenu
- titre de la section : 
- chaque carte présente :
    - le titre : exeemple "Découvrez les données phares"
    - une image (disponible au sein du répertoire asset
    - une description (description)
    - Redirection vers résultats de la requête API


## Composant DSFR :  

Type : Card ou Card contenu enrichi
Style : fr-card, fr-card--horizontal, fr-card—sm

## Spécifications des cards

| Élément                  | Emoji | Requête API        | Nombre | Objectif                                               |
| :----------------------- | :---- | :----------------- | :----- | :----------------------------------------------------- |
| Jeux les plus consultés  | 🔥    | `sort=-views`      | 20     | Mettre en avant les contenus les plus populaires       |
| Jeux les plus réutilisés | ♻️    | `sort=-reuses`     | 20     | Valoriser les jeux fréquemment repris ou remixés       | 
| Nouveaux jeux publiés    | 🆕    | `sort=-created_at` | 20     | Montrer les dernières publications de données ouvertes | 


## Code Yaml
```
- title: 🔥 Explorez les données en vue
  id: section_top_data
  content:
    sub_section_datasets:
    sub_section_cards:
      title:
      cards:
        - name: '🔥 Jeux les plus consultés'
          description: 'Découvrez les jeux les plus populaires sur la plateforme, en fonction du nombre de vues.'
          url: 'datasets?sort=-views'
          image_url: '/culture/assets/patrimoine.png'
        - name: '♻️ Jeux les plus réutilisés'
          description: 'Explorez les jeux de données les plus réutilisés par la communauté.'
          url: 'datasets?sort=-reuses'
          image_url: '/culture/assets/audiovisuel.png'
        - name: '🆕 Nouveaux jeux publiés'
          description: 'Parcourez les nouveaux jeux de données publiés sur la plateforme.'
          url: 'datasets?sort=-created_at'
          image_url: '/culture/assets/musee.png'
    sub_section_tiles:
    sub_section_buttons:
```
