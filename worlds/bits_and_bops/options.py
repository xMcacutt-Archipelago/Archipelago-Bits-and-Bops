from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions, OptionSet


class Goal(Choice):
    """
    Determines the goal of the seed

    Final Mixtape: Complete the Final Mixtape
    """
    display_name = "Goal"
    option_goal1 = 0
    default = 0


class RequiredLevelCompletions(Range):
    """
    The number of total levels that need to be completed to unlock the Final Mixtape
    """
    display_name = "Required Level Completions"
    range_start = 4
    range_end = 16
    default = 9


class RequiredRank(Choice):
    """
    The rank required to receive a check on a level.

    Cool: Any passing rank will reward a check

    Amazing: Better than Cool, while still allowing a few misses

    Perfect: Requires perfection. WARNING: THIS WILL CAUSE CHECKS TO BE EXTREMELY DIFFICULT!
    """
    display_name = "Required Rank"
    cool = 0
    amazing = 1
    perfect = 2
    default = 1


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
        RequiredLevelCompletions,
        RequiredRank,
    ]),
    OptionGroup("Sanity Options", [
        BadgeSanity
    ]),
    OptionGroup("Traps", [
    ]),
    OptionGroup("Death Link", [
        DeathLink
    ]),
]


@dataclass
class BitsAndBopsOptions(PerGameCommonOptions):
    goal: Goal
    required_rank: RequiredRank
    required_level_completions: RequiredLevelCompletions
    badgesanity: BadgeSanity
    allowed_badges: AllowedBadges
    death_link: DeathLink
