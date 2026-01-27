from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, TYPE_CHECKING
from worlds.bits_and_bops import *
from .regions import level_names, cartridge_names
from typing import Dict, Optional
from BaseClasses import Item, ItemClassification, MultiWorld, Location
from .data import *

class BitsAndBopsItem(Item):
    game: str = "Bits & Bops"


def get_random_item_names(rand, k: int, weights: dict[str, int]) -> list[str]:
    random_items = rand.choices(
        list(weights.keys()),
        weights=list(weights.values()),
        k=k)
    return random_items


def create_single(name: str, world: BitsAndBopsWorld, item_class: ItemClassification = None) -> None:
    classification = world.item_table[name].classification if item_class is None else item_class
    world.itempool.append(BitsAndBopsItem(name, classification, world.item_table[name].code, world.player))


def create_multiple(name: str, amount: int, world: BitsAndBopsWorld, item_class: ItemClassification = None):
    for i in range(amount):
        create_single(name, world, item_class)


def create_items(world: BitsAndBopsWorld):
    total_location_count: int = len(world.multiworld.get_unfilled_locations(world.player))

    starting_level = level_names[world.random.randint(0, len(level_names) - 1)]
    world.multiworld.push_precollected(world.create_item(f"{starting_level} Unlock"))

    for level_name in level_names:
        if level_name != starting_level:
            create_single(f"{level_name} Unlock", world)
    if has_records(world):
        for level_name in level_names:
            create_single(f"{level_name} Record", world)
    if world.options.badgesanity:
        create_single("Symphony Cartridge", world)
        create_single("Three-Legged Race Cartridge", world)
        create_single("Blacksmith Cartridge", world)
        create_single("Encore Cartridge", world)

    # Junk
    remaining_locations: int = total_location_count - len(world.multiworld.worlds[world.player].itempool)
    #trap_count: int = round(remaining_locations * options.trap_fill_percentage / 100)
    junk_count: int = remaining_locations
    junk = get_random_item_names(world.random, junk_count, junk_weights)
    for name in junk:
        create_single(name, world)
    #traps = get_random_item_names(world.random, trap_count, trap_weights)
    #for name in traps:
    #    create_single(name, world)
    world.multiworld.itempool += world.itempool


def get_item_groups():
    unlocks = set()
    records = set()
    for level_name in level_names:
        unlocks.add(f"{level_name} Unlock")
        records.add(f"{level_name} Record")
    carts = set()
    for cart_name in cartridge_names:
        carts.add(f"{cart_name} Cartridge")
    return {"Level Unlock": unlocks, "Record": records, "Cartridge": carts}


@dataclass(frozen=True)
class ItemData:
    code: Optional[int]
    classification: Optional[ItemClassification]


def generate_item_table() -> Dict[str, ItemData]:
    item_table = {}
    for i, level in enumerate(level_names):
        item_table[f"{level} Unlock"] = ItemData(i + 0x1, ItemClassification.progression)
    for i, cart in enumerate(cartridge_names):
        item_table[cart] = ItemData(i + 0x15, ItemClassification.progression)
    for i, level in enumerate(level_names):
        item_table[f"{level} Record"] = ItemData(i + 0x19, ItemClassification.progression)
    item_table["Random Souvenir"] = ItemData(0x100, ItemClassification.filler)
    item_table["Random Video Tape"] = ItemData(0x101, ItemClassification.filler)
    return item_table


bits_and_bops_item_table = generate_item_table()
bits_and_bops_item_name_groups = get_item_groups()


junk_weights = {
    "Random Souvenir":   10,
    "Random Video Tape": 10
}


trap_weights = {
}