import json
from src.modes.mode import mode
from src.mappings.template_map import template_map
from src.process_entries import process_entries

# Handle run options first (see README for more info)
if mode():
    exit(0)

# Load config
with open("config/modname.json", "r") as f:
    config = json.load(f)

# Obtain the mod name
mod_name = config.get("mod_name")

# Load all input objects from input.json (list of items)
with open("input.json", "r") as f:
    inputs = json.load(f)

# Process entries
process_entries(inputs, template_map, mod_name)
