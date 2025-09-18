import requests
import json
from collections import defaultdict

# URL API pour récupérer les datasets tagués "culture"
url = "https://www.data.gouv.fr/api/1/datasets/?tag=culture"
response = requests.get(url)
data = response.json()

# Regroupement des jeux par organisation
orgs = defaultdict(lambda: {
    "id": None,
    "datasets": []
})

# Parcours des jeux de données
for dataset in data["data"]:
    org = dataset.get("organization")
    if not org:
        continue

    org_name = org["name"]
    org_id = org["id"]

    orgs[org_name]["id"] = org_id
    orgs[org_name]["datasets"].append({
        "title": dataset["title"],
        "id": dataset["id"],
        "page": dataset["page"]
    })

# Sauvegarde au format JSON UTF-8
with open("OrgaCulture.json", "w", encoding="utf-8") as f:
    json.dump(orgs, f, indent=2, ensure_ascii=False)

print("Fichier OrgaCulture.json généré avec succès.")
