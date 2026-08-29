# How to Play this Manual
This manual is intended to be played on a freshly made character. Every technology is randomized as items in the multiworld, the only items you have access to are the first row of the technology tree.

If you are using Random Spawnpoint make sure the World is set to Multiplayer. If not, disregard this. After you've clicked on the initial location to receive either the Windswept Pass or the random spawn of choice, finish up the main quest until you receive the survival guide. Then you may click on emergency respawn.

You are only allowed to unlock a technology if you find it as an item first in the multiworld. Checks are tied to Capturing Pals, the Travel Points, Alphas, Bounties and Tower bosses by default. There are several yaml options to change them around.

If you wish to use the ingame randomizer for the pals, you should disabled the Palpedia as it will also disable any other logic requiring certain pals to be in certain locations.

A reference picture of Palpagos Isles from before 1.0 has been made by WeiLyra and have been added to this github named 'Palworld_Areas.png' where you can see all the areas that are locked behind an item of sorts.

## Island Passes
Each Island has an Island Pass which is required to have in your possession before you are allowed to go there. Each area can only be accessed adjacent to another accessible area. There are a few paths which allows someone with an eligble mount to reach certain areas at a further distance and allows them to take different paths throughout palpagos.

- **Windswept Pass** - Allows access to the whole Windswept Island.
- **Sea Breeze Pass** - Allows access to Sea Breeze Archipelago.
- **Bamboo Pass** - Allows access to the Bamboo Groves, the level 10-20 area in the middle of the map.
- **Silence Pass** - Allows Access to the Isle of Silence.
- **Murmurs Pass** - Allows Access to the Isle of Murmurs.
- **Sakurajima Pass** - Allows Access to Sakurajima.
- **Obsidian Pass** - Allows Access to Mount Obsidian, the volcanic island to the southwest.
- **Crescent Pass** - Allows Access to the Crescent Moon Shore area. Where you'll find the PAL Alliance Tower.
- **Verdant Pass** - Allows Access to the huge foresty island to the east. Which is called Verdant Brook.
- **Desiccated Pass** - Allows access to the Dessicated Dunes area, the massive Desert Region.
- **Marsh Pass** - Allows Access to Marsh Island.
- **Eastern Wild Pass** - Allows access to Eastern Wild Island.
- **Astral Pass** - Allows Access to the Astral Mountains.
- **Feybreak Pass** - Allows Access to Feybreak.
- **Sunreach Pass** - Allows Access to Sunreach.

The World Tree requires you to complete Panthalus' Main Mission and it will require 'Echoing Flute' to be found as an item in the Multiworld and you need access to the bones' locations.

If you are using Random Spawns you will begin with a "Spawn Item" such as "Windswept Spawn", these items are like the Passes, and is letting the logic know where you start off at! If you start with the Windswept Spawn, the Windswept Pass will no longer be in the item pool as they serve the same purpose for travel purposes.

And then there are just a bunch of small islands which each have their own pass such as:
- **Frostbitten Pass**
- **Eternal Summer Pass**
- **Sunlit Pass**
- **Decayed Pass**
- **Phantom Pass**
- **Oasis Pass**
- **Glacial Core Pass**
- **Suncrest Pass**
- **Sandstone Pass**
- **Glacial Memento Pass**
- **Bicornis Pass**
- **Scouring Pass**
- **Circular Ruins Pass**
- **Flamepulse Pass**

## Tower Key Spheres
The Key Spheres you usually receive from defeating each boss is instead required to access them. Those being:
- **Key Sphere of Envy** - Zoe - Rayne Syndicate Tower
- **Key Sphere of Pride** - Lily - Pal Alliance Tower
- **Key Sphere of Sloth** - Alex - Brotherhood of the Eternal Pyre Tower
- **Key Sphere of Greed** - Marcus - PIDF Tower
- **Key Sphere of Gluttony** - Victor - Pal Genetics Lab Tower
- **Key Sphere of Lust** - Saya - Moonflower Tower
- **Key Sphere of Wrath** - Bjorn - Feybreak Tower
- **Key Sphere of Original Sin** - Auri - Azure Covenant Tower

For Zenara in the world tree, you require the three items the Main Mission tasks you with to access it. The Dandilord's Petal, Silvance's Plume and the Modified Pal's Contaminated Core.

## Wildlife Sanctuaries
Each Wildlife Sanctuary requires a 'Tracker' for it to be in logic. Those are:
- Wildlife Sanctuary 1 Tracker
- Wildlife Sanctuary 2 Tracker
- Wildlife Sanctuary 3 Tracker

## Level Cap
There is a  level cap in place for the Manual, you can either choose it to be restricted by defeating Tower Bosses or by Regions in the yaml.

This level cap prevents certain bosses and wild pals from being in logic too early as well as checking when you can craft specific items.

You can disable the level cap for Technology or completely.

### To increase the Region Level Cap you require:
- **Level 1-10** - Requires Nothing.
- **Level 11-20** - Requires Access to Crescent Moon Shore and be able to craft Cloth Armor.
- **Level 21-30** - Requires Access to Mount Obsidian and be able to craft Pelt Armor.
- **Level 31-40** - Requires Access to Desiccated Dunes and be able to craft Metal Armor and (Heat or Cold) Resistant Armor.
- **Level 41-50** - Requires Access to Astral Mountains and be able to craft Refined Metal Armor.
- **Level 51-55** - Requires Access to Sakurajima and be able to craft Pal Metal Armor.
- **Level 56-60** - Requires Access to Feybreak and be able to craft Plasteel Armor.
- **Level 61-70** - Requires Access to Sunreach and be able to craft Hexolite Armor.
- **Level 71-80** - Requires Access to The World Tree and be able to craft Ancient Armor.

### To Increase the Tower Level Cap you require:
- **Level 1-10** - Requires Nothing.
- **Level 11-20** - Requires You to defeat Zoe and able to craft Cloth Armor.
- **Level 21-30** - Requires You to defeat Lily and able to craft Pelt Armor.
- **Level 31-40** - Requires You to defeat Alex and able to craft Metal Armor.
- **Level 41-50** - Requires You to defeat Marcus and able to craft Refined Metal Armor.
- **Level 51-55** - Requires You to defeat Victor and able to craft Pal Metal Armor.
- **Level 56-60** - Requires You to defeat Saya and able to craft Plasteel Armor.
- **Level 61-70** - Requires You to defeat Bjorn and able to craft Hexolite Armor.
- **Level 71-80** - Requires You to defeat Auri and able to craft Ancient Armor.

## Other Roadblocks
You require the Pal Gear Workbench and a Mount you can ride on before Feybreak is in logic, even if you have access to Mount Obsidian and possess the Feybreak pass.
There are other paths that require mounts to use, such as the Frostbitten Isle which can also only be reached with a mount.

Any other requirements are completely optional within the yaml. It is up to you how wish to play the manual!