#######################
#  ITEMS SET UP HERE  #
#######################

import stealy3_classes
from stealy3_classes import Item

knife = Item(
    name='knife',
    worth=25
)

mugs = Item(
    name='mugs',
    worth=5
)

microwave = Item(
    'microwave',
    30
)

tv = Item(
    'tv',
    200
)

art = Item(
    'art',
    300
)

console = Item(
    'console',
    150
)

plates = Item(
    'plates',
    10
)

cutlery = Item(
    'cutlery',
    15
)

placemats = Item(
    'placemats',
    2
)

umbrella = Item(
    'umbrella',
    15
)

hat = Item(
    'hat',
    12
)

laptop = Item(
    'laptop',
    250
)

fancy_pen = Item(
    'fancy_pen',
    10
)

guitar = Item(
    'guitar',
    300
)

microphone = Item(
    'microphone',
    75
)

synth = Item(
    'synth',
    125
)


# Attack types
poke = stealy3_classes.Attack('Poke', 1, 20)
stab = stealy3_classes.Attack('Stab', 1.5, 10)
slash = stealy3_classes.Attack('Slash', 1.1, 15)
swing = stealy3_classes.Attack('Swing', 1.7, 3)
clobber = stealy3_classes.Attack('Clobber', 1, 20)
thud = stealy3_classes.Attack('Thud', 2, 2)

# Weapon types
stabbing_weapon = [poke, stab]
slashing_weapon = [slash, swing]
blunt_weapon = [clobber, thud]

# Weapons
attack_knife = stealy3_classes.Weapon('Knife', 7, stabbing_weapon)
sword = stealy3_classes.Weapon('Sword', 15, slashing_weapon)
mace = stealy3_classes.Weapon('Mace', 12, blunt_weapon)
spoon = stealy3_classes.Weapon('Spoon', 1, blunt_weapon)

# Potion types
small_potion = stealy3_classes.Potion("Small Potion", 15)
large_potion = stealy3_classes.Potion("Large Potion", 50)
