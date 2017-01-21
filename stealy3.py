# TO DO LIST:
#


from sys import exit
from random import randint

import stealy3_items
import stealy3_rooms
import stealy3_functions
import stealy3_classes

# Set up takes place below here!

# Room list is required for room movement functions
room_list = [stealy3_rooms.kitchen, stealy3_rooms.lounge_room,
             stealy3_rooms.dining_room, stealy3_rooms.foyer,
             stealy3_rooms.escape_room, stealy3_rooms.study,
             stealy3_rooms.music_room ]

# Making player
player = stealy3_classes.Player("Jeff", stealy3_rooms.kitchen)
turns = 0


# Making a Murderer
murderer = stealy3_classes.Murderer(stealy3_rooms.waiting_room)



# Main function, takes player input and runs functions accordingly
def play():
    global turns
    moved = 0
    old_turns = turns

    action = raw_input("...\n>").lower()


    # Player checks inventory
    if "inv" in action:
        stealy3_functions.check_player_inv(player)


    # Player looks around room
    elif "look" in action:
        stealy3_functions.look_room(player)


    # Player moves
    elif ("move" in action or "go" in action
        and "north" not in action
        and "east" not in action
        and "south" not in action
        and "west" not in action):
        messed_up = 0
        action_2 = raw_input("Which direction would you like to go\n>")
        if "north" in action_2:
            direction = 0
        elif "east" in action_2:
            direction = 1
        elif "south" in action_2:
            direction = 2
        elif "west" in action_2:
            direction = 3
        else:
            print "I don't understand"
            messed_up = 1

        if messed_up == 1:
            stealy3_functions.player_move(player, room_list, direction)
            turns += 1


    # Player steals an item
    elif "steal" in action:
        stealy3_functions.steal(player, action)
        turns += 1


    # Player drops an item
    elif "drop" in action:
        stealy3_functions.drop(player, action)
        turns += 1


    # Player does nothing
    elif "stay" in action or "wait" in action:
        turns += 1


    # Player moves
    elif "north" in action:
        stealy3_functions.player_move(player, room_list, 0)
        turns += 1
    elif "east" in action:
        stealy3_functions.player_move(player, room_list, 1)
        turns += 1
    elif "south" in action:
        stealy3_functions.player_move(player, room_list, 2)
        turns += 1
    elif "west" in action:
        stealy3_functions.player_move(player, room_list, 3)
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
    else:
        print "I don't understand."



    # Murderer becomes active after 5 turns
    if turns == 1 and turns != old_turns:
        print "You hear someone come home!"
        murderer.room = stealy3_rooms.foyer
    elif turns > 1 and turns != old_turns:
        stealy3_functions.murderer_move(murderer, room_list)
        stealy3_functions.check_murderer_player_pos(murderer, player)

# Gameplay loop here!
print "Welcome to Stealy, the game of stealing!"
print "Steal all you can, and escape unscathed!"
print "type 'controls' to see the game controls"
while True:
    play()


    if player.room == stealy3_rooms.escape_room:
        action = raw_input("Do you want to escape the house?\n>")
        if "n" in action:
            player.room = stealy3_rooms.foyer
            print "You are in the %s" % player.room.name
        elif "y" in action:
            stealy3_functions.end_game(player)
