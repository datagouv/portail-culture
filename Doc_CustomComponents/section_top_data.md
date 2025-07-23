# section_top_data


## Objectif
Mettre en valeur les jeux de données les plus consultés sur la plateforme, afin d’encourager l’exploration des ressources jugées pertinentes ou utiles par la communauté. Ce bloc permet de valoriser les données à fort impact et d'orienter les utilisateurs vers les contenus les plus visités.

## Automatisation
Automatisé, les liens des cards sont des requêtes de l'API avec un tri dynamique selon nombre de vues, réutilisations

## Périodicité d’actualisation
Actualisation dynamique


| Élément                  | Emoji | Type de tri/API    | Objectif                                      | UX/UI                                                        |                                     
|:------------------------ |:----- |:------------------ |:--------------------------------------------- |:------------------------------------------------------------ |
| Jeux les plus consultés  | 🔥    | `sort=-views`      | Mettre en avant les contenus à forte audience | Bon point d’entrée. Limitation à 3 cards évite la surcharge. |
| Jeux les plus réutilisés | ♻️    | `sort=-reuses`     | Valoriser les rétuilisation et données les plus reprises       | Valorise les tendances actuelles            |
| Nouveaux jeux publiés    | 🆕    | `sort=-created_at` | Montrer les dernières publications            | Permet la découverte de nouveautés                           |
