import copy
import typing
from typing import *
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, Location, LocationProgressType
from Options import OptionError, Accessibility
from worlds.AutoWorld import WebWorld, World
from .items import BitsAndBopsItem, bits_and_bops_item_table, create_items, ItemData, get_random_item_names, \
    junk_weights, bits_and_bops_item_name_groups, generate_item_table
from .locations import bits_and_bops_location_table, BitsAndBopsLocation, badge_dict, rpm_16_level_dict, \
    rpm_45_level_dict, rpm_78_level_dict
from .options import BitsAndBopsOptions, bits_and_bops_option_groups
from .regions import create_regions, connect_regions, connect_all_regions
from .data import *
from .rules import set_rules


class BitsAndBopsWeb(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Bits & Bops randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["xMcacutt", "Dashieswag92"]
    )

    tutorials = [setup_en]
    option_groups = bits_and_bops_option_groups

class BitsAndBopsWorld(World):
    """
    Bits & Bops is a collection of original rhythm mini-games!
    Filled with catchy music, snappy gameplay and gorgeous, hand-drawn animation,
    Bits & Bops is sure to brighten your day.
    """
    game = "Bits & Bops"
    bab_world_version = "v1.0.4"
    options_dataclass = BitsAndBopsOptions
    options: BitsAndBopsOptions
    topology_present = True
    item_name_to_id = {name: item.code for name, item in bits_and_bops_item_table.items()}
    location_name_to_id = {name: item.code for name, item in bits_and_bops_location_table.items()}
    item_name_groups = bits_and_bops_item_name_groups

    web = BitsAndBopsWeb()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.item_table = copy.deepcopy(bits_and_bops_item_table)
        self.itempool = []
        self.excluded_locs: set[str] = set()

    def fill_slot_data(self) -> id:
        #from Utils import visualize_regions
        #state = self.multiworld.get_all_state(False)
        #state.update_reachable_regions(self.player)
        #visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml",
        #   show_entrance_names=True, regions_to_highlight=state.reachable_regions[self.player])
        return {
            "ModVersion": "1.0.4",
            "Required Rank": self.options.required_rank.value,
            "Required Level Completions": self.options.required_level_completions.value,
            "Required 16RPM Completions": self.options.required_16_rpm_completions.value,
            "Required 45RPM Completions": self.options.required_45_rpm_completions.value,
            "Required 78RPM Completions": self.options.required_78_rpm_completions.value,
            "DeathLink": self.options.death_link.value,
        }

    def handle_ut_yamless(self, slot_data: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        if not slot_data \
                and hasattr(self.multiworld, "re_gen_passthrough") \
                and isinstance(self.multiworld.re_gen_passthrough, dict) \
                and self.game in self.multiworld.re_gen_passthrough:
            slot_data = self.multiworld.re_gen_passthrough[self.game]
        if not slot_data:
            return None
        self.options.required_rank.value = slot_data["Required Rank"]
        self.options.required_level_completions.value = slot_data["Required Level Completions"]
        self.options.required_16_rpm_completions.value = slot_data["Required 16RPM Completions"]
        self.options.required_45_rpm_completions.value = slot_data["Required 45RPM Completions"]
        self.options.required_78_rpm_completions.value = slot_data["Required 78RPM Completions"]
        return slot_data

    def get_filler_item_name(self) -> str:
        return get_random_item_names(self.random, 1, junk_weights)[0]

    def generate_early(self) -> None:
        self.handle_ut_yamless(None)

        if self.options.accessibility == Accessibility.option_minimal:
            raise OptionError(f"[Bits & Bops - {self.multiworld.player_name[self.player]}] Accessibility minimal is not supported for Bits & Bops please use full accesibility in your yaml.")

        valid_locations = 20
        required_locations = 20

        if has_records(self):
            required_locations += 20

        if self.options.badgesanity.value:
            required_locations += 4

        if self.options.required_16_rpm_completions.value > 0:
            valid_locations += 20
            if self.options.required_16_rpm_completions > (20 - len(self.options.excluded_16_rpm_levels.value)):
                raise OptionError(f"[Bits & Bops - {self.multiworld.player_name[self.player]}] Excluded more 16RPM levels than required to goal.")
            for level_16rpm in self.options.excluded_16_rpm_levels.value:
                print(f"Excluded: {level_16rpm}")
                self.excluded_locs.add(level_16rpm)

        if self.options.required_45_rpm_completions.value > 0:
            valid_locations += 20
            if self.options.required_16_rpm_completions > (20 - len(self.options.excluded_45_rpm_levels.value)):
                raise OptionError(f"[Bits & Bops - {self.multiworld.player_name[self.player]}] Excluded more 45RPM levels than required to goal.")
            for level_45rpm in self.options.excluded_45_rpm_levels.value:
                print(f"Excluded: {level_45rpm}")
                self.excluded_locs.add(level_45rpm)

        if self.options.required_78_rpm_completions.value > 0:
            valid_locations += 20
            if self.options.required_78_rpm_completions > (20 - len(self.options.excluded_78_rpm_levels.value)):
                raise OptionError(f"[Bits & Bops - {self.multiworld.player_name[self.player]}] Excluded more 78RPM levels than required to goal.")
            for level_78rpm in self.options.excluded_78_rpm_levels.value:
                print(f"Excluded: {level_78rpm}")
                self.excluded_locs.add(level_78rpm)

        if self.options.badgesanity.value:
            valid_locations += 16
            for badge in self.options.excluded_badges.value:
                print(f"Excluded: {badge}")
                self.excluded_locs.add(badge)

        valid_locations -= len(self.excluded_locs)

        print(f"Valid: {valid_locations} Required: {required_locations}")
        if valid_locations < required_locations:
            raise OptionError(f"[Bits & Bops - {self.multiworld.player_name[self.player]}] Too many locations excluded. Valid: {valid_locations} Required: {required_locations}. Please adjust your yaml.")

        return

    def generate_basic(self):
        prog_items = []
        non_excluded_locs = []
        for item in self.itempool:
            if item.classification is ItemClassification.progression:
                prog_items.append(item.name)
        for loc in self.multiworld.get_locations(self.player):
            if loc.progress_type is not LocationProgressType.EXCLUDED:
                non_excluded_locs.append(loc.name)
        print(f"{len(prog_items)}, {len(non_excluded_locs)}")

    def create_item(self, name: str) -> Item:
        item_info = self.item_table[name]
        return BitsAndBopsItem(name, item_info.classification, item_info.code, self.player)

    def create_items(self):
        create_items(self)

    def create_event(self, region_name: str, event_loc_name: str, event_item_name: str) -> None:
        region: Region = self.multiworld.get_region(region_name, self.player)
        loc: BitsAndBopsLocation = BitsAndBopsLocation(self.player, event_loc_name, None, region)
        loc.place_locked_item(BitsAndBopsItem(event_item_name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)

    def create_regions(self):
        create_regions(self)
        connect_all_regions(self)
        for level_name in level_names:
            self.create_event(level_name, f"{level_name} Complete", "Level Complete")
            if self.options.required_16_rpm_completions.value > 0 and f"{level_name} - 16RPM" not in self.excluded_locs:
                self.create_event(level_name, f"{level_name} 16 RPM Record Complete", "16 RPM Record Complete")
            if self.options.required_45_rpm_completions.value > 0 and f"{level_name} - 45RPM" not in self.excluded_locs:
                self.create_event(level_name, f"{level_name} 45 RPM Record Complete", "45 RPM Record Complete")
            if self.options.required_78_rpm_completions.value > 0 and f"{level_name} - 78RPM" not in self.excluded_locs:
                self.create_event(level_name, f"{level_name} 78 RPM Record Complete", "78 RPM Record Complete")
        self.create_event("Menu", "Final Mixtape", "Final Mixtape")

    def set_rules(self):
        set_rules(self)

    def extend_hint_information(self, hint_data: typing.Dict[int, typing.Dict[int, str]]):
        new_hint_data = {}

        for key, data in bits_and_bops_location_table.items():
            try:
                location: Location = self.multiworld.get_location(key, self.player)
            except KeyError:
                continue

            # new_hint_data[location.address] = f""

        hint_data[self.player] = new_hint_data
