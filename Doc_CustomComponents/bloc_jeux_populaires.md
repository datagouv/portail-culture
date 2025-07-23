# Bloc : jeux les plus populaires
Identifiant : bloc_jeux_populaires

## Objectif
Mettre en valeur les jeux de données les plus consultés sur la plateforme, afin d’encourager l’exploration des ressources jugées pertinentes ou utiles par la communauté. Ce bloc permet de valoriser les données à fort impact et de guider les utilisateurs vers les contenus les plus visités.

## Gestion
- automatisée, basée sur les statistiques de consultation de data.gouv.fr (via API). Tri dynamique selon la popularité : nombre de vues, téléchargements ou interactions.

## Périodicité d’actualisation : 
- actualisation mensuelle

## Composant DSFR : 
- Type : Card ou Card contenu enrichi
- Style : fr-card, fr-card--horizontal, fr-card—sm
- Modèle d’intégration : composant custom vue alimenté par un fichier .json (préchargé via script/API)
  - https://vue-ds.fr/composants/DsfrCard
  - https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/carte

## Fonctionnement :
Chaque carte présente :
- le titre du jeu de données (title)
- un extrait de sa description (description)
- (option en attente) le nom producteur (administration, établissement, collectivité)
- un bouton ou lien "→ Voir le jeu de données« 
- Redirection vers l’URL du jeu sur data.culture.gouv.fr.
- Un bouton sous le bloc permet l’accès aux jeux via tri sur views

## Spécifications de la requête :
- Tri : décroissant sur le nombre de réutilisations
sort=-views
- Filtrage : par ID d’organisation (ministère de la Culture) organization=534fff91a3a7292c64a77f73
- Limite : 3 résultats

