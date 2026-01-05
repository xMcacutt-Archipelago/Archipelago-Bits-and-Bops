from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.BitsAndBops import BitsAndBopsWorld

from BaseClasses import CollectionState


def has_condition(world, state: CollectionState):
    return state.has("Example Item", world.player)


def get_rules(world):
    rules = {
        "locations": {
            "Example Location Dict 1":
                lambda state:
                    state.can_reach_region("Example Region 1", world.player)
                    or has_condition(world, state),
        },
        "entrances": {
            "Menu -> Example Region 1":
                lambda state:
                    state.has("Example Item", world.player, 2)
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

    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError:
            pass

    world.create_event("Victory Region", "Victory")
    world.get_location("Victory").access_rule = lambda state: False
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
