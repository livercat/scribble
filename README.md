# scribble

Automation script for the Stone Story RPG.

Equips weapons, uses abilities, deals with bosses!
Also shows ability cooldowns and buff/debuff info.

Warning: this README and in the script itself contain a lot of spoilers and hidden game info, so don't read further if you don't want to be spoiled!

## Features

1. Efficient combat: chooses weapons based on enemy element and location, uses item abilities when appropriate, and intelligently handles boss mechanics.
1. Optional UI: shows your buffs/debuffs, ability cooldowns, and extended enemy info (disabled by default). All of these can be individually hidden.
1. Blazing fast: caches computations where possible, and uses efficient branching
to not slow your game down.
1. Aimed at players with moderate gear: 8-10* with +5 to +10 enchants, nothing fancy.
1. Supports advanced mechanics which are broadly applicable regardless of your gear level: double-screen smite, `ai.idle` AAC for 2-handed melee weapons,
debuffing bosses, helping with quests, and much more.
1. Stunlock bosses and minibosses where it makes sense.
1. Dodges all exploding enemies.
1. Supportes all items with activated abilities, including all Lost items.

## Non-goals and limitations

1. Doesn't support advanced AAC (one-handed weapons, frame-perfect cancelling, or HP tracking).
1. Not tested with high-level gear, which might have completely different playstyles and approaches.
1. Only tested on iOS version, but should work everywhere.

## Prerequisites

Finish main story to unlock the Mindstone

## How to use

Copy contents of `scribble.txt` into your Mindstone, and configure your weapons and playstyle settings at the top of the script.
Before you configure the settings, please read in-depth explanations below to understand what the script is trying to do .

If you encounter a bug, you can use the `scribble.debug.txt` instead, which has a lot of diagnostics and debug info on screen, and record video of the incorrect script behavior with that - it will immensely speed up the bugfixing.

## In-depth explanations

By default, the script prefers to use melee weapons, and only uses ranged for  scripted bosses, against specific enemies (like mosquitoes and wasps), and to debuff when you don't have melee debuffing weapons. However, there are multiple settings that can change this behavior. I will describe the default mode, and you can learn more about settings from the comments in the script itself.

The script uses only the weapons and abilities that you explicitly configure in settings, so it won't use a random 0* +1 dP weapon you've got from a chest.

### Regular enemies

What script considers when selecting a weapon:

- Match the foe's weak element.
- Use hammers or heavy hammer if the foe has armor.
- Use single-target or AoE weapons based on `foe.count`.
- If you're on low HP, use lifestealing weapons and healing shields.
- If it's a boss, or if you have the Smite buff, debuffs the enemy.
- Uses `A` shields when approaching the enemy to get the armor.

### Bosses

Script uses frame-perfect blocks and dodges almost everywhere. Since many attacks depend on the amount of chill stacks on the enemy, script tries to take it into account, but sometimes the chill falls off in the exact wrong moment, and the dodge/block fails.

#### Dysan

Scout: just kills.
Phase 1: shield-blocks small attacks.
Phase 2: uses appropriate element in the main-hand, debuffs with the off-hand, uses abilities only when safe. Last-hits with the Smite to get 1 stack of it for the next phase.
Phase 3: dodges stun and ray, switches weapons based on current boss resistance buff.

#### Xylo & Poena

Wasp nest: uses single-target ranged.
Xylo: dodges the root (or blocks if Mind is on CD).
Poena: either stunlocks if you have the weapons to do it, or respects the mirror to slowly chip away if you don't.

#### Bolesh

Ceiling decorator: stunlocks if possible.
Bolesh: nukes in melee until he gets a damage buff, then switches to ranged.

#### Mushrooms

Snail & Puff: kills and dodges respectively.
Phase 1: dodges big swing, shield-blocks pellets.
Phase 2: dodges the big swing.

#### Pallas

Big grave: uses ranged AoE
Phase 1: shield-blocks the sword.
Phase 2: uses magic damage to kill summoned Booos.

#### Bronze Guardian

Bomb: dodges
Guardian: uses ranged damage/debuffs when hammer is up, dodges the hit if you don't have enough armor to block, nukes in melee while the hammer is down.

#### Hrimnir

Ice elemental: stunlock if possible.
Hrimnir: shield-blocks snowballs (and uses fire talisman to reduce damage), uses unmaking weapons against the wall.

Help needed: this fight almost certainly can be improved, please let me know if you have ideas for strategies.

#### Nagaraja

Cultist: just kills
Naga: dodges all poison balls in white and blue levels, tries to do it in yellow, but sometimes fails. Tris to dodge the boulder if Mind is off CD.

Help needed: yellow levels can use better positioning and dashes to avoid all poison, please let me know if you have ideas for strategies.

## Development

Since the mobile version doesn't support external imports, and Mindstone has a limit of 40kb of code, there are several versions of the script:

- `scribble.txt` is the primary one for regular play.
- `scribble.debug.txt` has no comments in settings, but shows advanced script diagnostics to more easily debug problems.
- `scribble.dev.txt` is the most complete one, wich full code comments and readable code, but it doesn't fit in Mindstone and can't be used directly. I develop in that version, and automatically generate `scribble.txt` and `scribble.debug.txt` from it (using the `minimize.py` Python script).

I use VSCode with a [syntax highlighter](https://marketplace.visualstudio.com/items?itemName=Catalyst-42.c42-stonescript) for StoneScript. I also set `"editor.rulers": [48]` in settings to make it easier to respect Mindstone line limit of 48 characters.

If you also play on mobile, please don't use in-game UI to write your code! It's fine for small adjustments, but for writing actual logic it's very inconvenient. Use a mobile programming editor, or even basic text editor/notes app, it will make your life less painful.

To copy the script from the PC to mobile, I use an online notepad sharing site - there is a lot of them, with varying level of sketchinnes. I can't recommend any one in particular, use the one you like.

## Screenshot

![screenshot demonstrating custom UI](https://i.imgur.com/FbL3kJQ.jpg)
