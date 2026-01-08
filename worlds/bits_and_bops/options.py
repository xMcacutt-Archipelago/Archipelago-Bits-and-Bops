from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions, OptionSet


class Goal(Choice):
    """
    Determines the goal of the seed

    Final Mixtape: Complete the Final Mixtape
    """
    display_name = "Goal"
    option_goal = 0
    default = 0

class RequiredRank(Choice):
    """
    The rank required to receive a check on a level.

    Cool: Any passing rank will reward a check

    Amazing: Better than Cool, while still allowing a few misses

    Perfect: Requires perfection. WARNING: THIS WILL CAUSE CHECKS TO BE EXTREMELY DIFFICULT!
    """
    display_name = "Required Rank"
    option_cool = 0
    option_amazing = 1
    option_perfect = 2
    default = 1


class RequiredLevelCompletions(Range):
    """
    The number of total levels that need to be completed to unlock the Final Mixtape
    """
    display_name = "Required Level Completions"
    range_start = 1
    range_end = 20
    default = 10


class Required16RPMCompletions(Range):
    """
    The number of 16RPM completions required to unlock Final Mixtape
    """
    display_name = "Required 16RPM Completions"
    range_start = 0
    range_end = 20
    default = 0


class Excluded16RPMLevels(OptionSet):
    """
    Choose which 78 RPM levels should not have required items
    """
    display_name = "Allowed 16RPM Levels"
    valid_keys = [
    "Flipper Snapper - 16RPM",
    "Sweet Tooth - 16RPM",
    "Rock, Paper, Showdown! - 16RPM",
    "Pantry Parade - 16RPM",
    "Jungle Mixtape - 16RPM",
    "B-Bot & the Fly Girls - 16RPM",
    "Flow Worms - 16RPM",
    "Meet & Tweet - 16RPM",
    "Steady Bears - 16RPM",
    "Sky Mixtape - 16RPM",
    "Pop Up Kitchen - 16RPM",
    "Firework Festival - 16RPM",
    "Hammer Time! - 16RPM",
    "Molecano - 16RPM",
    "Ocean Mixtape - 16RPM",
    "President Bird - 16RPM",
    "Snakedown - 16RPM",
    "Octeaparty - 16RPM",
    "Globe Trotters - 16RPM",
    "Fire Mixtape - 16RPM",
    ]
    default = []


class Required45RPMCompletions(Range):
    """
    The number of 45RPM completions required to unlock Final Mixtape
    """
    display_name = "Required 45RPM Completions"
    range_start = 0
    range_end = 20
    default = 0


class Excluded45RPMLevels(OptionSet):
    """
    Choose which 78 RPM levels should not have required items
    """
    display_name = "Allowed 45RPM Levels"
    valid_keys = [
    "Flipper Snapper - 45RPM",
    "Sweet Tooth - 45RPM",
    "Rock, Paper, Showdown! - 45RPM",
    "Pantry Parade - 45RPM",
    "Jungle Mixtape - 45RPM",
    "B-Bot & the Fly Girls - 45RPM",
    "Flow Worms - 45RPM",
    "Meet & Tweet - 45RPM",
    "Steady Bears - 45RPM",
    "Sky Mixtape - 45RPM",
    "Pop Up Kitchen - 45RPM",
    "Firework Festival - 45RPM",
    "Hammer Time! - 45RPM",
    "Molecano - 45RPM",
    "Ocean Mixtape - 45RPM",
    "President Bird - 45RPM",
    "Snakedown - 45RPM",
    "Octeaparty - 45RPM",
    "Globe Trotters - 45RPM",
    "Fire Mixtape - 45RPM",
    ]
    default = []


class Required78RPMCompletions(Range):
    """
    The number of 78RPM completions required to unlock Final Mixtape
    """
    display_name = "Required 78RPM Completions"
    range_start = 0
    range_end = 20
    default = 0


class Excluded78RPMLevels(OptionSet):
    """
    Choose which 78 RPM levels should not have required items
    """
    display_name = "Excluded 78RPM Levels"
    valid_keys = [
    "Flipper Snapper - 78RPM - 78RPM",
    "Sweet Tooth - 78RPM",
    "Rock, Paper, Showdown! - 78RPM",
    "Pantry Parade - 78RPM",
    "Jungle Mixtape - 78RPM",
    "B-Bot & the Fly Girls - 78RPM",
    "Flow Worms - 78RPM",
    "Meet & Tweet - 78RPM",
    "Steady Bears - 78RPM",
    "Sky Mixtape - 78RPM",
    "Pop Up Kitchen - 78RPM",
    "Firework Festival - 78RPM",
    "Hammer Time! - 78RPM",
    "Molecano - 78RPM",
    "Ocean Mixtape - 78RPM",
    "President Bird - 78RPM",
    "Snakedown - 78RPM",
    "Octeaparty - 78RPM",
    "Globe Trotters - 78RPM",
    "Fire Mixtape - 78RPM",
    ]
    default = [
    "Pantry Parade - 78RPM",
    "Flow Worms - 78RPM",
    "Steady Bears - 78RPM",
    "Sky Mixtape - 78RPM",
    "Snakedown - 78RPM",
    "Globe Trotters - 78RPM",
    "Fire Mixtape - 78RPM",
    ]


class BadgeSanity(Toggle):
    """
    Determines whether badges provide a check when collected (some more difficult badges will be de-prioritized).
    """
    display_name = "Badgesanity"


class AllowedBadges(OptionSet):
    """
    Sets which badges will be allowed to potentially have progression items
    """
    display_name = "Allowed Badges"
    valid_keys = [
        "Explorer Badge",
        "Aviator Badge",
        "Diver Badge",
        "Firefighter Badge",
        "Bravo! Badge",
        "Marathoner Badge",
        "Smithy Badge",
        "Maestro Badge",
        "Timekeeper Badge",
        "Completely Cool Badge",
        "Altogether Amazing Badge",
        "Purely Perfect Badge",
        "Get Help Badge",
        "Scratch the Itch Badge",
        "Technical Difficulties Badge",
        "Troublemaker Badge",
    ]
    default = [
        "Explorer Badge",
        "Aviator Badge",
        "Diver Badge",
        "Firefighter Badge",
        "Marathoner Badge",
        "Smithy Badge",
        "Get Help Badge",
        "Scratch the Itch Badge",
        "Technical Difficulties Badge",
        "Troublemaker Badge",
    ]

bits_and_bops_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
    ]),
    OptionGroup("Logic Options", [
        RequiredRank,
        RequiredLevelCompletions,
        Required16RPMCompletions,
        Excluded16RPMLevels,
        Required45RPMCompletions,
        Excluded45RPMLevels,
        Required78RPMCompletions,
        Excluded78RPMLevels,
    ]),
    OptionGroup("Sanity Options", [
        BadgeSanity,
        AllowedBadges,
    ]),
    #OptionGroup("Traps", [
    #]),
    OptionGroup("Death Link", [
        DeathLink
    ]),
]


@dataclass
class BitsAndBopsOptions(PerGameCommonOptions):
    goal: Goal
    required_rank: RequiredRank
    required_level_completions: RequiredLevelCompletions
    required_16_rpm_completions: Required16RPMCompletions
    excluded_16_rpm_levels: Excluded16RPMLevels
    required_45_rpm_completions: Required45RPMCompletions
    allowed_45_rpm_levels: Excluded45RPMLevels
    required_78_rpm_completions: Required78RPMCompletions
    excluded_78_rpm_levels: Excluded78RPMLevels
    badgesanity: BadgeSanity
    allowed_badges: AllowedBadges
    death_link: DeathLink
