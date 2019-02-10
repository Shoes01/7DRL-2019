### Combat?
Collisions turn into combat here!
Revisit monster AI
>>> Gets caught on things
Death function

### Items
Start desinging soul numbers and stuff here.

### GUI
Display player stats, skills, and monster stats+skills
Create a message log here too.

### Saving
Python can do this easily?

### Character++
Skills and ranged attack systems get done here.

### Mapgen++
Move map_gen code into a folder and split into appropriate pieces

### Render++
Move the Render code out of systems, into its own folder. Maybe.

### Numpy optmizations

```py
from typing import NamedTuple

class Tile(NamedTuple):
    blocks_sight: bool
    blocks_path: bool

tree = Tile(True, True)
```