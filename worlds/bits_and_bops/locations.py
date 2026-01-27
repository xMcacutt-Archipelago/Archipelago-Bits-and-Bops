from __future__ import annotations

from dataclasses import dataclass
from enum import EnumType, Enum
from typing import TYPE_CHECKING, NamedTuple, Any
from BaseClasses import Location, Region
from BaseClasses import Location, Region, LocationProgressType

from worlds.bits_and_bops.data import *
from worlds.bits_and_bops import *


class BitsAndBopsLocation(Location):
    game: str = "Bits & Bops"


@dataclass(frozen=True)
class LocData:
    code: int
    region: str
    progress_type: LocationProgressType = LocationProgressType.DEFAULT


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
    create_locations_from_dict(world, rpm_33_level_dict, reg, world.player)
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


rpm_16_level_dict = { }
rpm_33_level_dict = { }
rpm_45_level_dict = { }
rpm_78_level_dict = { }


def generate_level_dicts():
    for i, level_name in enumerate(level_names):
        rpm_16_level_dict[f"{level_name} - 16RPM"] = LocData(0x101 + i * 4, f"{level_name} - Record")
        rpm_33_level_dict[f"{level_name}"] = LocData(0x100 + i * 4, f"{level_name}")
        rpm_45_level_dict[f"{level_name} - 45RPM"] = LocData(0x102 + i * 4, f"{level_name} - Record")
        rpm_78_level_dict[f"{level_name} - 78RPM"] = LocData(0x103 + i * 4, f"{level_name} - Record")


generate_level_dicts()


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
    **rpm_33_level_dict,
    **badge_dict,
    **rpm_16_level_dict,
    **rpm_45_level_dict,
    **rpm_78_level_dict,
}
