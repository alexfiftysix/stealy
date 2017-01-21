from stealy3_classes import room
import stealy3_items

######################
## ROOM SET UP HERE ##
######################

kitchen = room(
name = 'Kitchen',
description = (
    "There is shattered glass on the ground from your forced entry."
    "\nA bench runs along the north and east walls of the room."
    "\nThere are doors to the North, East and West."
    ),
xypos = [1, 0],
inventory = [stealy3_items.knife, stealy3_items.mugs, stealy3_items.microwave]
)

lounge_room = room(
name ='Lounge room',
description = (
    "There is a couch on the west wall of the room."
    "\nThere is a door to the South, one to the East, and one to the West."
    ),
xypos = [1, 1],
inventory = [stealy3_items.tv, stealy3_items.art, stealy3_items.console]
)

dining_room = room(
name = 'Dining room',
description = (
    "A large table is in the centre of the room."
    "\nThe table is freshly laid with 6 places."
    "\nDoors lead to the East and North"
    ),
xypos = [0, 0],
inventory = [stealy3_items.plates, stealy3_items.cutlery, stealy3_items.placemats]
)

foyer = room(
name = "Foyer",
description = (
    "The front door is to the North, and doors lead to the South and East."
    ),
xypos = [0, 1],
inventory = [stealy3_items.umbrella, stealy3_items.hat]
)

study = room(
name = "Study",
description = (
    "There is a desk against the corner, under a window."
    "\nDoors lead to the West and South."
    ),
xypos = [2, 1],
inventory = [stealy3_items.laptop, stealy3_items.fancy_pen]
)

music_room = room(
name = "Music Room",
description = (
    "The music room has a baby-grand piano, recording equipment and a chandelier."
    "\nDoors lead to the North and West"
    ),
xypos = [2, 0],
inventory = [stealy3_items.guitar, stealy3_items.microphone, stealy3_items.synth]
)



# This room does not exist in game
# This is a place to store the murderer until he enters the game
waiting_room = room(
name = "Waiting Room",
description = "How are you seeing this?",
xypos = [-666, 666],
inventory = []
)

# This room does not exist in game
# This room is where the player escapes to when they escape the house
escape_room = room(
name = "Escape Room",
description = "How are you seeing this?",
xypos = [0, 2],
inventory = []
)
