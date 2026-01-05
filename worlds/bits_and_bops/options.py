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


class Required45RPMCompletions(Range):
    """
    The number of 45RPM completions required to unlock Final Mixtape
    """
    display_name = "Required 45RPM Completions"
    range_start = 0
    range_end = 20
    default = 0


class Required78RPMCompletions(Range):
    """
    The number of 78RPM completions required to unlock Final Mixtape
    """
    display_name = "Required 78RPM Completions"
    range_start = 0
    range_end = 20
    default = 0


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
        Required45RPMCompletions,
        Required78RPMCompletions,
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
    required_45_rpm_completions: Required45RPMCompletions
    required_78_rpm_completions: Required78RPMCompletions
    badgesanity: BadgeSanity
    allowed_badges: AllowedBadges
    death_link: DeathLink
