# Minecraft JSON Generator

A utility for generating structured Minecraft JSON files for blocks, items, recipes, advancements, and tags — tailored to your mod configuration.

---

## Renaming to Your Mod Name

Replace the `new_mod_name` attribute in `config/modname.json` with your mod name, then run:

python main.py --changeModName

---

## Sorting Tags and Language Files

Sorts all values in tag JSONs and entries in `en_us.json` alphabetically:

python main.py --sortTags

---

## Clearing Existing JSON Files in `resources/`

Deletes all generated JSON files under `resources/assets` and `resources/data`, while preserving important tag and language files:

python main.py --delete

---

## Types

Each entry in your `input.json` must specify a valid `type`. These types correspond to templates and define what fields are required.

---

### Block Types

- **block**  
  Basic block structure with model and blockstate.  
  - Required fields: `id`, `name`

- **block/gemblock**  
  Blocks crafted from a gem (e.g., emerald block, ruby block).  
  - Required fields: `id`, `name`, `gem`  
  - Optional fields:
    - `pickaxe`: `"stone"` or `"iron"` — adds to `needs_stone_tool` or `needs_iron_tool`
    - `beacon_block`: `true` — adds to `beacon_base_blocks`

- **block/slab**  
  Half-height blocks.  
  - Required fields: `id`, `name`, `full_block`  
  - Optional fields:
    - `tool`: `"axe"`, `"hoe"`, `"pickaxe"`, `"shovel"` — adds to `blocks/mineable/<tool>`

- **block/stairs**  
  Stairs with shape handling.  
  - Required fields: `id`, `name`, `full_block`  
  - Optional fields:
    - `tool`: `"axe"`, `"hoe"`, `"pickaxe"`, `"shovel"` — adds to `blocks/mineable/<tool>`

- **block/wall**  
  Wall blocks for fences and partitions.  
  - Required fields: `id`, `name`, `full_block`  
  - Optional fields:
    - `tool`: `"axe"`, `"hoe"`, `"pickaxe"`, `"shovel"` — adds to `blocks/mineable/<tool>`

---

## Required Fields by Type

| Type              | Required Fields          |
|-------------------|--------------------------|
| block             | id, name                 |
| block/gemblock    | id, name, gem            |
| block/slab        | id, name, full_block     |
| block/stairs      | id, name, full_block     |
| block/wall        | id, name, full_block     |
| item              | id, name                 |
| item/gem          | id, name, gem_block      |
| item/axe          | id, name, material       |
| item/hoe          | id, name, material       |
| item/pickaxe      | id, name, material       |
| item/shovel       | id, name, material       |
| item/sword        | id, name, material       |
| item/helmet       | id, name, material       |
| item/chestplate   | id, name, material       |
| item/leggings     | id, name, material       |
| item/boots        | id, name, material       |
| set/tools         | id, name, material       |
| set/armor         | id, name, material       |

---

## Example Input
```json
[
  {
    "type": "item/gem",
    "id": "ruby",
    "name": "Ruby",
    "gem_block": "ruby_block",
    "beacon_payment": true
  },
  {
    "type": "block/gemblock",
    "id": "ruby_block",
    "name": "Ruby Block",
    "gem": "ruby",
    "pickaxe": "iron",
    "beacon_block": true
  },
  {
    "type": "block/slab",
    "id": "ruby_slab",
    "name": "Ruby Slab",
    "full_block": "ruby_block",
    "tool": "pickaxe"
  },
  {
    "type": "block/stairs",
    "id": "ruby_stairs",
    "name": "Ruby Stairs",
    "full_block": "ruby_block",
    "tool": "pickaxe"
  },
  {
    "type": "block/wall",
    "id": "ruby_wall",
    "name": "Ruby Wall",
    "full_block": "ruby_block",
    "tool": "pickaxe"
  }
]

