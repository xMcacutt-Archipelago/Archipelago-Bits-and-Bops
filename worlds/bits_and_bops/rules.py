from __future__ import annotations
from typing import TYPE_CHECKING
from .regions import level_names, cartridge_names
if TYPE_CHECKING:
    from worlds.bits_and_bops import BitsAndBopsWorld

from .data import *
from BaseClasses import CollectionState

def has_level(world, state: CollectionState, level: str):
    return state.has(f"{level} Unlock", world.player)

def has_record(world, state: CollectionState, level: str):
    return state.has(f"{level} Record", world.player)

def has_cartridge(world, state: CollectionState, cartridge: str):
    return state.has(f"{cartridge}", world.player)


def get_rules(world):
    rules = {
        "locations": {
            "Completely Cool Badge":
                lambda state: state.has("Level Complete", world.player, 20),
            "Altogether Amazing Badge":
                lambda state: state.has("Level Complete", world.player, 20),
            "Purely Perfect Badge":
                lambda state: state.has("Level Complete", world.player, 20),

        },
        "entrances": {
        }
    }
    return rules


def set_rules(world):
    from . import BitsAndBopsWorld
    world: BitsAndBopsWorld
    rules_lookup = get_rules(world)
    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError:
            pass

    for level_name in level_names:
        world.get_entrance(f"Menu -> {level_name}").access_rule = lambda state, level = level_name: has_level(world, state, level)

    if has_records(world):
        for level_name in level_names:
            world.get_entrance(f"Menu -> {level_name} - Record").access_rule = lambda state, level = level_name: has_record(world, state, level)

    if world.options.badgesanity:
        for cartridge_name in cartridge_names:
            world.get_entrance(f"Menu -> {cartridge_name}").access_rule = lambda state, cartridge = cartridge_name: has_cartridge(world, state, cartridge)

    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError:
            pass

    world.get_location("Final Mixtape").access_rule = lambda state:\
        state.has("Level Complete", world.player, world.options.required_level_completions.value)\
        and state.has("16 RPM Record Complete", world.player, world.options.required_16_rpm_completions.value)\
        and state.has("45 RPM Record Complete", world.player, world.options.required_45_rpm_completions.value)\
        and state.has("78 RPM Record Complete", world.player, world.options.required_78_rpm_completions.value)
    world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location("Final Mixtape", world.player)