import tcod as libtcod

from game import LOG

def render_message_log(consoles, message_log):
    console = consoles['log']
    console_root = consoles['root']
    # Reset the console.
    console.clear()

    # Print to the console.
    y = 1
    for message in message_log.messages:
        console.print(1, y, message.text, fg=message.color, bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
        y += 1

    # Send to console.
    # console.clear(ch=5, fg=libtcod.green, bg=libtcod.green) # DEBUG code.
    console.blit(dest=console_root, dest_x=LOG.X, dest_y=LOG.Y, src_x=0, src_y=0, width=LOG.W, height=LOG.H)