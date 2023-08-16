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

If you also play on mobile, please don't use in-game UI to write your code! It's fine for small adjustments, but for writing actual logic it's very inconvenient. Use a mobile programming editor, or even basic text editor/notes app, it will make your life less painful.

## Screenshot

![screenshot demonstrating custom UI](https://i.imgur.com/FbL3kJQ.jpg)
