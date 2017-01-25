# TO DO LIST:
# Randomly generate house layout

import stealy3_rooms
import stealy3_functions
import stealy3_classes
import stealy3_items
import random

# Set up takes place below here!
room_list = [stealy3_rooms.kitchen]

stealy3_functions.generate_room(stealy3_rooms.lounge_room, room_list)
stealy3_functions.generate_room(stealy3_rooms.dining_room, room_list)
stealy3_functions.generate_room(stealy3_rooms.foyer, room_list)
stealy3_functions.generate_room(stealy3_rooms.music_room, room_list)
stealy3_functions.generate_room(stealy3_rooms.study, room_list)

# Making player
rand_room = room_list[random.randint(0, len(room_list)-1)]
player = stealy3_classes.Player("Jeff", rand_room)
turns = 0

# Making a Murderer
murderer = stealy3_classes.Player("Capt Murder", stealy3_rooms.waiting_room)
murderer.weapon = stealy3_items.mace

# Gameplay loop here!
print "..."
stealy3_functions.play(player, murderer, room_list)
