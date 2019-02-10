### Messenger Pattern
Create Message Log
Populate Message Log via messenger pattern
All systems should return results.
>>> In the old game, I allowed the messenger pattern to run systems...

### Items
Start desinging soul numbers and stuff here.

### GUI
Display player stats, skills, and monster stats+skills
Create a message log here too.

### Saving
Python can do this easily?

### Character++
Skills and ranged attack systems get done here.

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