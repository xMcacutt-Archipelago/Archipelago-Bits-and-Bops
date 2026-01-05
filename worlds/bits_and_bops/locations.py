from __future__ import annotations
from enum import EnumType, Enum
from typing import TYPE_CHECKING, NamedTuple, Any
from BaseClasses import Location, Region
from BaseClasses import Location, Region, LocationProgressType

from worlds.bits_and_bops import *


class BitsAndBopsLocation(Location):
    game: str = "Bits & Bops"


class LocData:
    def __init__(self, code: int, region: str, progress_type: LocationProgressType = LocationProgressType.DEFAULT):
        """
        Represents a location with associated conditions.

        :param code: A unique identifier for the location.
        :param region: Name of the containing region.
        """
        self.code = code
        self.region = region
        self.progress_type = progress_type


def create_location(player: int, reg: Region, name: str, code: int, progress_type: LocationProgressType = LocationProgressType.DEFAULT):
    location = BitsAndBopsLocation(player, name, code, reg)
    location.progress_type = progress_type
    reg.locations.append(location)


def create_locations_from_dict(loc_dict, reg, player):
    for (key, data) in loc_dict.items():
        if data.region != reg.name:
            continue
        create_location(player, reg, key, data.code, data.progress_type)


def create_locations(world: BitsAndBopsWorld, reg: Region):
    # Levels
    create_locations_from_dict(levels_dict, reg, world.player)
    # Example 2
    create_locations_from_dict(example_location_dict2, reg, world.player)
    # Badges
    if world.options.badgesanity.value:
        create_locations_from_dict(badge_dict, reg, world.player)


levels_dict = {
    # Levels
    "Flipper Snapper":
        LocData(0x100, "Flipper Snapper"),
    "Flipper Snapper - 16RPM":
        LocData(0x101, "Flipper Snapper - Record"),
    "Flipper Snapper - 45RPM":
        LocData(0x102, "Flipper Snapper - Record"),
    "Flipper Snapper - 78RPM":
        LocData(0x103, "Flipper Snapper - Record"),
    "Sweet Tooth":
        LocData(0x104, "Sweet Tooth"),
    "Sweet Tooth - 16RPM":
        LocData(0x105, "Sweet Tooth - Record"),
    "Sweet Tooth - 45RPM":
        LocData(0x106, "Sweet Tooth - Record"),
    "Sweet Tooth - 78RPM":
        LocData(0x107, "Sweet Tooth - Record"),
    "Rock, Paper, Showdown!":
        LocData(0x108, "Rock, Paper, Showdown!"),
    "Rock, Paper, Showdown! - 16RPM":
        LocData(0x109, "Rock, Paper, Showdown! - Record"),
    "Rock, Paper, Showdown! - 45RPM":
        LocData(0x10A, "Rock, Paper, Showdown! - Record"),
    "Rock, Paper, Showdown! - 78RPM":
        LocData(0x10B, "Rock, Paper, Showdown! - Record"),
    "Pantry Parade":
        LocData(0x10C, "Pantry Parade"),
    "Pantry Parade - 16RPM":
        LocData(0x10D, "Pantry Parade - Record"),
    "Pantry Parade - 45RPM":
        LocData(0x10E, "Pantry Parade - Record"),
    "Pantry Parade - 78RPM":
        LocData(0x10F, "Pantry Parade - Record"),
    "Jungle Mixtape":
        LocData(0x110, "Jungle Mixtape"),
    "Jungle Mixtape - 16RPM":
        LocData(0x111, "Jungle Mixtape - Record"),
    "Jungle Mixtape - 45RPM":
        LocData(0x112, "Jungle Mixtape - Record"),
    "Jungle Mixtape - 78RPM":
        LocData(0x113, "Jungle Mixtape - Record"),
    "B-Bot & the Fly Girls":
        LocData(0x114, "B-Bot & the Fly Girls"),
    "B-Bot & the Fly Girls - 16RPM":
        LocData(0x115, "B-Bot & the Fly Girls - Record"),
    "B-Bot & the Fly Girls - 45RPM":
        LocData(0x116, "B-Bot & the Fly Girls - Record"),
    "B-Bot & the Fly Girls - 78RPM":
        LocData(0x117, "B-Bot & the Fly Girls - Record"),
    "Flow Worms":
        LocData(0x118, "Flow Worms"),
    "Flow Worms - 16RPM":
        LocData(0x119, "Flow Worms - Record"),
    "Flow Worms - 45RPM":
        LocData(0x11A, "Flow Worms - Record"),
    "Flow Worms - 78RPM":
        LocData(0x11B, "Flow Worms - Record"),
    "Meet & Tweet":
        LocData(0x11C, "Meet & Tweet"),
    "Meet & Tweet - 16RPM":
        LocData(0x11D, "Meet & Tweet - Record"),
    "Meet & Tweet - 45RPM":
        LocData(0x11E, "Meet & Tweet - Record"),
    "Meet & Tweet - 78RPM":
        LocData(0x11F, "Meet & Tweet - Record"),
    "Steady Bears":
        LocData(0x120, "Steady Bears"),
    "Steady Bears - 16RPM":
        LocData(0x121, "Steady Bears - Record"),
    "Steady Bears - 45RPM":
        LocData(0x122, "Steady Bears - Record"),
    "Steady Bears - 78RPM":
        LocData(0x123, "Steady Bears - Record"),
    "Sky Mixtape":
        LocData(0x124, "Sky Mixtape"),
    "Sky Mixtape - 16RPM":
        LocData(0x125, "Sky Mixtape - Record"),
    "Sky Mixtape - 45RPM":
        LocData(0x126, "Sky Mixtape - Record"),
    "Sky Mixtape - 78RPM":
        LocData(0x127, "Sky Mixtape - Record"),
    "Pop Up Kitchen":
        LocData(0x128, "Pop Up Kitchen"),
    "Pop Up Kitchen - 16RPM":
        LocData(0x129, "Pop Up Kitchen - Record"),
    "Pop Up Kitchen - 45RPM":
        LocData(0x12A, "Pop Up Kitchen - Record"),
    "Pop Up Kitchen - 78RPM":
        LocData(0x12B, "Pop Up Kitchen - Record"),
    "Firework Festival":
        LocData(0x12C, "Firework Festival"),
    "Firework Festival - 16RPM":
        LocData(0x12D, "Firework Festival - Record"),
    "Firework Festival - 45RPM":
        LocData(0x12E, "Firework Festival - Record"),
    "Firework Festival - 78RPM":
        LocData(0x12F, "Firework Festival - Record"),
    "Hammer Time!":
        LocData(0x130, "Hammer Time!"),
    "Hammer Time! - 16RPM":
        LocData(0x131, "Hammer Time! - Record"),
    "Hammer Time! - 45RPM":
        LocData(0x132, "Hammer Time! - Record"),
    "Hammer Time! - 78RPM":
        LocData(0x133, "Hammer Time! - Record"),
    "Molecano":
        LocData(0x134, "Molecano"),
    "Molecano - 16RPM":
        LocData(0x135, "Molecano - Record"),
    "Molecano - 45RPM":
        LocData(0x136, "Molecano - Record"),
    "Molecano - 78RPM":
        LocData(0x137, "Molecano - Record"),
    "Ocean Mixtape":
        LocData(0x138, "Ocean Mixtape"),
    "Ocean Mixtape - 16RPM":
        LocData(0x139, "Ocean Mixtape - Record"),
    "Ocean Mixtape - 45RPM":
        LocData(0x13A, "Ocean Mixtape - Record"),
    "Ocean Mixtape - 78RPM":
        LocData(0x13B, "Ocean Mixtape - Record"),
    "President Bird":
        LocData(0x13C, "President Bird"),
    "President Bird - 16RPM":
        LocData(0x13D, "President Bird - Record"),
    "President Bird - 45RPM":
        LocData(0x13E, "President Bird - Record"),
    "President Bird - 78RPM":
        LocData(0x13F, "President Bird - Record"),
    "Snakedown":
        LocData(0x140, "Snakedown"),
    "Snakedown - 16RPM":
        LocData(0x141, "Snakedown - Record"),
    "Snakedown - 45RPM":
        LocData(0x142, "Snakedown - Record"),
    "Snakedown - 78RPM":
        LocData(0x143, "Snakedown - Record"),
    "Octeaparty":
        LocData(0x144, "Octeaparty"),
    "Octeaparty - 16RPM":
        LocData(0x145, "Octeaparty - Record"),
    "Octeaparty - 45RPM":
        LocData(0x146, "Octeaparty - Record"),
    "Octeaparty - 78RPM":
        LocData(0x147, "Octeaparty - Record"),
    "Globe Trotters":
        LocData(0x148, "Globe Trotters"),
    "Globe Trotters - 16RPM":
        LocData(0x149, "Globe Trotters - Record"),
    "Globe Trotters - 45RPM":
        LocData(0x14A, "Globe Trotters - Record"),
    "Globe Trotters - 78RPM":
        LocData(0x14B, "Globe Trotters - Record"),
    "Fire Mixtape":
        LocData(0x14C, "Fire Mixtape"),
    "Fire Mixtape - 16RPM":
        LocData(0x14D, "Fire Mixtape - Record"),
    "Fire Mixtape - 45RPM":
        LocData(0x14E, "Fire Mixtape - Record"),
    "Fire Mixtape - 78RPM":
        LocData(0x14F, "Fire Mixtape - Record"),
}


example_location_dict2 = {
    # description
    "Example Location Dict 2":
        LocData(0x200, "Example Region"),
}


badge_dict = {
    # Badges
    "Explorer Badge":
        LocData(0x300, "Jungle Mixtape"),
    "Aviator Badge":
        LocData(0x301, "Sky Mixtape"),
    "Diver Badge":
        LocData(0x302, "Ocean Mixtape"),
    "Firefighter Badge":
        LocData(0x303, "Fire Mixtape"),
    "Bravo! Badge":
        LocData(0x304, "Encore Cartridge"),
    "Marathoner Badge":
        LocData(0x305, "Three-Legged Race Cartridge"),
    "Smithy Badge":
        LocData(0x306, "Blacksmith Cartridge"),
    "Maestro Badge":
        LocData(0x307, "Symphony Cartridge"),
    "Timekeeper Badge":
        LocData(0x308, "Clock"),
    "Completely Cool Badge":
        LocData(0x309, "All Levels"),
    "Altogether Amazing Badge":
        LocData(0x30A, "All Levels"),
    "Purely Perfect Badge":
        LocData(0x30B, "All Levels"),
    "Get Help Badge":
        LocData(0x30C, "Help Desk"),
    "Scratch the Itch Badge":
        LocData(0x30D, "Record Player"),
    "Technical Difficulties Badge":
        LocData(0x30E, "Computer"),
    "Troublemaker Badge":
        LocData(0x30F, "Any Level")
}


bits_and_bops_location_table = {
    **levels_dict,
    **example_location_dict2,
    **badge_dict,
}
