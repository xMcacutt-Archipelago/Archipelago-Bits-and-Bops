import copy
import typing
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, Location, LocationProgressType
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from .items import BitsAndBopsItem, bits_and_bops_item_table, create_items, ItemData
from .locations import bits_and_bops_location_table, BitsAndBopsLocation, badge_dict, rpm_16_level_dict, \
    rpm_45_level_dict, rpm_78_level_dict
from .options import BitsAndBopsOptions, bits_and_bops_option_groups
from .regions import create_regions, connect_regions, connect_all_regions
from .rules import set_rules, create_events

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
    options_dataclass = BitsAndBopsOptions
    options: BitsAndBopsOptions
    topology_present = True
    item_name_to_id = {name: item.code for name, item in bits_and_bops_item_table.items()}
    location_name_to_id = {name: item.code for name, item in bits_and_bops_location_table.items()}

    web = BitsAndBopsWeb()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.itempool = []
        self.excluded_locs: set[str] = set()

    def fill_slot_data(self) -> id:
        #from Utils import visualize_regions
        #state = self.multiworld.get_all_state(False)
        #state.update_reachable_regions(self.player)
        #visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml",
        #                  show_entrance_names=True, regions_to_highlight=state.reachable_regions[self.player])
        return {
            "ModVersion": "1.0.3",
            "Required Rank": self.options.required_rank.value,
            "Required Level Completions": self.options.required_level_completions.value,
            "Required 16RPM Completions": self.options.required_16_rpm_completions.value,
            "Required 45RPM Completions": self.options.required_45_rpm_completions.value,
            "Required 78RPM Completions": self.options.required_78_rpm_completions.value,
            "DeathLink": self.options.death_link.value,
        }

    def generate_early(self) -> None:
        valid_locations = 20
        required_locations = 20

        if self.options.required_16_rpm_completions.value > 0 or \
            self.options.required_45_rpm_completions.value > 0 or \
            self.options.required_78_rpm_completions.value > 0:
            required_locations += 20

        if self.options.badgesanity.value:
            required_locations += 4

        if self.options.required_16_rpm_completions.value > 0:
            valid_locations += 20
            for level_16rpm in self.options.excluded_16_rpm_levels.value:
                self.excluded_locs.add(level_16rpm)

        if self.options.required_45_rpm_completions.value > 0:
            valid_locations += 20
            for level_45rpm in self.options.excluded_45_rpm_levels.value:
                self.excluded_locs.add(level_45rpm)

        if self.options.required_78_rpm_completions.value > 0:
            valid_locations += 20
            for level_78rpm in self.options.excluded_78_rpm_levels.value:
                self.excluded_locs.add(level_78rpm)

        if self.options.badgesanity.value:
            valid_locations += 4
            for badge in self.options.excluded_badges.value:
                self.excluded_locs.add(badge)

        valid_locations -= len(self.excluded_locs)

        if valid_locations < required_locations:
            raise OptionError(f"[Bits & Bops - {self.multiworld.player_name[self.player]}] Too many locations excluded. Please adjust your yaml.")

        return

    def pre_fill(self) -> None:
        for item in self.multiworld.itempool:
            print(item.name)
        for item in self.multiworld.get_locations(self.player):
            print(item.name)

    def create_item(self, name: str) -> Item:
        item_info = bits_and_bops_item_table[name]
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

    def set_rules(self):
        create_events(self)
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
