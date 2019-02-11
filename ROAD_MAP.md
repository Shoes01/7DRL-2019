### Items
Start desinging soul numbers and stuff here.

### GUI
Create a message log here.

` To organize the GUI, I should have many consoles. `
Root console: 80 x 60. Already made in engine.py
Map console: 80 x 50. Displays the "game".
Panel console: 80 x 10. Displays the HUD.

` The render function should render each console separately `


Display player stats, skills, and monster stats+skills

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