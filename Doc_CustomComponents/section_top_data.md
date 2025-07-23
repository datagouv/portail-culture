# section_top_data


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
    - Redirection vers résulttats de la requête API (


Composant DSFR :  

Type : Card ou Card contenu enrichi
Style : fr-card, fr-card--horizontal, fr-card—sm
<img width="647" height="455" alt="image" src="https://github.com/user-attachments/assets/6e748479-6868-4fed-8cc3-9db6951360ed" />


| Élément                  | Emoji | Type de tri/API    |Nombre| Objectif                                      | UX/UI                                                        |                                     
|:------------------------ |:----- |:------------------ |:----- |:--------------------------------------------- |:------------------------------------------------------------ |
| Jeux les plus consultés  | 🔥    | `sort=-views`      |20| Mettre en avant les contenus à forte audience | Bon point d’entrée. Limitation à 3 cards évite la surcharge. |
| Jeux les plus réutilisés | ♻️    | `sort=-reuses`     |20| Valoriser les rétuilisation et données les plus reprises       | Valorise les tendances actuelles            |
| Nouveaux jeux publiés    | 🆕    | `sort=-created_at` |20| Montrer les dernières publications            | Permet la découverte de nouveautés                           |
