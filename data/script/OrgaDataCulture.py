import requests
import pandas as pd
import time
from collections import defaultdict

BASE_URL = "https://www.data.gouv.fr/api/1"
TAG = "culture"
PAGE_SIZE = 100
MAX_RETRY = 5

headers = {
    "User-Agent": "MinCultureDataBot/1.0 (+https://culture.data.gouv.fr)"
}

def retry_get(url):
    retries = 0
    while retries < MAX_RETRY:
        try:
            r = requests.get(url, headers=headers, timeout=30)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            retries += 1
            wait = retries * 2
            print(f"⚠️ Error fetching {url}, retry {retries}/{MAX_RETRY}, wait {wait}s — ({e})")
            time.sleep(wait)
    print(f"❌ Failed after {MAX_RETRY} retries: {url}")
    return None

def fetch_all_datasets():
    page = 1
    results = []

    while True:
        print(f"📄 Fetching page {page}...")
        url = f"{BASE_URL}/datasets/?tag={TAG}&page={page}&page_size={PAGE_SIZE}"
        data = retry_get(url)

        if not data or len(data.get("data", [])) == 0:
            print("✅ Pagination terminée")
            break

        results.extend(data["data"])
        page += 1
        time.sleep(0.5)

    return results

def fetch_org_details(org_id):
    url = f"{BASE_URL}/organizations/{org_id}/"
    return retry_get(url)

# --- MAIN ---

datasets = fetch_all_datasets()

orgs = defaultdict(lambda: {
    "id": None,
    "name": None,
    "siret": None,
    "badges": [],
    "datasets_count": 0
})

# Collect base org data from datasets listing
for ds in datasets:
    org = ds.get("organization")
    if not org: 
        continue

    name = org.get("name")
    orgs[name]["id"] = org.get("id")
    orgs[name]["name"] = name

    # badges from dataset listing
    badges = org.get("badges", [])
    orgs[name]["badges"] = list(set(orgs[name]["badges"] + [b.get("kind") for b in badges if "kind" in b]))
    orgs[name]["datasets_count"] += 1

# Fetch SIRETs via org API
print("\n🏛️ Récupération des SIRET pour chaque organisation…\n")

for name, info in orgs.items():
    org_id = info["id"]
    if not org_id:
        continue

    org_data = fetch_org_details(org_id)
    if org_data:
        orgs[name]["siret"] = org_data.get("business_number_id")

    time.sleep(0.3)  # polite delay

# Build dataframe
df = pd.DataFrame([
    {
        "organisation": info["name"],
        "id": info["id"],
        "siret": info["siret"],
        "badges": ", ".join(info["badges"]) if info["badges"] else "none",
        "datasets_count": info["datasets_count"]
    }
    for info in orgs.values()
]).sort_values(by="datasets_count", ascending=False)

df.to_csv("data/organisation_count_culture.csv", index=False)
df.to_json("data/organisation_culture.json", orient="records", force_ascii=False)

print("\n✅ Terminé — fichiers générés :")
print(" - data/organisation_count_culture.csv")
print(" - data/organisation_culture.json")
