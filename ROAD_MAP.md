### Equipment

Move the body subcomponent to its own component
> Name it something else?
Create an equipment component
Attach a skill to an equipment
Create a few basic items
Monsters drop loot
Show items on the HUD.
There needs a stats system in order to fetch base_attack from stats comp and bonus_attack from item comp

### GUI
Make the consoles look a little better
Have a menu at the start of the game? (maybe not for 7DRL)
>>> If so, look into saving the game
Clean up the "names" of the stats in the level up menu.

### Monsters++
` Race and Soul mechanic `
The race of a unit will determine its baseline stat. Example: a rat has a baseline stat of 1. A goblin has a baseline stat of 5.
The soul of a unit will determine how the stat value determine ATT, DEF, etc.
The eccentricity of a soul will determine how far apart numbers can be in the soul.
* Stats can be negative, but will be treated as 0?
The rank of the soul will determine its net worth. (Example: a rare sould would have a sum of +5) 
* The rank of the soul is a prefix to the unit race. A Goblin Zombie is 5+0, whereas a Goblin Hero is 5+5. 

` Soul ranks `
-2 :: Zombie
-1 :: Thrull
 0 :: no name
+1 :: Adventurer
+5 :: Hero
+7 :: Champion
+9 :: Legend

### Systems++
Move map_gen code into a folder and split into appropriate pieces
Move Factory code out of systems.

According to ECS, systems should be run in a specific order, every tick. 
Don't know if I want to do that...

Example

[InputSystem]
Write the Input to the InputComponents of entities that have one but don't have an AIComponent. (Should only be the player.) Example: {'move': (+1, 0)}
[AIInputSystem]
Write the Input to the InputComponents of entitiesthat have one _and_ have an AIComponent.
[MovementSystem]
Read the InputComponent.
Write the new position of the PositionComponent of the entity.
[CollisionSystem]
Read the PositionComponent of the entity. Read the Map?.
Write collision, if there are any. Does the PositionComponent have a rewind?

### Skill System
Skills and ranged attack systems get done here.

### Items++
Start desinging soul numbers and stuff here.
>> Update GUI here

### AI++
Have the take_turn ai system check to see the kind of AI the entity has, and then ship all the needed info into the appropriate function.

### Numpy optmizations

```py
from typing import NamedTuple

class Tile(NamedTuple):
    blocks_sight: bool
    blocks_path: bool

tree = Tile(True, True)
```