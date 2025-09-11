# Transversale des données culturelles

Documentation et prototypage pour la verticale Culture du portail de données ouvertes data.gouv.fr.

## 🌐 Environnements
- Production : https://culture.data.gouv.fr
- Préproduction : https://culture.preprod.data.gouv.fr | https://github.com/opendatateam/udata-front-kit/tree/culture-preprod
- Forum des verticales : https://github.com/opendatateam/udata-front-kit/discussions/categories/general
- Gestion de la section automatisée : mise à jour régulière des blocs (ex. « Nouveaux jeux de données », « Top réutilisations ») selon des temporalités différenciées (quotidien / mensuel). : https://github.com/datagouv/datagouvfr_data_pipelines/tree/main/verticales/culture




## 🎯 Objectif du dépôt
Ce dépôt centralise les éléments de documentation et les ébauches de composants utilisés pour construire et enrichir la page d’accueil de la verticale Culture, en cohérence avec le Design System de l’État.

Il accompagne le travail UX/UI mené dans le cadre de la mission "Circulation et ouverture des données culturelles" au ministère de la Culture.

## 📁 Arborescence principale
### Doc_CustomComponents/
  Ce répertoire contient :
  - Des exemples et ébauches de sections et blocs pour la page d’accueil, au format Vue.js (.vue) ou HTML/CSS (.html)
  - Un sous-répertoire d’illustrations et images associées aux blocs réalisés (exemples de visuels illustratifs ou fonds de blocs)
  - Composition de la page d'accueil https://github.com/datagouv/portail-culture/blob/Documentation/Doc_CustomComponents/composition_accueil.md

### requestVerticaleCulture.md
Documente les requêtes API utilisées pour alimenter dynamiquement la verticale Culture :
- Requêtes vers l’API uData pour récupérer jeux de données, réutilisations, producteurs
- Filtres et paramètres spécifiques utilisés (thématique Culture, tags, tri, pagination)
- Requêtes typiques utilisées dans les blocs du portail (ex. : top datasets, dernières publications, visualisations associées)

## 🧪 Usage conseillé
Ce dépôt peut être utilisé pour :

💡 Préparer des ateliers UX/UI avec des prototypes visuels simples

🧱 Tester des combinaisons de blocs sur la page d’accueil (en local ou via preprod)

📝 Documenter le fonctionnement de chaque composant (fonction, cible, source de données)

🔄 Itérer rapidement sans impacter la branche de production

📌 Pour aller plus loin
🔧 Code source du portail : opendatateam/udata-front-kit (branche culture-preprod)

🧱 Design System utilisé : @gouvfr/dsfr

📁 Référentiel des composants : @datagouv/components
