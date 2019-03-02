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

Entities have their char determined by their race
Their color determined by their "soul rank" (zombie, etc)
Have their class determined by ...

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