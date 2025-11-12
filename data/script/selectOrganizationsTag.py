#!/usr/bin/env python3
import os
import json
from datagouv import Client, Dataset, Organization

TAG = os.getenv("TAG", "culture")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "data/organizations-datasets-tag.json")

EXCLUDED_ORG_IDS = {
    "534fff8ca3a7292c64a77edf",  # Ministère de l'Agriculture

}

def should_exclude(org):
    if org.id in EXCLUDED_ORG_IDS:
        return True
    return False

client = Client()

def main():
    print(f"→ Récupération des organisations pour les jeux de données tagués '{TAG}'")

    datasets = list(
        client.get_all_from_api_query(
            f"api/1/datasets/?tag={TAG}",
            mask="data{id,title,organization{id,name,slug},resources{id}}",
            cast_as=Dataset,
        )
    )

    print(f"  {len(datasets)} jeux de données récupérés depuis {client.base_url}")

    organizations = {}
    for dataset in datasets:
        organization = dataset.organization
        if not isinstance(organization, Organization):
            continue
        if should_exclude(organization):
            continue

        if organization.id not in organizations:
            organizations[organization.id] = {
                "id": organization.id,
                "name": organization.name,
            }

    sorted_organizations = sorted(
        organizations.values(), key=lambda o: (o.get("name") or "").lower()
    )

    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted_organizations, f, ensure_ascii=False, indent=2)

    print(f"✓ {len(sorted_organizations)} organisations exportées dans {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
