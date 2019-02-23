### BUGS
The targeting logic may reach outside the game_map index

Using a skill does not end the player turn...

Gaining a level while in the Targeting State sends conflicing messages to the game.state manager
> I have used a skill, so it wants the state to be PLAYER_TURN
> I have gained a level, so it wants the state to be LEVEL_UP
>>> This will be fixed my using a FSM, or GSM

### GAME STATE MACHINE

[Player_Turn]   >>> is killed   >>> [Player_Dead]
                >>> attacks     >>> [Enemy_Turn]        >>> ai.take_turn()  >>> [Player_Turn]
                >>> opens inv   >>> [Open_Inveotry]     >>> close inv       >>> [Player_Turn]
                >>> levels up   >>> [Level_Up]          >>> chooses stat    >>> [Player_Turn]
                >>> uses skill  >>> [Targeting_State]   >>> chooses dir     >>> [Enemy_Turn] <bug>
<bug>: Because the GSM goes straight to enemy, there is no chance to level up. 
If the event queue were a persistent object, it would persist between updates.

The event queue is loaded with events.
The events are taken from the queue and fed to the state machine.
If the machine accepts the queue, the event is removed from the queue.
Otherwise, the event stays in.

Some events need to be pinged every tick, until they get resolved. They are persistent.
Example: Leveling up.


### GUI
Make the consoles look a little better
Have a menu at the start of the game? (maybe not for 7DRL)
>>> If so, look into saving the game
Clean up the "names" of the stats in the level up menu.

### CONTENT - Loot

Create more lootable items
Expand the monster dropping loot logic

### CONTENT - Monsters
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

[NAIVE_ECS]
Each system iterates over all entities every time. Systems don't talk to each other. They are fed components and change them. 
Systems are processed in a specific order, so that in one tick a multi-system action may be done.

Example

Note: the way I am using the "messenger" pattern now has only one flaw in reagrds to systems: I process the results after all the systems have been read.
Instead, the result of each system should be fed into the next relevant system.

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

### SKILLS++
Skills and ranged attack systems get done here.

> More offensive skills
> Skills that use a different nature
    > Indirect
> Skills that move the player
> Skills that buff defense

### ITEMS++
Start desinging soul numbers and stuff here.
>> Update GUI here

### AI++
Make use of the Dijkstra features of libtcod
> Need to generate a Dijkstra map.
> When that is made, I can use it to build a path using libtocd.path.Dijkstra()
Have the take_turn ai system check to see the kind of AI the entity has, and then ship all the needed info into the appropriate function.

### Numpy optmizations

```py
from typing import NamedTuple

class Tile(NamedTuple):
    blocks_sight: bool
    blocks_path: bool

tree = Tile(True, True)
```