import gc
from sys import exit
from random import randint

#Use this class when making new rooms
class room(object):
    def __init__(self, name, description, xypos, inventory):
        self.name = name
        self.description = description
        self.xypos = xypos
        self.inventory = inventory

#Use this class when making new items
class item(object):
    def __init__(self, name, worth):
        self.name = name
        self.worth = worth

#######################
## ITEMS SET UP HERE ##
#######################
knife = item(
name = 'knife',
worth = 25
)

mugs = item(
name = 'mugs',
worth = 5
)

microwave = item(
'microwave',
30
)

######################
## ROOM SET UP HERE ##
######################

kitchen = room(
name ='Kitchen',
description = "There is shattered glass on the ground from your forced entry. \nA bench runs along the north and east walls of the room. \nThere are doors to the North and the West.",
xypos = [1, 0],
inventory = [['knife', 25], ['mugs', 5], ['microwave', 30]]
)

lounge_room = room(
name ='Lounge room',
description = "There is a couch on the west wall of the room. \nThere is a door to the South, and one to the West.",
xypos = [1, 1],
inventory = [['tv', 200], ['art', 300], ['console', 150]]
)

dining_room = room(
name = 'Dining room',
description = "A large table is in the centre of the room. \nThe table is freshly laid with 6 places.\nDoors lead to the East and North",
xypos = [0, 0],
inventory = [['plates', 10], ['cutlery', 15], ['placemats', 2]]
)

foyer = room(
name = "Foyer",
description = "The front door is to the North, and doors lead to the South and East.",
xypos = [0, 1],
inventory = [['umbrella', 15], ['hat', 12]]
)

########################
## PLAYER SET UP HERE ##
########################

player_room = kitchen
player_pos = [x for x in player_room.xypos]
revert_pos = [x for x in player_room.xypos]
player_inv = []
turns = 0

# Checks player's inventory
def look_player_inv():
    if len(player_inv) < 1:
        print "You have nothing in your inventory"
    else:
        for i in player_inv:
            print "%s    :    $%s" % (i[0], i[1])

# Looks around the room the player is currently in
def look_room():
    print "You are in the", player_room.name
    print player_room.description
    if len(player_room.inventory) < 1:
        print "There is nothing to steal here."
    else:
        print "The %s contains:" % player_room.name
        for i in player_room.inventory:
            print "%s   :   $%s" % (i[0], i[1])

#Checks which room player is in using xypos
def check_player_pos():
    global player_pos
    global player_room
    for obj in gc.get_objects():
        if isinstance(obj, room) and player_pos == obj.xypos:
            player_room = obj
            player_pos = [x for x in player_room.xypos]
            break

        else:
            pass
    # If player tries to enter non-location, reverts to previous location
    if player_room.xypos != player_pos:
        player_pos = revert_pos
        print "ERROR - PLAYER OUT OF BOUNDS\nRETURNING TO PREVIOUS LOCATION"

    print "you are now in the", player_room.name

#Prints all objects of class 'room'
def print_all_rooms():
    for obj in gc.get_objects():
        if isinstance(obj, room):
            print obj.name

#Player moves N, E, S, or W
# N = 0, E = 1, S = 2, W = 3
def player_move(direction):
    global revert_pos
    revert_pos = [x for x in player_pos]
    if direction == 0:
        player_pos[1] += 1
        print "Player has moved North"
        check_player_pos()
    elif direction == 1:
        player_pos[0] += 1
        print "Player has moved East"
        check_player_pos()
    elif direction == 2:
        player_pos[1] -= 1
        print "Player has moved South"
        check_player_pos()
    elif direction == 3:
        player_pos[0] -= 1
        print "Player has moved West"
        check_player_pos()
    else:
        print "Where are you going?"

# player steals an object
def steal(sentence):
    thing_stolen = 0
    for i in player_room.inventory:
        if i[0] in sentence:
            print "stealing", i[0]
            player_inv.append(i)
            player_room.inventory.pop(player_room.inventory.index(i))
            thing_stolen = 1

    if thing_stolen != 1:
        print "Can't find thing to steal"


# Player drops an object
def drop(sentence):
    item_dropped = 0
    for i in player_inv:
        if i[0] in sentence:
            print "dropping", i[0]
            player_room.inventory.append(i)
            player_inv.pop(player_inv.index(i))
            item_dropped = 1
    if item_dropped != 1:
        print "Can't find thing to drop."

##############################
## MURDERER FUNCTIONS BELOW ##
##############################

murderer_pos = [0, 1]
revert_murderer_pos = []
murderer_room = foyer

# Murderer moves
def murderer_move():
    murderer_direction = randint(0, 3)
    global revert_murderer_pos
    revert_murderer_pos = [x for x in murderer_pos]

    if murderer_direction == 0:
        murderer_pos[1] += 1
        check_murderer_pos()
    elif murderer_direction == 1:
        murderer_pos[0] += 1
        check_murderer_pos()
    elif murderer_direction == 2:
        murderer_pos[1] -= 1
        check_murderer_pos()
    elif murderer_direction == 3:
        murderer_pos[0] -= 1
        check_murderer_pos()
    else:
        print "Where are you going?"

#Checks which room murderer is in using xypos
def check_murderer_pos():
    global murderer_pos
    global murderer_room
    for obj in gc.get_objects():
        if isinstance(obj, room) and murderer_pos == obj.xypos:
            murderer_room = obj
            murderer_pos = [x for x in murderer_room.xypos]
            break

        else:
            pass

# If murderer tries to go out of bounds, murderer returns to previous location
    if murderer_room.xypos != murderer_pos:
        murderer_pos = revert_murderer_pos

    print "You hear someone moving in the", murderer_room.name

#Checks turns, if greater than 5, murderer enters house
def check_turns():
    global murderer_room
    print murderer_pos
    if turns < 5:
        pass
    elif turns == 5:
        print "You hear the door turn in the foyer, quick, hide!"
    elif turns == 6:
        if murderer_pos == player_pos:
            print "You were found, and murdered!\nGame Over"
            exit()
    elif turns > 6:
        murderer_move()
        print "..."
        if murderer_pos == player_pos:
            print "You were found, and murdered!"
            exit()

#####################################
# Player turn code runs below here
# Player turn takes input from player and runs functions accordingly
# Runs constantly untill game over
#####################################

def playerturn():
    global turns
    player_choice = raw_input(">").lower()

    #Player looks
    if "look" in player_choice:
        look_room()

    # Player looks at inventory
    elif "inv" in player_choice:
        look_player_inv()

    #player moves, simple
    elif "north" in player_choice:
        player_move(0)
    elif "east" in player_choice:
        player_move(1)
    elif "south" in player_choice:
        player_move(2)
    elif "west" in player_choice:
        player_move(3)

    #Player moves, with options
    elif "move" in player_choice:
        ask = raw_input("Which way?\nN, E, S, W\n>")
        if ask == "n":
            player_move(0)
        elif ask == "e":
            player_move(1)
        elif ask == "s":
            player_move(2)
        elif ask == "w":
            player_move(3)
        else:
            print "I don't understand"

    #player exits game
    elif "exit" in player_choice:
        ask = raw_input("Exit? Are you sure?\n>").lower()
        if "y" in ask:
            exit()
        else:
            pass

    #Player steals an item
    elif 'steal' in player_choice:
        steal(player_choice)

    elif 'drop' in player_choice:
        drop(player_choice)

    #Player does none of the above
    else:
        print "I don't understand"

    turns += 1
    print "..."




#Starts game








look_room()
print "..."
while True:
    playerturn()
    check_turns()










#
#########################
