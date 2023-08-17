# scribble

Automation script for the Stone Story RPG.

Equips weapons, uses abilities, deals with bosses!
Also shows ability cooldowns and buff/debuff info.

Pull requests and bug reports are very welcome.

## Features

1. Efficient combat: chooses weapons based on enemy element and location, uses item abilities when appropriate, and handles boss mechanics.
1. Minimalistic UI: shows your buffs/debuffs, ability cooldowns, and enemy info (disabled by default). All of these can be disabled individually.
1. Blazing fast: uses early returns and branched ifs (:?) where possible. If you feel your game is noticeably slow with this script, please let me know by creating an issue!
1. Highly modular: most of the functionality is contained in descriptively named (and sometimes documented) functions, so you can reuse parts of this script for your own scripts.

## Prerequisites

Finish main story to unlock the Mindstone

## How to use

Copy contents of `scribble.txt` into your Mindstone and configure your weapons and runtime settings at the top

## Limitations

- Only tested on iOS version
- Mobile version doesn't support arbitrary `import`s, so all code is contained in a single file.
- Tested mostly on blue-level zones (6 to 10 stars) and a bit on white-levels (1-5) and very little in yellow (11+)
- Only the following Lost Items are supported (because I don't have the rest): `Skeleton Arm`, `Bashing Shield`, `Blade of the Fallen God`, `Cultist Mask`
- Doesn't do AAC for normal weapons, only for specials (heavy hammer, bardiche, skeleton arm). If you don't know what AAC is, don't worry about it :)
- Doesn't support potions besides Healing and Vampiric

## Development

I use VSCode with a [syntax highlighter](https://marketplace.visualstudio.com/items?itemName=Catalyst-42.c42-stonescript) for StoneScript. I also set `"editor.rulers": [49]` in settings to make it easier to respect Mindstone line limit of 49 characters - remember that you always can split a long line into several lines:
```
something
^like
^this
```
Some variable names are shorter than I would prefer for readability, but Mindstone has line limit of 49 chars (actually it might be 48, need to check).

I use a mix of function arguments and global variables for various pieces of logic. I would prefer not to use global vars at all 
to make it harder to miss something and easier to follow the logic, but since we don't have optional or default arguments,
functions would have very ugly signatures. So func argument are used for weapon switching where it's important to make sure everything
lines up correctly.

I also use a mix of conditional branching (:?) and early returns. Early returns reduce line lenght and make funcs more readable. They are neat!

Main logic is in following functions:
prelude() - collects info from game state
  into global vars
progress() - entry point for combat logic
  and boss handling
fight() - main logic for choosing range and
  fighting special non-boss enemies
melee(), ranged(), elemental() - equip
  appropriate weapons
draw_ui() - draws UI :)

If you also play on mobile, please don't use in-game UI to write your code! It's fine for small adjustments, but for writing actual logic it's very inconvenient. Use a mobile programming editor, or even basic text editor/notes app, it will make your life less painful.

## Notes on weapon naming

Each elemental weapon aside from staffs and warhammers has two variants: "D" or "dX",
where "X" is the elemental modifier ("A" and "ax" for shields). Staffs and warhammers instead have six!

"A", "D", "ax", "aX", "dx", "dX".

You can mutate between them using moondial.

Meaning of letters in suffix:
"A": get armor on egage for each foe
"D": attack bonus vs correct element
"x": on being hit, chance to: unmake (aether),
     fire dot, chill (ice), +attack (poison),
     heal (vigor)
"X": on attack, chance to: unmake (aether),
     fire dot, chill (ice), lifesteal (vigor),
     reduce foe attack (poison)

Full list of suffixes:
Defensive: staffs, warhammers, shields
  "au", "af", "ai", "ap", "ah", "A"
Offensive: staffs, warhammers, swords, xbows
  "dU", "dF", "dI", "dP", "dL", "D"
Exclusive to staffs and warhammers:
  "aU", "aF", "aI", "aP", "aL",
  "du", "df", "di", "dp", "dh"

Note that vigor has 2 different letters: "L" for offensive lifesteal and "h" for defensive "heal on being hit".
There are no "l" or "H" modifiers.

## Screenshot

![screenshot demonstrating custom UI](https://i.imgur.com/FbL3kJQ.jpg)
