import tcod as libtcod

from game import MESSAGE

def render_message_log(consoles, message_log):
    console_message_log = consoles['message_log']
    console_root = consoles['root']
    # Reset the console.
    console_message_log.default_bg = libtcod.black
    console_message_log.clear()

    # Print to the console.
    y = 1
    for message in message_log.messages:
        console_message_log.default_fg = message.color
        console_message_log.print_(0, y, message.text, libtcod.BKGND_NONE, libtcod.LEFT)
        y += 1

    # Send to console.
    console_message_log.blit(dest=console_root, dest_x=MESSAGE.X, dest_y=MESSAGE.Y, src_x=0, src_y=0, width=MESSAGE.W, height=MESSAGE.H)