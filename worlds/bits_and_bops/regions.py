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
    world.regions.append(reg)


def create_regions(world: BitsAndBopsWorld):
    create_region(world, "Menu")
    create_region(world, "Example Region 1")
    create_region(world, "Example Region 2")
    create_region(world, "Example Region 3")


def connect_all_regions(world: BitsAndBopsWorld):
    connect_regions(world, "Menu","Example Region 1", "Menu -> Example Region 1")
    connect_regions(world, "Example Region 1","Example Region 2", "Example Region 1 -> Example Region 2")
    connect_regions(world, "Example Region 1","Example Region 3", "Example Region 1 -> Example Region 3")
