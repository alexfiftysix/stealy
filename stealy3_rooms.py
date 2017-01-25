from stealy3_classes import Room
import stealy3_items
import random

######################
#  ROOM SET UP HERE  #
######################

kitchen = Room(
    name='Kitchen',
    description=(
        "There is shattered glass on the ground from your forced entry."
        "\nA bench runs along the north and east walls of the room."
    ),
    xypos=[5, 5],
    inventory=[stealy3_items.knife, stealy3_items.mugs, stealy3_items.microwave]
)

lounge_room = Room(
    name='Lounge room',
    description=(
        "There is a couch on the west wall of the room."
        ),
    xypos=[],
    inventory=[stealy3_items.tv, stealy3_items.art, stealy3_items.console]
)

dining_room = Room(
    name='Dining room',
    description=(
        "A large table is in the centre of the room."
        "\nThe table is freshly laid with 6 places."
        ),
    xypos=[],
    inventory=[stealy3_items.plates, stealy3_items.cutlery, stealy3_items.placemats]
)

foyer = Room(
    name="Foyer",
    description=(
        "The front door is to the North."
        ),
    xypos=[],
    inventory=[stealy3_items.umbrella, stealy3_items.hat]
)

study = Room(
    name="Study",
    description=(
        "There is a desk against the corner, under a window."
        ),
    xypos=[],
    inventory=[stealy3_items.laptop, stealy3_items.fancy_pen]
)

music_room = Room(
    name="Music Room",
    description=(
        "The music room has a baby-grand piano, recording equipment and a chandelier."
        ),
    xypos=[],
    inventory=[stealy3_items.guitar, stealy3_items.microphone, stealy3_items.synth]
)


# This room does not exist in game
# This is a place to store the murderer until he enters the game
waiting_room = Room(
    name="Waiting Room",
    description="How are you seeing this?",
    xypos=[-666, 666],
    inventory=[]
)

# This room does not exist in game
# This room is where the player escapes to when they escape the house
escape_room = Room(
    name="Escape Room",
    description="How are you seeing this?",
    xypos=[],
    inventory=[]
)
