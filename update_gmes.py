#!/usr/bin/env python3
import os

ugs_dir = "ugs-singlefile/UGS-Files"
hydra_dir = "hydra-assets/gmes"

ugs_files = [f for f in os.listdir(ugs_dir) if f.endswith(".html")]
hydra_files = [f for f in os.listdir(hydra_dir) if f.endswith(".html")]


def find_hydra_match(ugs_file):
    base = ugs_file[2:-5]
    base_lower = base.lower()

    for hydra in hydra_files:
        hydra_base = hydra[:-5].lower().replace("-", "")
        if hydra_base in base_lower or base_lower in hydra_base:
            return hydra
    return None


updated = 0
for ugs_file in ugs_files:
    hydra_name = find_hydra_match(ugs_file)
    if hydra_name:
        ugs_path = os.path.join(ugs_dir, ugs_file)
        hydra_path = os.path.join(hydra_dir, hydra_name)
        with open(ugs_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        with open(hydra_path, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1

print(f"Updated: {updated}")
