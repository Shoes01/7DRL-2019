### Items
Start desinging soul numbers and stuff here.
>> Update GUI here

### Saving
Python can do this easily?

### Monsters++
` Race and Soul mechanic `
The race of a unit will determine its baseline stat. Example: a rat has a baseline stat of 1. A goblin has a baseline stat of 5.
The soul of a unit will determine how the stat value determine ATT, DEF, etc.
The eccentricity of a soul will determine how far apart numbers can be in the soul.
* Stats can be negative, but will be treated as 0?
The rank of the soul will determine its net worth. (Example: a rare sould would have a sum of +5) 
* The rank of the soul is a prefix to the unit race. A Goblin Zombie is 5+0, whereas a Goblin Hero is 5+5. 

` Soul ranks `
Zombie
Thrull

Adventurer

Hero
Demigod
God

### Systems++
Move map_gen code into a folder and split into appropriate pieces
Move the Render code out of systems, into its own folder. Maybe.
Move FOV code and Factory code out of systems.

### Skill System
Skills and ranged attack systems get done here.

### Numpy optmizations

```py
from typing import NamedTuple

class Tile(NamedTuple):
    blocks_sight: bool
    blocks_path: bool

tree = Tile(True, True)
```