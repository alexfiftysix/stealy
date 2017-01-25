import random
import stealy3_rooms
import stealy3_items


# Generate rooms before game begins
def generate_room(room, room_list):
    # picks a room, then generates a room to its N, S, E or W
    room_chosen = False
    while not room_chosen:
        # can_build returns false if functions tried to build over an existing room
        can_build = True
        pick_base_room = random.randint(0, len(room_list)-1)
        base_room = room_list[pick_base_room]
        new_point = [x for x in base_room.xypos]
        direction = random.randint(0, 3)
        if direction == 0:
            new_point[1] += 1
        elif direction == 1:
            new_point[0] += 1
        elif direction == 2:
            new_point[1] -= 1
        else:
            new_point[0] -= 1

        # if room already is in new_point, return false and restart the loop
        for i in room_list:
            if new_point == i.xypos:
                can_build = False

        # if room can be built, set xypos and add to room_list
        if can_build:
            room.xypos = [x for x in new_point]
            room_list.append(room)
            room_chosen = True


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
def look_room(player, room_list):

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

    north_of_current = [x for x in player.room.xypos]
    north_of_current[1] += 1
    east_of_current = [x for x in player.room.xypos]
    east_of_current[0] += 1
    south_of_current = [x for x in player.room.xypos]
    south_of_current[1] -= 1
    west_of_current = [x for x in player.room.xypos]
    west_of_current[0] -= 1

    room_exits = []
    for i in room_list:
        if north_of_current == i.xypos:
            room_exits.append("North")

        if east_of_current == i.xypos:
            room_exits.append("East")

        if south_of_current == i.xypos:
            room_exits.append("South")

        if west_of_current == i.xypos:
            room_exits.append("West")

    print "Doors lead to the %s" % room_exits


# Player moves N, E, S, or W
# N = 0, E = 1, S = 2, W = 3
def player_move(player, room_list, direction):

    new_pos = [x for x in player.room.xypos]
    room_exists = False

    # Move North
    if direction == 0:
        new_pos[1] += 1
    # Move East
    elif direction == 1:
        new_pos[0] += 1
    # Move South
    elif direction == 2:
        new_pos[1] -= 1
    # Move West
    elif direction == 3:
        new_pos[0] -= 1
    else:
        print "Where are you going?"

    # Check if player xypos matches a room's xypos
    for i in room_list:
        if new_pos == i.xypos:
            room_exists = True
            player.room = i
        else:
            pass

    if not room_exists:
        print "You can't go there!"

    # If player enters the 'escape room'
    if player.room == stealy3_rooms.escape_room:
        print "Do you want to escape?"
        print "y/n?"
        action = raw_input("> ")
        if action.lower() == "y":
            end_game(player)
        else:
            player.room = stealy3_rooms.foyer
    print "You are in the " + player.room.name + "."


# player steals an object
def steal(player, sentence):
    thing_stolen = 0
    if len(player.inventory) >= 10:
        print "You can't hold more than 10 things!"
    else:
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
    murderer_direction = random.randint(0, 3)
    revert_murderer_pos = [x for x in murderer.room.xypos]

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

    direction = ""
    if murderer.room.xypos == player.room.xypos:
        if stealy3_items.knife in player.inventory:
            player.weapon = stealy3_items.attack_knife
            fight(player, murderer)
        else:
            print "You have been attacked by the murderer!"
            print "You have no means to defend yourself, you have been murdered!"
            exit(1)

    elif murderer.room.xypos[1] > player.room.xypos[1]:
        direction += "North-"

    elif murderer.room.xypos[1] < player.room.xypos[1]:
        direction += "South-"

    if murderer.room.xypos[0] < player.room.xypos[0]:
        direction += "West"

    elif murderer.room.xypos[0] > player.room.xypos[0]:
        direction += "East"

    if len(direction) == 6:
        direction = direction[:-1]
    if murderer.alive:
        print "You hear movement to the " + direction + "."


#######################################
# Combat specific functions are below #
#######################################

def attack(attack_player, hit_player, move_index):
    print "%s used %s." % (attack_player.name, attack_player.weapon.move_list[move_index].name)
    power = attack_player.attack_power(move_index)
    print "%s did %s damage." % (attack_player.weapon.move_list[move_index].name, power)
    hit_player.hp -= power


def choose_attack(player):
    count = 1
    attack_1 = "1. " + player.weapon.move_list[0].name
    attack_2 = "2. " + player.weapon.move_list[1].name

    for i in player.weapon.move_list:
        print str(count) + ". " + i.name + " "*(15-len(i.name)) + "[%s/%s]" % (i.ap, i.max_ap)
        count += 1

    action = raw_input("> ")
    for i in range(len(player.weapon.move_list)):
        if action.lower() in player.weapon.move_list[i].name.lower():
            if player.weapon.move_list[i].ap <= 0:
                print "Out of Attack Points"
                return choose_attack(player)

            player.weapon.move_list[i].ap -= 1
            return i

    if action in attack_1:
        if player.weapon.move_list[0].ap <= 0:
            print "Out of Attack Points"
            return choose_attack(player)
        else:
            player.weapon.move_list[0].ap -= 1
            return 0
    elif action in attack_2:
        if player.weapon.move_list[1].ap <= 0:
            print "Out of Attack Points"
            return choose_attack(player)
        else:
            player.weapon.move_list[1].ap -= 1
            return 1


def choose_move(player1, player2):
    attack_1 = "1. Attack"
    print attack_1

    action = raw_input("> ")
    if action.lower() in attack_1.lower():
        selection = choose_attack(player1)
        attack(player1, player2, selection)


def print_name_and_hp(player1, player2):
    raw_input("> ")
    top_line = "# " + player2.name + "[" + str(player2.hp) + "/" + str(player2.max_hp) + "]"
    bottom_line = player1.name + "[" + str(player1.hp) + "/" + str(player1.max_hp) + "]"
    print
    print "#" * 40
    print top_line + " " * (39 - len(top_line)) + "#"
    print "#" + " " * (37 - len(bottom_line)) + bottom_line + " #"
    print "#" * 40
    print


def fight(player1, player2):
    print "You have been challenged by %s" % player2.name + "!"
    fighting = True
    while fighting:
        print_name_and_hp(player1, player2)

        # Player turn
        move_index = choose_attack(player1)
        attack(player1, player2, move_index)
        if player2.hp <= 0:
            print '%s wins, with %s hp remaining.' % (player1.name, player1.hp)
            break

        print_name_and_hp(player1, player2)
        raw_input("> ")
        # AI turn
        attack(player2, player1, 0)
        if player1.hp <= 0:
            raw_input("> ")
            print '%s wins with %s hp remaining.' % (player2.name, player2.hp)
            print 'You are dead!'
            exit(1)

    player2.alive = False
    print "You defeated the murderer! Steal to your heart's content."


# Main function, takes player input and runs other functions accordingly
def play(player, murderer, room_list):
    turns = 1
    print "Welcome to Stealy, the game of stealing!"
    print "Steal all you can, and escape unscathed!"
    print "You are in the %s" % player.room.name
    print "type 'controls' to see the game controls"

    while True:

        old_turns = turns

        action = raw_input("...\n>").lower()

        # Player checks inventory
        if "inv" in action:
            check_player_inv(player)

        # Player looks around room
        elif "look" in action:
            look_room(player, room_list)

        # Player looks at map
        elif "map" in action:
            for i in room_list:
                print i.name + "_" * (15-len(i.name)) + str(i.xypos)

        # Player steals an item
        elif "steal" in action:
            steal(player, action)
            turns += 1

        # Player drops an item
        elif "drop" in action:
            drop(player, action)
            turns += 1

        # Player does nothing
        elif "stay" in action or "wait" in action:
            turns += 1

        # Player moves
        elif "north" in action:
            player_move(player, room_list, 0)
            turns += 1
        elif "east" in action:
            player_move(player, room_list, 1)
            turns += 1
        elif "south" in action:
            player_move(player, room_list, 2)
            turns += 1
        elif "west" in action:
            player_move(player, room_list, 3)
            turns += 1

        # Player checks controls
        elif "controls" in action:
            print "look__________________look at room"
            print "inv___________________look at player inventory"
            print "move__________________move"
            print "steal 'item'__________steals 'item' from room"
            print "drop 'item'___________drops 'item' from inventory"
            print "move 'direction_______moves in 'direction'"
            print "wait__________________wait a turn"
            print "escape________________escape the house"


        # Player wants to escape house
        elif "escape" in action:
            answer = raw_input("Do you want to escape?\ny/n?\n> ")
            if answer == "y":
                end_game(player)

        # action is not understood by program
        else:
            print "I don't understand."




        # Murderer becomes active after 5 turns
        if murderer.alive:
            if turns == 5 and turns != old_turns:
                print "You hear someone come home!"
                murderer.room = stealy3_rooms.foyer
            elif turns > 5 and turns != old_turns:
                murderer_move(murderer, room_list)
                check_murderer_player_pos(murderer, player)

            if player.room == stealy3_rooms.escape_room:
                action = raw_input("Do you want to escape the house?\n>")
                if "n" in action:
                    player.room = stealy3_rooms.foyer
                    print "You are in the %s" % player.room.name
                elif "y" in action:
                    end_game(player)
