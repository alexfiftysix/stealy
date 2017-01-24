# TO DO LIST:
#

import stealy3_rooms
import stealy3_functions
import stealy3_classes
import stealy3_items
# Set up takes place below here!

# Room list is required for room movement functions
room_list = [stealy3_rooms.kitchen, stealy3_rooms.lounge_room,
             stealy3_rooms.dining_room, stealy3_rooms.foyer,
             stealy3_rooms.escape_room, stealy3_rooms.study,
             stealy3_rooms.music_room]

# Making player
player = stealy3_classes.Player("Jeff", stealy3_rooms.kitchen)
turns = 0


# Making a Murderer
murderer = stealy3_classes.Player("Capt Murder", stealy3_rooms.waiting_room)
murderer.weapon = stealy3_items.mace

# Gameplay loop here!
stealy3_functions.play(player, murderer, room_list)
