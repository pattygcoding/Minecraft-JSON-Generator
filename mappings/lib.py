import os
import json

def getJsonMap(category, name):
    path = os.path.join("mappings", category, f"{name}.json")
    with open(path, "r") as f:
        return json.load(f)