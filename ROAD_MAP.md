### Main Loop
Basic stuff. Input > Update > Render.

### Character
Basic functionality for a movable player entity on screen.
> Create Entity class
>> Create components: Position, Base
>>> Base contains glyph, color, name

### Maps
Map generation happens here.

[Intent]: a basic dungeon. Rooms, corridors. Nothing special. BSP.

### FOV
libtcod handles this.

### Path Finding
Collision logic is done here

### Monsters
Zombie AI.
Monster generation within the dungeon.
A* pathing?

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