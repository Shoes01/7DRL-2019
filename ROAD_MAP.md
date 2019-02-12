### GUI
Create a message log.
Color would be nice on the GUI.

### Items
Start desinging soul numbers and stuff here.
>> Update GUI here

### Saving
Python can do this easily?

### Character++
Skills and ranged attack systems get done here.
Get a list of "soul sized" "levels" for monsters. Race will determine base stats, soul will determine bonus stats.
Zombie :: Poor Soul   :: -1
Thrall :: Common Soul :: +0
...


### Systems++
Move map_gen code into a folder and split into appropriate pieces
Move the Render code out of systems, into its own folder. Maybe.
Move FOV code and Factory code out of systems.

### Numpy optmizations

```py
from typing import NamedTuple

class Tile(NamedTuple):
    blocks_sight: bool
    blocks_path: bool

tree = Tile(True, True)
```