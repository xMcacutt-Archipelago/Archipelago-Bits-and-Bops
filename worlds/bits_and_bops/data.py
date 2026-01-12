level_names = [
    "Flipper Snapper",
    "Sweet Tooth",
    "Rock, Paper, Showdown!",
    "Pantry Parade",
    "Jungle Mixtape",
    "B-Bot & the Fly Girls",
    "Flow Worms",
    "Meet & Tweet",
    "Steady Bears",
    "Sky Mixtape",
    "Pop Up Kitchen",
    "Firework Festival",
    "Hammer Time!",
    "Molecano",
    "Ocean Mixtape",
    "President Bird",
    "Snakedown",
    "Octeaparty",
    "Globe Trotters",
    "Fire Mixtape",
]

cartridge_names = [
    "Encore Cartridge",
    "Three-Legged Race Cartridge",
    "Blacksmith Cartridge",
    "Symphony Cartridge",
]

def has_records(world):
    return world.options.required_78_rpm_completions > 0 or \
        world.options.required_45_rpm_completions > 0 or \
        world.options.required_16_rpm_completions > 0