from src.mappings.helpers.template_map_helpers import *

t = "templates"

# Blocks
block = {t: [blockstate(), inventory("block"), *model_block(), loot_table("block")]}

block_button = {t: [
    blockstate("button"),
    *model_block(["button", "button_inventory", "button_pressed"]),
    inventory("block_inventory"),
    loot_table(),
    recipe("button")(),
    advancement("recipes/redstone/cut_block")
]}

block_door = {t: [
    blockstate("button"),
    *model_block(["door_bottom_left", "door_bottom_right", "door_top_left", "door_top_right", "door_bottom_left_open", "door_bottom_right_open", "door_top_left_open", "door_top_right_open"]),
    inventory("item"),
    loot_table(),
    recipe("door"),
    advancement("recipes/redstone/cut_block")
]}

block_pressure_plate = {t: [
    blockstate("pressure_plate"),
    *model_block(["pressure_plate", "pressure_plate_down"]),
    inventory("block"),
    loot_table(),
    recipe("pressure_plate"),
    advancement("recipes/redstone/cut_block")
]}

block_slab = {t: [
    blockstate("slab"),
    *model_block(["slab", "slab_top"]),
    inventory("block"),
    loot_table("slab"),
    recipe("slab"),
    recipe("slab_from_full_block_stonecutting"),
    advancement("recipes/building_blocks/cut_block")
]}

block_stairs = {t: [
    blockstate("stairs"),
    *model_block(["stairs", "stairs_inner", "stairs_outer"]),
    loot_table(),
    recipe("stairs"),
    recipe("stairs_from_full_block_stonecutting"),
    advancement("recipes/building_blocks/cut_block")
]}

block_wall = {t: [
    blockstate("wall"),
    *model_block(["wall_inventory", "wall_post", "wall_side", "wall_side_tall"]),
    inventory("block_inventory"),
    loot_table(),
    recipe("wall"),
    recipe("wall_from_full_block_stonecutting"),
    advancement("recipes/building_blocks/cut_block")
]}


# Block tool defaults
block_tool_pickaxe = {t: block[t] + [tag("blocks/mineable/pickaxe")]}

block_gemblock = {t: block_tool_pickaxe[t] + [recipe("gem_block"), advancement("recipes/building_blocks/gem_block")]}

# Items
item = {t: [inventory("item"), model_item()]}
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

# Define the base template map
base_template_map = {
    "block": block,
    "block/button": block_button,
    "block/door": block_door,
    "block/gemblock": block_gemblock,
    "block/pressure_plate": block_pressure_plate,
    "block/slab": block_slab,
    "block/stairs": block_stairs,
    "block/wall": block_wall,
    "item": item,
    "item/gem": item_gem,
    "item/axe": item_axe,
    "item/pickaxe": item_pickaxe,
    "item/shovel": item_shovel,
    "item/hoe": item_hoe,
    "item/sword": item_sword,
    "item/helmet": item_helmet,
    "item/chestplate": item_chestplate,
    "item/leggings": item_leggings,
    "item/boots": item_boots,
    "set/armor": set_armor,
    "set/tools": set_tools
}

# Create template_map with vanilla variants included
template_map = {
    **base_template_map,
    **{f"{key}/vanilla": value for key, value in base_template_map.items()}
}
