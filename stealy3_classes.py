# All classes for the game Stealy 3, the Stealening, are below


# Use this class when making new rooms
class Room(object):
    def __init__(self, name, description, xypos, inventory):
        self.name = name
        self.description = description
        self.xypos = xypos
        self.inventory = inventory


# Use this class when making new items
class Item(object):
    def __init__(self, name, worth):
        self.name = name
        self.worth = worth


class Player(object):
    def __init__(self, name, room):
        self.name = name
        self.hp = 50
        self.max_hp = 50
        self.power = 1
        self.weapon = None
        self.inventory = []
        self.room = room
        self.alive = True

    def attack_power(self, move_index):
        return int(self.power * self.weapon.power * self.weapon.move_list[move_index].power)


class Weapon(object):
    def __init__(self, name, power, move_list):
        self.name = name
        self.power = power
        self.move_list = move_list


class Potion(object):
    def __init__(self, name, heal_power):
        self.name = name
        self.heal_power = heal_power


class Attack(object):
    def __init__(self, name, power, ap):
        self.name = name
        self.power = power
        self.ap = ap
        self.max_ap = ap
