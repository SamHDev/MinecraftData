target = "578"

import os
from os.path import join
import json

data = {}
data["_"] = { "version": { "id": int(target), "name": "1.15.2"}, "includes": ["recipes", "advancements", "tags", "loot_tables", "blocks", "commands"] }

data["recipes"] = { "type": "multiple", "base": "/data/minecraft/recipes/", "files": [], "dirs": []  }
for file in os.listdir(f"versions/{target}/data/minecraft/recipes/"):
    data["recipes"]["files"].append(file)

data["advancements"] = { "type": "multiple", "base": "/data/minecraft/advancements/", "files": [], "dirs": [] }
for dir in os.listdir(f"versions/{target}/data/minecraft/advancements/"):
    data["advancements"]["dirs"].append(dir)
    for file in os.listdir(f"versions/{target}/data/minecraft/advancements/{dir}/"):
        data["advancements"]["files"].append(f"{dir}/{file}")

data["tags"] = { "type": "multiple", "base": "/data/minecraft/tags/", "files": [], "dirs": [] }
for dir in os.listdir(f"versions/{target}/data/minecraft/tags/"):
    data["tags"]["dirs"].append(dir)
    for file in os.listdir(f"versions/{target}/data/minecraft/tags/{dir}/"):
        data["tags"]["files"].append(f"{dir}/{file}")

data["loot_tables"] = { "type": "multiple", "base": "/data/minecraft/loot_tables/", "files": [], "dirs": [] }
for folder, subs, files in os.walk(f"versions/{target}/data/minecraft/loot_tables/"):
    for sub in subs:
        data["loot_tables"]["dirs"].append(f"{folder}/{sub}".replace(f"versions/{target}/data/minecraft/loot_tables/", "").lstrip("/"))
        for file in files:
            data["loot_tables"]["files"].append(f"{folder}/{sub}/{file}".replace(f"versions/{target}/data/minecraft/loot_tables/", "").lstrip("/"))

data["blocks"] = { "type": "single", "file": "/reports/blocks.json"}
data["commands"] = { "type": "single", "file": "/reports/commands.json"}


with open(join("versions", target, "index.json"), "w") as f:
    f.write(json.dumps(data, indent=4))
