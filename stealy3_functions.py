from random import randint
import stealy3_rooms
# Checks player inventory
def check_player_inv(player):


    if len(player.inventory) < 1:
        print "You have nothing in your inventory."

    else:
        print "player inv is..."
        for i in player.inventory:
            spaces = 0
            while (len(i.name) + spaces) < 15:
                spaces += 1
            print (
                   i.name
                   + "_"*spaces
                   + "$"
                   + str(i.worth)
                   )



# Looks around the room the player is currently in
def look_room(player):


    print "You are in the", player.room.name + "."
    print player.room.description

    if len(player.room.inventory) < 1:
        print "There is nothing to steal here."

    else:
        print "The %s contains:" % player.room.name
        for i in player.room.inventory:
            spaces = 0
            while (len(i.name) + spaces) < 15:
                spaces += 1
            print (
                   i.name
                   + "_"*spaces
                   + "$"
                   + str(i.worth)
                   )



#Player moves N, E, S, or W
# N = 0, E = 1, S = 2, W = 3
def player_move(player, room_list, direction):


    global revert_pos
    revert_pos = [x for x in player.room.xypos]
    room_exists = 0

    # Move North
    if direction == 0:
        revert_pos[1] += 1
    elif direction == 1:
        revert_pos[0] += 1
    elif direction == 2:
        revert_pos[1] -= 1
    elif direction == 3:
        revert_pos[0] -= 1
    else:
        print "Where are you going?"

    for i in room_list:
        if revert_pos == i.xypos:
            room_exists = 1
            player.room = i
        else:
            pass
    if room_exists == 0:
        print "You can't go there!"

    print "You are in the " + player.room.name + "."



# player steals an object
def steal(player, sentence):
    thing_stolen = 0
    for i in player.room.inventory:
        if i.name in sentence:
            print "Stealing " + i.name
            player.room.inventory.pop(player.room.inventory.index(i))
            player.inventory.append(i)
            thing_stolen = 1

    if thing_stolen != 1:
        print "Can't find '%s' to steal" % sentence



# Player drops an object
def drop(player, sentence):
    item_dropped = 0
    for i in player.inventory:
        if i.name in sentence:
            print "dropping", i.name
            player.room.inventory.append(i)
            player.inventory.pop(player.inventory.index(i))
            item_dropped = 1
    if item_dropped != 1:
        print "Can't find thing to drop."



def end_game(player):
    score = 0
    for i in player.inventory:
        score += i.worth
    if score > 0:
        print "Well done, you stole some loot and escaped unscathed!"
        print "You fence your stolen goods for $%s!" % score
        print "Congratulations!"
    elif score <= 0:
        print "You didn't steal anything!"
    exit()


###############################################



# Murderer moves
def murderer_move(murderer, room_list):
    murderer_direction = randint(0, 3)
    revert_murderer_pos = [x for x in murderer.room.xypos]
    murderer_moved = 0

    if murderer_direction == 0:
        revert_murderer_pos[1] += 1
    elif murderer_direction == 1:
        revert_murderer_pos[0] += 1
    elif murderer_direction == 2:
        revert_murderer_pos[1] -= 1
    elif murderer_direction == 3:
        revert_murderer_pos[0] -= 1
    else:
        print "Where are you going?"

    for i in room_list:
        if i.xypos == revert_murderer_pos:
            murderer.room = i

    # if murder room is escape room, in ther words
    if murderer.room.xypos == [0, 2]:
        print "murderer tried to escape"
        murderer.room = stealy3_rooms.foyer



# Checks player pos relative to murder position
def check_murderer_player_pos(murderer, player):
    murdered = 0
    if murderer.room.xypos == player.room.xypos:
        print "The murderer is in the room with you!"
        print "You have been murdered!"
        exit()

    elif (murderer.room.xypos[0] == player.room.xypos[0]
        and murderer.room.xypos[1] > player.room.xypos[1]):
        direction = "North"

    elif (murderer.room.xypos[0] > player.room.xypos[0]
        and murderer.room.xypos[1] > player.room.xypos[1]):
        direction = "North-East"

    elif (murderer.room.xypos[0] > player.room.xypos[0]
        and murderer.room.xypos[1] == player.room.xypos[1]):
        direction = "East"

    elif (murderer.room.xypos[0] > player.room.xypos[0]
        and murderer.room.xypos[1] < player.room.xypos[1]):
        direction = "South-East"

    elif (murderer.room.xypos[0] == player.room.xypos[0]
        and murderer.room.xypos[1] < player.room.xypos[1]):
        direction = "South"

    elif (murderer.room.xypos[0] < player.room.xypos[0]
        and murderer.room.xypos[1] < player.room.xypos[1]):
        direction = "South-West"

    elif (murderer.room.xypos[0] < player.room.xypos[0]
        and murderer.room.xypos[1] == player.room.xypos[1]):
        direction = "West"

    elif (murderer.room.xypos[0] < player.room.xypos[0]
        and murderer.room.xypos[1] > player.room.xypos[1]):
        direction = "North-West"

    print "You hear movement to the " + direction + "."
