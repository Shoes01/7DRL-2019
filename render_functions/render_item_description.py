import textwrap

from game import COLORS, LOG

def render_item_description(consoles, player):
    console = consoles['log']
    console_root = consoles['root']

    # This console is shared with the message log. Only render this if an item is selected.
    _selected_item = None
    for _, item in player.body.parts.items():
        if item and item.skill and item.skill.selected:
            _selected_item = item
    
    if _selected_item is None:
        return

    # Reset console.
    console.clear()

    # Print to console.    
    _item_name = _selected_item.base.name.capitalize()
    _skill_name = _selected_item.skill.name.capitalize()
    _skill_description_lines = textwrap.wrap(_selected_item.skill.description, LOG.W)

    console.print(0, 0, _item_name, fg=COLORS['hud_skill_description'])
    console.print(0, 1, _skill_name, fg=COLORS['hud_skill_description'])

    y = 0
    for line in _skill_description_lines:
        console.print(0, 3 + y, line, fg=COLORS['hud_skill_description'])
        y += 1

    # Sent to console.
    console.blit(console_root, LOG.X, LOG.Y, 0, 0, LOG.W, LOG.H)