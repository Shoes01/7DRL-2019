### 7DRL 2019 ###

[GOALS]

__Goal 1__
Controls are hyper-streamlined.

Controls:
    Numpad: movement
    num_5: wait, or interact with item
    qweads: activate skill

    esc: exit

All other information is on the HUD.

<what about damage?> Killing enemies returns HP. Killing many per turn grants more HP? Revenge kills grant more HP? <lore> When a soul leaves a body, you absorb some of that ... energy ...

__Goal 1.1__
No inventory.

Picking up an item prompts the player to swap if one is already equipped.

###################

Pressing SPACE triggers the "interact" action.

If there is an item on the ground, equip it
    If there is already an item equipped in that slot, compare the items
        Press 9 for SWAP, 3 for DON'T SWAP

If there is nothing on the ground, pass turn.

>>> The ITEMDESC panel should say what "5" does. Rename to the INTERACTION panel.


###################

__Goal 2__
Soul number mechanic.

__Goal 2.1__
Stats are derived in unique way.

A Soul Number is a 2x3 matrix of numbers.
The class of a unit informs how the soul number is used to affect the stats.
A racial bonus is a flat number applied to all stats.
HP always has a multiplier on it.

__Goal 2.2__
The play may consume the souls of the fallen to increase their own power.

The play may rotate or flip the soul before consuming it, thus choosing how it affects the numbers.

__Goal 3__
Skills are interesting.
Enemies use the skills too???

Gameplay has the player taking on huge numbers of lowly creatures, and a few heroic opponents.