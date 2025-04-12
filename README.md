# Minecraft JSON Generator

A utility for generating structured Minecraft JSON files for blocks, items, recipes, advancements, and tags — tailored to your mod configuration.

---

## Renaming to Your Mod Name

Replace the `new_mod_name` attribute in `config.json` with your mod name, then run:
```python
python main.py --changeModName
```
---

## Sorting Tags and Language Files

Sorts all values in tag JSONs and entries in `en_us.json` alphabetically:
```python
python main.py --sortTags
```
---

## Clearing Existing JSON Files in `resources/`

Deletes all generated JSON files under `resources/assets` and `resources/data`:
```python
python main.py --delete
```
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

---

### Item Types

- **item**  
  A basic standalone item.  
  - Required fields: `id`, `name`

- **item/gem**  
  Craftable gem items (e.g., ruby, diamond).  
  - Required fields: `id`, `name`, `gem_block`

- **Tool Items**  
  Types: `item/axe`, `item/hoe`, `item/pickaxe`, `item/shovel`, `item/sword`  
  - Required fields: `id`, `name`, `material`

- **Armor Items**  
  Types: `item/helmet`, `item/chestplate`, `item/leggings`, `item/boots`  
  - Required fields: `id`, `name`, `material`

---

### Set Types

Set types automatically generate full sets of tool or armor entries based on a base ID and material.

- **set/tools**  
  Generates: `axe`, `pickaxe`, `shovel`, `sword`, `hoe`  
  - Required fields: `id`, `name`, `material`

- **set/armor**  
  Generates: `helmet`, `chestplate`, `leggings`, `boots`  
  - Required fields: `id`, `name`, `material`

---

## Required Fields by Type

| Type              | Required Fields          |
|-------------------|--------------------------|
| block             | id, name                 |
| block/gemblock    | id, name, gem            |
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

## Output Directory Structure

Generated files are written to the following locations:

resources/  
├── assets/  
│   └── <mod_name>/  
│       ├── blockstates/  
│       ├── models/  
│       │   ├── block/  
│       │   └── item/  
│       └── lang/  
└── data/  
    └── <mod_name>/  
        ├── recipes/  
        ├── advancements/  
        └── tags/

Tags for common Minecraft namespaces (like `minecraft:beacon_payment_items`) are also created under `data/minecraft/tags`.

---

## Example Input

[
  {
    "type": "item/gem",
    "id": "ruby",
    "name": "Ruby",
    "gem_block": "ruby_block"
  },
  {
    "type": "set/tools",
    "id": "ruby",
    "name": "Ruby",
    "material": "ruby"
  },
  {
    "type": "set/armor",
    "id": "ruby",
    "name": "Ruby",
    "material": "ruby"
  }
]
