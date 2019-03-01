## NEXT THING TO DO

Skills should have their own damage profile.

### POLISH
When selecting a skill, you should still be able to click the other buttons
>>> The targeting state needs to accept these inputs
When selecting a skill a second time, it should toggle it off
>>> Special code needs to be written for this..?
Better report the errors selecting a skill can produce.
>>> What about when there is no equipment?
>>> What about when there are no legal targets?
>>> What about when the direction chosen is not legal?
>>> Still on cooldown?

### 7DRL CHANGES

Remove inventory
Remove experience
Remove leveling up
Remove the associated keys
Change the behavior of num_5
>>> Write new code for this
Auto equip items
NEW STATE: Item comparison state
>>> Describe the item, provide a damage profile
>>> Show what the legal targeting area of the skill is
REWORK HUD 
>>> Remove LVL. 
>>> ItemDesc always the damage and defense profiles of items when a skill is not selected
>>> Show Soul Number
>>> Make entire root console wider... much wider...
>>>>>> Display monster rank and race. Notihng else
>>> Show enemy race and rank on screen
>>> Have some way of inspecting monsters...
Create new items
Create new monsters
Create algorithms for monster generation/distribution, and loot dropping
Create level progression
Improve monster AI
>>> Allow them to use skills

__MONSTER DESIGN__
Rank informs what slots have items equipped a monster has equipped
Race informs what items are equipped to those slots

:: Rank ::
Zombie: Main hand only
Husk: + torso
Thrull: + off hand
Adventurer: + boots
Hero: + ring
Champion 

[KOBOLD]
Main hand: Knife
Torso: Rags
Offhand: Dagger >> 
Feet: Sandals
Ring Finger: Stealth???
Belt: ???

[GOLBIN]
Main Hand: Sword
Torso: Cuirass
Offhand: Buckler
Feet: Boots


### GUI
Exit confirmation

### CONTENT - Loot

Create more lootable items
Expand the monster dropping loot logic

### CONTENT - Monsters
` Race and Soul mechanic `
The race of a unit will determine its baseline stat. Example: a rat has a baseline stat of 1. A goblin has a baseline stat of 5.
The soul of a unit will determine how the stat value determine ATK, DEF, etc.
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

Skills do not affect stats, but rather attack as a multiple of stats.
A sword slash may do 0.9xATK to the targeted tiles.
A fireball may do 1.1xMAG.
A staff may do 0.4xATK + 0.6xMAG

MainHand skills are offensive
OffHand skills are active defensive
Head skills are ... 
    debuff skills? (intimidation, confuse) 
    perception skills? (see through walls, detect all monsters on map)? 
    useless, choose a different slot? (amulet, left ring finger, )
RingFinger skills are indirect offensive
Torso skills are passive defensive
Feet skills are movement

Items are static. They grant the same skills all the time. A sword has a lunge attack, an axe a cleave attack. A great sword has a different skill. The Sword of Greatness has another skill.
Is this too much content to make?

### ITEMS++
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