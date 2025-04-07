# Minecraft JSON Generator

## Renaming to Your Mod Name
Replace the new_mod_name attribute in config.json with your mod name, then run:
```
python main.py --changeModName
```

## Sort Tags & Lang Json Files
Run this:
```
python main.py --sortTags
```

## Clearing Existing JSON Files in Resources
Run this:
```
python main.py --delete
```

## Types
- "block/gemblock": Gem blocks (like diamond blocks)
    - "gem": The gem of the gem block to craft with

- "item": Basic items
- "item/gem": Gems such as diamonds that can be crafted into blocks or tools
    - "gemblock": The gem block that the item can be crafted into
