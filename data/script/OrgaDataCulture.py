import requests
import json
import pandas as pd
from collections import defaultdict

BASE_URL = "https://www.data.gouv.fr/api/1/datasets/?tag=culture"
PAGE_SIZE = 100  # Max safe page size

def fetch_all_culture_datasets():
    page = 1
    all_data = []

    while True:
        url = f"{BASE_URL}&page={page}&page_size={PAGE_SIZE}"
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()

        if "data" not in data or len(data["data"]) == 0:
            break

        all_data.extend(data["data"])
        page += 1

    return all_data

datasets = fetch_all_culture_datasets()

# Regroupement par organisation
orgs = defaultdict(lambda: {"id": None, "count": 0})

for d in datasets:
    org = d.get("organization")
    if not org:
        continue

    orgs[org["name"]]["id"] = org["id"]
    orgs[org["name"]]["count"] += 1

# JSON output
with open("./data/organisation_culture.json", "w", encoding="utf-8") as f:
    json.dump(orgs, f, indent=2, ensure_ascii=False)

# CSV output
df = pd.DataFrame([
    {"organization_name": name, "organization_id": info["id"], "dataset_count": info["count"]}
    for name, info in orgs.items()
])

df.to_csv("./data/organisation_count_culture.csv", index=False, encoding="utf-8")

print("✅ Fichiers générés :")
print("- data/organisation_culture.json")
print("- data/organisation_count_culture.csv")
