#### All classes for the game Stealy 3, the Stealening, are below


# Use this class when making new rooms
class room(object):
    def __init__(self, name, description, xypos, inventory):
        self.name = name
        self.description = description
        self.xypos = xypos
        self.inventory = inventory

# Use this class when making new items
class item(object):
    def __init__(self, name, worth):
        self.name = name
        self.worth = worth

class Player(object):
    def __init__(self, name, room):
        self.name = "Jeff"
        self.inventory = []
        self.room = room

class Murderer(object):
    def __init__(self, room):
        self.room = room
