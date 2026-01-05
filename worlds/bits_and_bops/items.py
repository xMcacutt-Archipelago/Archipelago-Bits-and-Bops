from __future__ import annotations
from typing import Dict, Optional, TYPE_CHECKING
from worlds.bits_and_bops import *
from typing import Dict, Optional
from BaseClasses import Item, ItemClassification, MultiWorld, Location


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
    total_location_count: int = len(world.get_unfilled_locations(world.player))

    # Generic
    create_multiple("Example Item", 2, world, ItemClassification.useful)

    # Junk
    remaining_locations: int = total_location_count - len(world.worlds[world.player].itempool)
    trap_count: int = round(remaining_locations * options.trap_fill_percentage / 100)
    junk_count: int = remaining_locations - trap_count
    junk = get_random_item_names(world.random, junk_count, junk_weights)
    for name in junk:
        create_single(name, world)
    traps = get_random_item_names(world.random, trap_count, trap_weights)
    for name in traps:
        create_single(name, world)
    world.multiworld.itempool += world.itempool


def place_locked_items(world: MultiWorld, player: int):
    classification = ItemClassification.progression_skip_balancing
    example_loc: Location = world.get_location("Example Location", player)
    example_item: BitsAndBopsItem = BitsAndBopsItem("Example Item", classification, 0xFF, player)
    example_loc.place_locked_item(example_item)


class ItemData:
    def __init__(self, code: Optional[int], classification: Optional[ItemClassification]):
        self.code = code
        self.classification = classification


bits_and_bops_item_table: Dict[str, ItemData] = {
    "Flipper Snapper": ItemData(0x1, ItemClassification.progression),
    "Sweet Tooth": ItemData(0x2, ItemClassification.progression),
    "Rock, Paper, Showdown!": ItemData(0x3, ItemClassification.progression),
    "Pantry Parade": ItemData(0x4, ItemClassification.progression),
    "Jungle Mixtape": ItemData(0x5, ItemClassification.progression),
    "B-Bot & the Fly Girls": ItemData(0x6, ItemClassification.progression),
    "Flow Worms": ItemData(0x7, ItemClassification.progression),
    "Meet & Tweet": ItemData(0x8, ItemClassification.progression),
    "Steady Bears": ItemData(0x9, ItemClassification.progression),
    "Sky Mixtape": ItemData(0xA, ItemClassification.progression),
    "Pop Up Kitchen": ItemData(0xB, ItemClassification.progression),
    "Firework Festival": ItemData(0xC, ItemClassification.progression),
    "Hammer Time!": ItemData(0xD, ItemClassification.progression),
    "Molecano": ItemData(0xE, ItemClassification.progression),
    "Ocean Mixtape": ItemData(0xF, ItemClassification.progression),
    "President Bird": ItemData(0x10, ItemClassification.progression),
    "Snakedown": ItemData(0x11, ItemClassification.progression),
    "Octeaparty": ItemData(0x12, ItemClassification.progression),
    "Globe Trotters": ItemData(0x13, ItemClassification.progression),
    "Fire Mixtape": ItemData(0x14, ItemClassification.progression),
    "Symphony Cartridge": ItemData(0x15, ItemClassification.progression),
    "Three-Legged Race Cartridge": ItemData(0x16, ItemClassification.progression),
    "Blacksmith Cartridge": ItemData(0x17, ItemClassification.progression),
    "Encore Cartridge": ItemData(0x18, ItemClassification.progression),
    "Random Souvenir": ItemData(0x19, ItemClassification.filler),
}


junk_weights = {
    "Random Souvenir": 10
}

trap_weights = {
}