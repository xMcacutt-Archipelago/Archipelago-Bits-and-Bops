from __future__ import annotations
from worlds.bits_and_bops import *
from BaseClasses import MultiWorld, Region, Entrance
from typing import List, Dict

from worlds.bits_and_bops.locations import create_locations


class Ty1Region(Region):
    subregions: List[Region] = []


def connect_regions(world: BitsAndBopsWorld, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.multiworld.get_region(from_name, world.player)
    exit_region = world.multiworld.get_region(to_name, world.player)
    return entrance_region.connect(exit_region, entrance_name)


def create_region(world: BitsAndBopsWorld, name: str):
    reg = Region(name, world.player, world.multiworld)
    create_locations(world, reg)
    world.multiworld.regions.append(reg)

level_names = [
    "Flipper Snapper",
    "Sweet Tooth",
    "Rock, Paper, Showdown!",
    "Pantry Parade",
    "Jungle Mixtape",
    "B-Bot & the Fly Girls",
    "Flow Worms",
    "Meet & Tweet",
    "Steady Bears",
    "Sky Mixtape",
    "Pop Up Kitchen",
    "Firework Festival",
    "Hammer Time!",
    "Molecano",
    "Ocean Mixtape",
    "President Bird",
    "Snakedown",
    "Octeaparty",
    "Globe Trotters",
    "Fire Mixtape",
]

cartridge_names = [
    "Encore Cartridge",
    "Three-Legged Race Cartridge",
    "Blacksmith Cartridge",
    "Symphony Cartridge",
]

def create_regions(world: BitsAndBopsWorld):
    create_region(world, "Menu")
    for level_name in level_names:
        create_region(world, level_name)
        create_region(world, f"{level_name} - Record")
    for cartridge_name in cartridge_names:
        create_region(world, f"{cartridge_name}")


def connect_all_regions(world: BitsAndBopsWorld):
    for level_name in level_names:
        connect_regions(world, "Menu", level_name, f"Menu -> {level_name}")
        connect_regions(world, level_name, f"{level_name} - Record", f"Menu -> {level_name} - Record")

    for cartridge_name in cartridge_names:
        connect_regions(world, "Menu", cartridge_name, f"Menu -> {cartridge_name}")
