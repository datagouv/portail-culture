# 📘 Verticale *Culture* - données dynamiques

## Présentation générale

| Information | Valeur |
|--------------|--------|
| **Fichier source** | `verticales/culture/DAG.py` |
| **Description** | Ce traitement automatise la préparation et la mise à jour des données affichées sur **[culture.data.gouv.fr](https://culture.data.gouv.fr)**. |
| **Fréquence de mise à jour** | Hebdomadaire |
| **Données sources** | `Grist` (contenus éditoriaux) et `catalogue data.gouv.fr` (statistiques d’usage) |
| **Données de sortie** | `Minio` (exports) et `Grist` (mises à jour du document Portail-Culture) |
| **Canal Mattermost d’information** | `~startup-datagouv-dataeng` |

---

## Qu’est-ce qu’un DAG ?

Un **DAG** (*Directed Acyclic Graph*) est un **workflow automatisé** défini dans **Apache Airflow**.  
Il décrit une série de **tâches planifiées** à exécuter dans un **ordre précis**, sans boucle.

> Autrement dit, c’est une **routine planifiée** qui s’exécute automatiquement selon un scénario défini.

---

##  Fonctionnement global

### Étape 1 — Collecte et agrégation des données

**Fichier concerné :**  
`datagouvfr_data_pipelines/verticales/culture/task_functions.py`

- Les tâches du DAG interrogent l’API `data.gouv.fr` pour chaque organisation et jeu de données du périmètre “Culture”.
- Les statistiques mensuelles (vues, téléchargements, réutilisations…) sont **additionnées** pour obtenir un total sur les **12 derniers mois**.
- Ces totaux sont enregistrés sous forme d’objets standardisés :
  - par type (`datasets`, `organizations`, `reuses`),
  - avec des clés normalisées (`views_datasets`, `downloads_resources`, `reuses`, etc.).

---

### Étape 2 — Publication dans Grist

**Fichier concerné :**  
`tâche Airflow “send_to_grist”`

- Les données agrégées sont injectées dans le document **Grist “Portail-Culture”** via l’API Grist :
  - Table `Table1` → structure des sections (titres, couleurs, types de blocs),
  - Table `Content_section` → contenus éditoriaux (textes, liens, images),
  - Table `Tops` → jeux de données les plus consultés, les plus réutilisés, ou les plus récents.
- Grist joue donc le rôle de **CMS éditorial et base de données publique** pour la verticale.

---

### Étape 3 — Diffusion et affichage sur le site

**Fichier concerné :**  
`src/custom/culture/views/HomeView.vue`

- Le front Vue.js de `culture.data.gouv.fr` **appelle directement l’API Grist** :
  - `/Table1/records` → structure des sections  
  - `/Content_section/records` → contenus associés  
  - `/Tops/records` → tops calculés par le pipeline
- Les réponses JSON sont intégrées dans les composants Vue (`CultureDatasetCard`, `SearchComponent`, etc.).
- Le site génère dynamiquement :
  - les blocs éditoriaux (cartes, tags, highlights),
  - et les sections “Jeux de données les plus consultés / réutilisés / récents”.
