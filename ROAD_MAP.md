# Bugs

There is a bug where the place_player() function will fail.
1) Maybe because the range of random integer is too great? would be 0 to len() - 1?
2) Maybe the map fails to generate, and I should gen again.

## MENU

___ Menu RENDERING ___
<rendering_only>
Given the action (or the state), fetch the required info.
> The outline of a menu is drawn
> The title of the menu is drawn
> The contents of the menu are drawn
>>> Contents are generated on the fly. For the case of the player inventory, the render code would need to know the player inventory.
>>> When the contents are generated, the index letter is also prepended.
>>> Check to see if an item is <act>'d, and if so alter how it is rendered.

<reminder> Don't over generalize. Get a working inventory. Then if I want to add more stuff (character sheet, main menu), I can tweak the Menu class.

___ Inventory System ___
Allow the user to select an item
When selected, allow a user to <act> on the item. 
> First action will be to drop the item.

[Decoupling]
The Menu system has two parts: interaction, and rendering.
The rendering code should have nothing to do with input.
The menu system would flag an item as chosen, and then the rendering system would know to color it.

## Inventory
>>> Need to create a Menu class that stores all the info that can be passed to the render function
[x] Pressing i opens the inventory
>>> Restructure the inventory system to be a generic menu system
[ ] List the items with an index
[ ] Pressing the item letter selects the item.    
[ ] Selected items may be dropped, equipped, or other.

### Items and Inventory
Create a few basic items
Create an inventory allowing to store items
> Create a show inventory state
> Create pickup/drop commands
Create an interface to equip items
> Done via inventory
Confer bonuses according to equipped items
Show items on the HUD.
Killing monsters should spawn items

### Organization++
The Game object holds the game-state. It should also hold a previous game state. Perhaps, changing game states automatically sets the previous state.
Rename the Inventory console to menu
> It will be used by more than one menu
>>> Perhaps make a generic menu console?

### GUI
Make the consoles look a little better
Have a menu at the start of the game?
>>> If so, look into saving the game

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
Move the Render code out of systems, into its own folder. Maybe.
Move FOV code and Factory code out of systems.

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