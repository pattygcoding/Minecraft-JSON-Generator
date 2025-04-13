from src.mappings.helpers.template_map_helpers import *

t = "templates"

# Blocks
block = {t: [blockstate(), model_block(), model_item("block"), loot_table("block")]}
block_slab = {t: [blockstate("slab"), model_block(["block", "slab", "slab_top"]), model_item("block"), loot_table("slab")]}

# Block tool defaults
block_tool_pickaxe = {t: block[t] + [tag("blocks/mineable/pickaxe")]}

block_gemblock = {t: block_tool_pickaxe[t] + [recipe("gemblock"), advancement("recipes/building_blocks/gemblock")]}

# Items
item = {t: [model_item()]}
item_gem = {t: item[t] + [recipe("gem"), advancement("recipes/misc/gem")]}
item_axe = {t: item[t] + [recipe("axe"), advancement("recipes/tools/default")]}
item_pickaxe = {t: item[t] + [recipe("pickaxe"), advancement("recipes/tools/default")]}
item_shovel = {t: item[t] + [recipe("shovel"), advancement("recipes/tools/default")]}
item_hoe = {t: item[t] + [recipe("hoe"), advancement("recipes/tools/default")]}
item_sword = {t: item[t] + [recipe("sword"), advancement("recipes/combat/default")]}
item_helmet = {t: item[t] + [recipe("helmet"), advancement("recipes/combat/default"), tag("items/trimmable_armor")]}
item_chestplate = {t: item[t] + [recipe("chestplate"), advancement("recipes/combat/default"), tag("items/trimmable_armor")]}
item_leggings = {t: item[t] + [recipe("leggings"), advancement("recipes/combat/default"), tag("items/trimmable_armor")]}
item_boots = {t: item[t] + [recipe("boots"), advancement("recipes/combat/default"), tag("items/trimmable_armor")]}

# Sets
set_armor = {t: item_helmet[t] + item_chestplate[t] + item_leggings[t] + item_boots[t]}
set_tools = {t: item_axe[t] + item_pickaxe[t] + item_shovel[t] + item_sword[t] + item_hoe[t]}

template_map = {
    "block": block,
    "block/gemblock": block_gemblock,
    "block/gemblock/vanilla": block_gemblock,
    "item": item,
    "item/gem": item_gem,
    "item/axe": item_axe,
    "item/axe/vanilla": item_axe,
    "item/pickaxe": item_pickaxe,
    "item/pickaxe/vanilla": item_pickaxe,
    "item/shovel": item_shovel,
    "item/shovel/vanilla": item_shovel,
    "item/hoe": item_hoe,
    "item/hoe/vanilla": item_hoe,
    "item/sword": item_sword,
    "item/sword/vanilla": item_sword,
    "item/helmet": item_helmet,
    "item/helmet/vanilla": item_helmet,
    "item/chestplate": item_chestplate,
    "item/chestplate/vanilla": item_chestplate,
    "item/leggings": item_leggings,
    "item/leggings/vanilla": item_leggings,
    "item/boots": item_boots,
    "item/boots/vanilla": item_boots,
    "set/armor": set_armor,
    "set/armor/vanilla": set_armor,
    "set/tools": set_tools,
    "set/tools/vanilla": set_tools
}
