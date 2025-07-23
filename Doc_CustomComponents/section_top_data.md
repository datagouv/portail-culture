# À explorer en priorité
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
    - le titre : exeemple "🔥 Explorez les données en vue"
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
