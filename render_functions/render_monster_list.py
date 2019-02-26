import tcod as libtcod

from game import MONSTERS

def render_monster_list(consoles, entities, fov_map):
    console = consoles['monsters']
    console_root = consoles['root']

    # Reset console.
    console.clear()

    # Print to console.
    entities_in_render_order = sorted(entities, key=lambda x: x.base.render_order.value)
    entities_in_render_order.reverse()

    y = 1
    for entity in entities_in_render_order:
        if fov_map.fov[entity.pos.x, entity.pos.y] and entity.base.char is not '@':
            if entity.base.char is '%':
                string = entity.base.char + ' Corpse'    
            else:
                string = entity.base.char + ' ' + entity.base.name.capitalize()

            console.print(0, y, string, fg=entity.base.color, bg_blend=libtcod.BKGND_NONE)
            y += 1

    # Send to console.
    console.blit(console_root, MONSTERS.X, MONSTERS.Y, 0, 0, MONSTERS.W, MONSTERS.H - 1)