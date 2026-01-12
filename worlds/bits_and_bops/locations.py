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


def create_locations_from_dict(world, loc_dict, reg, player):
    for (key, data) in loc_dict.items():
        if data.region != reg.name:
            continue
        progress_type = LocationProgressType.EXCLUDED if key in world.excluded_locs else LocationProgressType.DEFAULT
        create_location(player, reg, key, data.code, progress_type)


def create_locations(world: BitsAndBopsWorld, reg: Region):
    # Levels
    create_locations_from_dict(world, levels_dict, reg, world.player)
    # Badges
    if world.options.badgesanity.value:
        create_locations_from_dict(world, badge_dict, reg, world.player)
    # 16RPM
    if world.options.required_16_rpm_completions.value > 0:
        create_locations_from_dict(world, rpm_16_level_dict, reg, world.player)
    # 45RPM
    if world.options.required_45_rpm_completions.value > 0:
        create_locations_from_dict(world, rpm_45_level_dict, reg, world.player)
    # 78RPM
    if world.options.required_78_rpm_completions.value > 0:
        create_locations_from_dict(world, rpm_78_level_dict, reg, world.player)

levels_dict = {
    # Levels
    "Flipper Snapper":
        LocData(0x100, "Flipper Snapper"),
    "Sweet Tooth":
        LocData(0x104, "Sweet Tooth"),
    "Rock, Paper, Showdown!":
        LocData(0x108, "Rock, Paper, Showdown!"),
    "Pantry Parade":
        LocData(0x10C, "Pantry Parade"),
    "Jungle Mixtape":
        LocData(0x110, "Jungle Mixtape"),
    "B-Bot & the Fly Girls":
        LocData(0x114, "B-Bot & the Fly Girls"),
    "Flow Worms":
        LocData(0x118, "Flow Worms"),
    "Meet & Tweet":
        LocData(0x11C, "Meet & Tweet"),
    "Steady Bears":
        LocData(0x120, "Steady Bears"),
    "Sky Mixtape":
        LocData(0x124, "Sky Mixtape"),
    "Pop Up Kitchen":
        LocData(0x128, "Pop Up Kitchen"),
    "Firework Festival":
        LocData(0x12C, "Firework Festival"),
    "Hammer Time!":
        LocData(0x130, "Hammer Time!"),
    "Molecano":
        LocData(0x134, "Molecano"),
    "Ocean Mixtape":
        LocData(0x138, "Ocean Mixtape"),
    "President Bird":
        LocData(0x13C, "President Bird"),
    "Snakedown":
        LocData(0x140, "Snakedown"),
    "Octeaparty":
        LocData(0x144, "Octeaparty"),
    "Globe Trotters":
        LocData(0x148, "Globe Trotters"),
    "Fire Mixtape":
        LocData(0x14C, "Fire Mixtape"),
}

rpm_16_level_dict = {
    "Flipper Snapper - 16RPM":
        LocData(0x101, "Flipper Snapper - Record"),
    "Sweet Tooth - 16RPM":
        LocData(0x105, "Sweet Tooth - Record"),
    "Rock, Paper, Showdown! - 16RPM":
        LocData(0x109, "Rock, Paper, Showdown! - Record"),
    "Pantry Parade - 16RPM":
        LocData(0x10D, "Pantry Parade - Record"),
    "Jungle Mixtape - 16RPM":
        LocData(0x111, "Jungle Mixtape - Record"),
    "B-Bot & the Fly Girls - 16RPM":
        LocData(0x115, "B-Bot & the Fly Girls - Record"),
     "Flow Worms - 16RPM":
         LocData(0x119, "Flow Worms - Record"),
    "Meet & Tweet - 16RPM":
        LocData(0x11D, "Meet & Tweet - Record"),
    "Steady Bears - 16RPM":
        LocData(0x121, "Steady Bears - Record"),
    "Sky Mixtape - 16RPM":
        LocData(0x125, "Sky Mixtape - Record"),
    "Pop Up Kitchen - 16RPM":
        LocData(0x129, "Pop Up Kitchen - Record"),
    "Firework Festival - 16RPM":
        LocData(0x12D, "Firework Festival - Record"),
    "Hammer Time! - 16RPM":
        LocData(0x131, "Hammer Time! - Record"),
    "Molecano - 16RPM":
        LocData(0x135, "Molecano - Record"),
    "Ocean Mixtape - 16RPM":
        LocData(0x139, "Ocean Mixtape - Record"),
    "President Bird - 16RPM":
        LocData(0x13D, "President Bird - Record"),
    "Snakedown - 16RPM":
        LocData(0x141, "Snakedown - Record"),
    "Octeaparty - 16RPM":
        LocData(0x145, "Octeaparty - Record"),
    "Globe Trotters - 16RPM":
        LocData(0x149, "Globe Trotters - Record"),
    "Fire Mixtape - 16RPM":
        LocData(0x14D, "Fire Mixtape - Record"),
}

rpm_45_level_dict = {
    "Flipper Snapper - 45RPM":
            LocData(0x102, "Flipper Snapper - Record"),
    "Sweet Tooth - 45RPM":
        LocData(0x106, "Sweet Tooth - Record"),
    "Rock, Paper, Showdown! - 45RPM":
        LocData(0x10A, "Rock, Paper, Showdown! - Record"),
    "Pantry Parade - 45RPM":
        LocData(0x10E, "Pantry Parade - Record"),
    "Jungle Mixtape - 45RPM":
        LocData(0x112, "Jungle Mixtape - Record"),
    "B-Bot & the Fly Girls - 45RPM":
        LocData(0x116, "B-Bot & the Fly Girls - Record"),
    "Flow Worms - 45RPM":
        LocData(0x11A, "Flow Worms - Record"),
    "Meet & Tweet - 45RPM":
        LocData(0x11E, "Meet & Tweet - Record"),
    "Steady Bears - 45RPM":
        LocData(0x122, "Steady Bears - Record"),
    "Sky Mixtape - 45RPM":
        LocData(0x126, "Sky Mixtape - Record"),
    "Pop Up Kitchen - 45RPM":
        LocData(0x12A, "Pop Up Kitchen - Record"),
    "Firework Festival - 45RPM":
        LocData(0x12E, "Firework Festival - Record"),
    "Hammer Time! - 45RPM":
        LocData(0x132, "Hammer Time! - Record"),
    "Molecano - 45RPM":
        LocData(0x136, "Molecano - Record"),
    "Ocean Mixtape - 45RPM":
        LocData(0x13A, "Ocean Mixtape - Record"),
    "President Bird - 45RPM":
        LocData(0x13E, "President Bird - Record"),
    "Snakedown - 45RPM":
        LocData(0x142, "Snakedown - Record"),
    "Octeaparty - 45RPM":
        LocData(0x146, "Octeaparty - Record"),
    "Globe Trotters - 45RPM":
        LocData(0x14A, "Globe Trotters - Record"),
    "Fire Mixtape - 45RPM":
        LocData(0x14E, "Fire Mixtape - Record"),
}

rpm_78_level_dict = {
    "Flipper Snapper - 78RPM":
            LocData(0x103, "Flipper Snapper - Record"),
    "Sweet Tooth - 78RPM":
        LocData(0x107, "Sweet Tooth - Record"),
    "Rock, Paper, Showdown! - 78RPM":
        LocData(0x10B, "Rock, Paper, Showdown! - Record"),
    "Pantry Parade - 78RPM":
        LocData(0x10F, "Pantry Parade - Record"),
    "Jungle Mixtape - 78RPM":
        LocData(0x113, "Jungle Mixtape - Record"),
    "B-Bot & the Fly Girls - 78RPM":
        LocData(0x117, "B-Bot & the Fly Girls - Record"),
    "Flow Worms - 78RPM":
        LocData(0x11B, "Flow Worms - Record"),
    "Meet & Tweet - 78RPM":
        LocData(0x11F, "Meet & Tweet - Record"),
    "Steady Bears - 78RPM":
        LocData(0x123, "Steady Bears - Record"),
    "Sky Mixtape - 78RPM":
        LocData(0x127, "Sky Mixtape - Record"),
    "Pop Up Kitchen - 78RPM":
        LocData(0x12B, "Pop Up Kitchen - Record"),
    "Firework Festival - 78RPM":
        LocData(0x12F, "Firework Festival - Record"),
    "Hammer Time! - 78RPM":
        LocData(0x133, "Hammer Time! - Record"),
    "Molecano - 78RPM":
        LocData(0x137, "Molecano - Record"),
    "Ocean Mixtape - 78RPM":
        LocData(0x13B, "Ocean Mixtape - Record"),
    "President Bird - 78RPM":
        LocData(0x13F, "President Bird - Record"),
    "Snakedown - 78RPM":
        LocData(0x143, "Snakedown - Record"),
    "Octeaparty - 78RPM":
        LocData(0x147, "Octeaparty - Record"),
    "Globe Trotters - 78RPM":
        LocData(0x14B, "Globe Trotters - Record"),
    "Fire Mixtape - 78RPM":
        LocData(0x14F, "Fire Mixtape - Record"),
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
        LocData(0x308, "Menu"),
    "Completely Cool Badge":
        LocData(0x309, "Menu"),
    "Altogether Amazing Badge":
        LocData(0x30A, "Menu"),
    "Purely Perfect Badge":
        LocData(0x30B, "Menu"),
    "Get Help Badge":
        LocData(0x30C, "Menu"),
    "Scratch the Itch Badge":
        LocData(0x30D, "Menu"),
    "Technical Difficulties Badge":
        LocData(0x30E, "Menu"),
    "Troublemaker Badge":
        LocData(0x30F, "Menu")
}


bits_and_bops_location_table = {
    **levels_dict,
    **badge_dict,
    **rpm_16_level_dict,
    **rpm_45_level_dict,
    **rpm_78_level_dict,
}
