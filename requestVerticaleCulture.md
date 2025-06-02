# Conception des requêtes pour la verticale Culture
## Contexte
Ce document a pour objectif de documenter les requêtes API utilisées dans le cadre de la nouvelle verticale Culture sur le site de diffusion des données ouvertes.

URL du site en préproduction : culture.preprod.data.gouv.fr

Info dépots Github : 
Officiel pour la gestion des verticales : https://github.com/opendatateam/udata-front-kit

### Info conception des requêtes

- ID Organization Ministère de la Culture : 534fff91a3a7292c64a77f73
- Exemple ID Dataset Liste des festivals en France : 62cf95993d99f22480f49334 
- Exemple ID Ressource : 47ac11c2-8a00-46a7-9fa8-9b802643f975
- https://www.data.gouv.fr/fr/datasets/r/47ac11c2-8a00-46a7-9fa8-9b802643f975


### Documentation des APIs


- API Data.gouv : https://doc.data.gouv.fr/api/reference/
- API Explore (uniquement jeux csv et json avec une limite de taille): https://tabular-api.data.gouv.fr/api/doc

-  https://tabular-api.data.gouv.fr/api/resources/47ac11c2-8a00-46a7-9fa8-9b802643f975/data/




### Bloc — Nouveaux jeux de données
Promesse UX : une mise en avant
des nouveaux jeux de données –

#### Description
Afficher en page d’accueil ou section dédiée les jeux de données récemment publiés par le ministère de la Culture.



#### Spécifications de la requête

Tri décroissant sur la date de création : sort=-created

Filtrage par ID de l’organisation

Limitation à 10 résultats

Temporalité de mise à jour : quotidienne


#### Request URL
```
https://www.data.gouv.fr/api/1/datasets/?sort=-created&page=1&page_size=10&organization=534fff91a3a7292c64a77f73

```

##### Powershell
```
curl -X 'GET' \
  'https://www.data.gouv.fr/api/1/datasets/?sort=-created&page=1&page_size=10&organization=534fff91a3a7292c64a77f73' \
  -H 'accept: application/json'
```
##### Script python 

```
import requests

# URL de l'API pour les 10 derniers jeux créés du ministère de la Culture
url = "https://www.data.gouv.fr/api/1/datasets/?sort=-created&page=1&page_size=10&organization=534fff91a3a7292c64a77f73"

# Requête API
response = requests.get(url)
response.raise_for_status()  # en cas d'erreur HTTP
datasets = response.json()["data"]

# Parcours des jeux de données
for dataset in datasets:
    title = dataset["title"]
    dataset_id = dataset["id"]
    dataset_url = f"https://www.data.gouv.fr/fr/datasets/{dataset_id}"
    print(f"{title} — {dataset_url}")

```

### Bloc — TOP 10 des jeux les plus réutilisés
Promesse UX : une mise en avant
des nouveaux jeux de données –
Mettre en valeur les jeux de données du ministère qui génèrent le plus d’impact par leurs réutilisations concrètes (visualisations, outils, services, articles, etc.).

#### Description
Les 10 jeux de données les plus réutilisés

#### Spécifications de la requête
- Tri décroissant sur le nombre de réutilisations : sort=-reuses
- Filtrage par ID de l’organisation
- Limitation à 10 résultats

Temporalité de mise à jour : mensuelle

#### Request URL
```
https://www.data.gouv.fr/api/1/datasets/?sort=-reuses&page=1&page_size=10&organization=534fff91a3a7292c64a77f73
```

