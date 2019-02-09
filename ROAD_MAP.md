### Monsters
Create monster generation code
> Generate dungeon
>>> Remember list of rooms
> Spawn the player in one room
> Spawn monsters in each other room

Create components/systems needed for AI entity
> AI component
>>> Decide to move toward the player, and send that to the move system
> Uses the move system to move


### Combat?
Collisions turn into combat here!
Revisit monster AI
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

### Numpy optmizations

```py
from typing import NamedTuple

class Tile(NamedTuple):
    blocks_sight: bool
    blocks_path: bool

tree = Tile(True, True)
```