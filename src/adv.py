from room import Room
from player import Player
from item import Item
from lightsource import LightSource

# Create list of items
items = [
    Item('sword', 'This is a very sharp sword.'),
    Item('book', 'This book is full of magical spells.'),
    Item('chest', 'This chest can be used to store all your stuff.'),
    Item('cup', 'This will be of good use when you need a cold drink.'),
    Item('basketball', 'This basketball is full of air and ready for a game.'),
    Item('gloves', 'A pair of gloves that are fire retardant.'),
    Item('bicycle', 'This bicycle is in good shape and ready to be ridden.'),
    Item('notebook', 'This notebook has plenty of space for all your thoughts.'),
    Item('pencil', 'A #2 pencil sharpened and ready for you to write or draw anything.'),
    Item('helmet', 'A helmet that can protect you in certain situations.'),
]

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
                      Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage",
                   """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by 
                   earlier adventurers. The only exit is to the south."""),
}

# Set initial items for each room
room['outside'].add_item(items[0])  # sword
room['foyer'].add_item(items[1])  # book
room['foyer'].add_item(items[5])  # gloves
room['overlook'].add_item(items[2])  # chest
room['overlook'].add_item(items[6])  # bicycle
room['overlook'].add_item(items[9])  # helmet
room['narrow'].add_item(items[3])  # cup
room['narrow'].add_item(items[7])  # notebook
room['treasure'].add_item(items[4])  # basketball
room['treasure'].add_item(items[8])  # pencil

# Stretch: Add a new room
kitchen = Room("Kitchen", "The smell of the food entices you into this kitchen full of yummy food.")
room['kitchen'] = kitchen

# Create a new item and add it to kitchen
pot = Item('pot', 'A pot for cooking some very tasty stew.')
items.append(pot)
room['kitchen'].add_item(pot)

# Stretch: Set the is_light value for each room
room['outside'].is_light = True
room['foyer'].is_light = True
room['overlook'].is_light = False
room['narrow'].is_light = False
room['treasure'].is_light = False
room['kitchen'].is_light = True

# Stretch: Added LightSource object to list of items and the 'narrow' room
light_1 = LightSource('lamp', 'This will brighten the room!')
items.append(light_1)
room['narrow'].add_item(light_1)

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].e_to = room['kitchen']
room['kitchen'].w_to = room['overlook']
room['kitchen'].e_to = room['treasure']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].w_to = room['kitchen']


#
# Main
#

# Function checks user input and if correct returns True, otherwise False
def check_input(inp):
    inp = inp.lower().split(' ')

    if len(inp) > 2:
        return False
    elif len(inp) == 1 and inp[0] != 'q' and inp[0] != 'n' and inp[0] != 's' and inp[0] != 'e' and inp[0] != 'w' \
            and inp[0] != 'i' and inp[0] != 'inventory':
        return False
    elif len(inp) == 2 and inp[0] != 'get' and inp[0] != 'take' and inp[0] != 'drop':
        return False
    else:
        return True


# Make a new player object that is currently in the 'outside'
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

name_input = input(f'Enter your name: ')
# while loop to check that the user name input is at least one character long
while len(name_input) == 0:
    print('\nYour name must be at least one character long!')
    name_input = input(f'Enter your name: ')

p1 = Player(name_input, room['outside'])

print(f'\nHello {p1.name}, welcome to the game!')
print("Enter 'q' at anytime to quit the game.\n")

print(f'You are currently in the {p1.current_room}')
# Called check_light function to check if initial room is lite or has a light source
p1.check_light()

# While loop, loops until player inputs 'q'
while True:
    user_input = input("\nEnter a direction ('n', 's', 'e', 'w') to move or 'get/take item_name' or 'drop item_name', "
                       "('i' or 'inventory' to see your items): ").lower()

    # Calling check_input to check if the player's input is in the correct form
    if check_input(user_input):
        user_input = user_input.split(' ')
    elif not check_input(user_input):
        print('\nYour input is invalid, please try again!')
        continue

    if len(user_input) == 1:
        if user_input[0] == 'q':
            print('\nGoodbye!')
            break
        elif user_input[0] == 'n':
            p1.move_rooms('north', p1.current_room.n_to)
        elif user_input[0] == 's':
            p1.move_rooms('south', p1.current_room.s_to)
        elif user_input[0] == 'e':
            p1.move_rooms('east', p1.current_room.e_to)
        elif user_input[0] == 'w':
            p1.move_rooms('west', p1.current_room.w_to)
        elif user_input[0] == 'i' or user_input[0] == 'inventory':
            p1.print_items()

    if len(user_input) == 2:
        p1.set_items(user_input[0], user_input[1])
