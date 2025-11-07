import requests
import json
import pandas as pd
from collections import defaultdict

BASE_URL = "https://www.data.gouv.fr/api/1/datasets/?tag=culture"
PAGE_SIZE = 100  # max allowed
MAX_PAGES = 100  # safety guard
import requests
import json
import pandas as pd
from collections import defaultdict

API_URL = "https://www.data.gouv.fr/api/1/datasets/"
TAG = "culture"
PAGE_SIZE = 100

def fetch_all_culture_datasets():
    page = 1
    results = []

    while True:
        url = f"{API_URL}?tag={TAG}&page={page}&page_size={PAGE_SIZE}"
        r = requests.get(url)
        if r.status_code == 404:  # plus de page suivante
            break
        
        r.raise_for_status()
        data = r.json()

        if not data["data"]:
            break

        results.extend(data["data"])
        page += 1

    return results

datasets = fetch_all_culture_datasets()

# Structure: { org_name: { id, count, badge } }
orgs = defaultdict(lambda: {"id": None, "count": 0, "badge": None})

for d in datasets:
    org = d.get("organization")
    if not org:
        continue

    name = org["name"]
    orgs[name]["id"] = org["id"]
    orgs[name]["count"] += 1

    badges = org.get("badges", [])
    if badges:
        orgs[name]["badge"] = badges[0].get("kind", "none")
    else:
        orgs[name]["badge"] = "none"

# ✅ JSON export
with open("./data/organisation_culture.json", "w", encoding="utf-8") as f:
    json.dump(orgs, f, indent=2, ensure_ascii=False)

# ✅ CSV export
df = pd.DataFrame([
    {
        "organization_name": name,
        "organization_id": info["id"],
        "dataset_count": info["count"],
        "organization_badge": info["badge"]
    }
    for name, info in orgs.items()
])

df.to_csv("./data/organisation_count_culture.csv", index=False, encoding="utf-8")

print("✅ Files generated:")
print(" - data/organisation_culture.json")
print(" - data/organisation_count_culture.csv")

def fetch_all_culture_datasets():
    page = 1
    all_data = []

    while page <= MAX_PAGES:
        url = f"{BASE_URL}&page={page}&page_size={PAGE_SIZE}"
        print(f"Fetching page {page}...")

        r = requests.get(url)

        # ✅ Stop if page doesn't exist
        if r.status_code == 404:
            print("✅ API returned 404, stopping pagination.")
            break

        r.raise_for_status()
        data = r.json()

        # ✅ No results means end of pagination
        if "data" not in data or len(data["data"]) == 0:
            print("✅ No more data, stopping pagination.")
            break

        all_data.extend(data["data"])
        page += 1

    print(f"📦 Total datasets fetched: {len(all_data)}")
    return all_data


datasets = fetch_all_culture_datasets()

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

print("✅ Files created:")
print("- data/organisation_culture.json")
print("- data/organisation_count_culture.csv")
