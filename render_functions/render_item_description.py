import textwrap

from game import COLORS, ITEMDESC

def render_item_description(consoles, player):
    console = consoles['item_description']
    console_root = consoles['root']

    # Reset console.
    console.clear()

    # Print to console.
    _selected_item = player
    for item in player.inv.contents:
        if item and item.skill and item.skill.selected:
            _selected_item = item
    
            _item_name = _selected_item.base.name.capitalize()
            _skill_name = _selected_item.skill.name.capitalize()
            _skill_description_lines = textwrap.wrap(_selected_item.skill.description, ITEMDESC.W)

            console.print(0, 0, _item_name, fg=COLORS['hud_skill_description'])
            console.print(0, 1, _skill_name, fg=COLORS['hud_skill_description'])

            y = 0
            for line in _skill_description_lines:
                console.print(0, 3 + y, line, fg=COLORS['hud_skill_description'])
                y += 1

    # Sent to console.
    console.blit(console_root, ITEMDESC.X, ITEMDESC.Y, 0, 0, ITEMDESC.W, ITEMDESC.H)