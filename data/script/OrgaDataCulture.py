import requests
import pandas as pd
import time
from collections import defaultdict

BASE_URL = "https://www.data.gouv.fr/api/1/datasets/"
TAG = "culture"
PAGE_SIZE = 100
MAX_RETRY = 5

headers = {
    "User-Agent": "MinCultureDataBot/1.0 (+https://culture.data.gouv.fr)"
}

def fetch_page(page):
    url = f"{BASE_URL}?tag={TAG}&page={page}&page_size={PAGE_SIZE}"
    retries = 0

    while retries < MAX_RETRY:
        try:
            r = requests.get(url, headers=headers, timeout=30, stream=True)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            retries += 1
            wait = retries * 2
            print(f"⚠️ Error loading page {page}, retry {retries}/{MAX_RETRY}... waiting {wait}s ({e})")
            time.sleep(wait)

    print(f"❌ Failed to fetch page {page} after retries.")
    return None

def fetch_all_culture_datasets():
    page = 1
    all_results = []

    while True:
        print(f"Fetching page {page}...")
        data = fetch_page(page)

        if not data or "data" not in data or len(data["data"]) == 0:
            print("✅ Finished pagination")
            break

        all_results.extend(data["data"])
        page += 1

        time.sleep(0.6)  # respect API rate limits

    return all_results

# --- Main extraction logic ---

datasets = fetch_all_culture_datasets()

orgs = defaultdict(lambda: {
    "id": None,
    "badge": None,
    "count": 0
})

for ds in datasets:
    org = ds.get("organization")
    if not org:
        continue

    name = org["name"]
    orgs[name]["id"] = org["id"]
    badges = org.get("badges", [])

    orgs[name]["badge"] = badges[0]["kind"] if badges else "unknown"
    orgs[name]["count"] += 1

# Convert to DataFrame
df = pd.DataFrame([
    {"organisation": name, "id": data["id"], "type": data["badge"], "datasets_count": data["count"]}
    for name, data in orgs.items()
]).sort_values(by="datasets_count", ascending=False)

# Save CSV + JSON
df.to_csv("data/organisation_count_culture.csv", index=False)
df.to_json("data/organisation_culture.json", orient="records", force_ascii=False)

print("✅ Files generated:")
print(" - data/organisation_culture.json")
print(" - data/organisation_count_culture.csv")
