from __future__ import annotations
from typing import Dict, Optional, TYPE_CHECKING
from worlds.bits_and_bops import *
from .regions import level_names, cartridge_names
from typing import Dict, Optional
from BaseClasses import Item, ItemClassification, MultiWorld, Location
from .data import *

class BitsAndBopsItem(Item):
    game: str = "Bits & Bops"


def get_random_item_names(rand, k: int, weights: dict[str, int]) -> str:
    random_items = rand.choices(
        list(weights.keys()),
        weights=list(weights.values()),
        k=k)
    return random_items


def create_single(name: str, world: BitsAndBopsWorld, item_class: ItemClassification = None) -> None:
    classification = bits_and_bops_item_table[name].classification if item_class is None else item_class
    world.itempool.append(BitsAndBopsItem(name, classification, bits_and_bops_item_table[name].code, world.player))


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
    # Generic
    if has_records(world):
        create_single("Flipper Snapper Record", world)
        create_single("Sweet Tooth Record", world)
        create_single("Rock, Paper, Showdown! Record", world)
        create_single("Pantry Parade Record", world)
        create_single("Jungle Mixtape Record", world)
        create_single("B-Bot & the Fly Girls Record", world)
        create_single("Flow Worms Record", world)
        create_single("Meet & Tweet Record", world)
        create_single("Steady Bears Record", world)
        create_single("Sky Mixtape Record", world)
        create_single("Pop Up Kitchen Record", world)
        create_single("Firework Festival Record", world)
        create_single("Hammer Time! Record", world)
        create_single("Molecano Record", world)
        create_single("Ocean Mixtape Record", world)
        create_single("President Bird Record", world)
        create_single("Snakedown Record", world)
        create_single("Octeaparty Record", world)
        create_single("Globe Trotters Record", world)
        create_single("Fire Mixtape Record", world)
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
        carts.add(cart_name)
    return {"Level Unlock": unlocks, "Record": records, "Cartridge": carts}


class ItemData:
    def __init__(self, code: Optional[int], classification: Optional[ItemClassification]):
        self.code = code
        self.classification = classification


bits_and_bops_item_table: Dict[str, ItemData] = {
    "Flipper Snapper Unlock":        ItemData(0x1, ItemClassification.progression),
    "Sweet Tooth Unlock":            ItemData(0x2, ItemClassification.progression),
    "Rock, Paper, Showdown! Unlock": ItemData(0x3, ItemClassification.progression),
    "Pantry Parade Unlock":          ItemData(0x4, ItemClassification.progression),
    "Jungle Mixtape Unlock":         ItemData(0x5, ItemClassification.progression),
    "B-Bot & the Fly Girls Unlock":  ItemData(0x6, ItemClassification.progression),
    "Flow Worms Unlock":             ItemData(0x7, ItemClassification.progression),
    "Meet & Tweet Unlock":           ItemData(0x8, ItemClassification.progression),
    "Steady Bears Unlock":           ItemData(0x9, ItemClassification.progression),
    "Sky Mixtape Unlock":            ItemData(0xA, ItemClassification.progression),
    "Pop Up Kitchen Unlock":         ItemData(0xB, ItemClassification.progression),
    "Firework Festival Unlock":      ItemData(0xC, ItemClassification.progression),
    "Hammer Time! Unlock":           ItemData(0xD, ItemClassification.progression),
    "Molecano Unlock":               ItemData(0xE, ItemClassification.progression),
    "Ocean Mixtape Unlock":          ItemData(0xF, ItemClassification.progression),
    "President Bird Unlock":         ItemData(0x10, ItemClassification.progression),
    "Snakedown Unlock":              ItemData(0x11, ItemClassification.progression),
    "Octeaparty Unlock":             ItemData(0x12, ItemClassification.progression),
    "Globe Trotters Unlock":         ItemData(0x13, ItemClassification.progression),
    "Fire Mixtape Unlock":           ItemData(0x14, ItemClassification.progression),
    "Symphony Cartridge":            ItemData(0x15, ItemClassification.progression),
    "Three-Legged Race Cartridge":   ItemData(0x16, ItemClassification.progression),
    "Blacksmith Cartridge":          ItemData(0x17, ItemClassification.progression),
    "Encore Cartridge":              ItemData(0x18, ItemClassification.progression),
    "Flipper Snapper Record":        ItemData(0x19, ItemClassification.progression),
    "Sweet Tooth Record":            ItemData(0x1A, ItemClassification.progression),
    "Rock, Paper, Showdown! Record": ItemData(0x1B, ItemClassification.progression),
    "Pantry Parade Record":          ItemData(0x1C, ItemClassification.progression),
    "Jungle Mixtape Record":         ItemData(0x1D, ItemClassification.progression),
    "B-Bot & the Fly Girls Record":  ItemData(0x1E, ItemClassification.progression),
    "Flow Worms Record":             ItemData(0x1F, ItemClassification.progression),
    "Meet & Tweet Record":           ItemData(0x20, ItemClassification.progression),
    "Steady Bears Record":           ItemData(0x21, ItemClassification.progression),
    "Sky Mixtape Record":            ItemData(0x22, ItemClassification.progression),
    "Pop Up Kitchen Record":         ItemData(0x23, ItemClassification.progression),
    "Firework Festival Record":      ItemData(0x24, ItemClassification.progression),
    "Hammer Time! Record":           ItemData(0x25, ItemClassification.progression),
    "Molecano Record":               ItemData(0x26, ItemClassification.progression),
    "Ocean Mixtape Record":          ItemData(0x27, ItemClassification.progression),
    "President Bird Record":         ItemData(0x28, ItemClassification.progression),
    "Snakedown Record":              ItemData(0x29, ItemClassification.progression),
    "Octeaparty Record":             ItemData(0x2A, ItemClassification.progression),
    "Globe Trotters Record":         ItemData(0x2B, ItemClassification.progression),
    "Fire Mixtape Record":           ItemData(0x2C, ItemClassification.progression),
    #Junk
    "Random Souvenir":               ItemData(0x100, ItemClassification.filler),
    "Random Video Tape":             ItemData(0x101, ItemClassification.filler),
}

bits_and_bops_item_name_groups = get_item_groups()

junk_weights = {
    "Random Souvenir":   10,
    "Random Video Tape": 10
}

trap_weights = {
}