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
    Item('pot', 'A pot for cooking some very tasty stew.'),  # Stretch: Created Item 'pot' and placed in 'Kitchen'
]


# Declare all the rooms
room = {
    # is_light == True
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons.", True, [items[0]]),

    # is_light == True
    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", True,
                  [items[1], items[5]]),

    # is_light == False
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
                      Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                     False, [items[2], items[6], items[9]]),

    # is_light == False
    'narrow': Room("Narrow Passage",
                   """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                   False, [items[3], items[7]]),

    # is_light == False
    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by 
                   earlier adventurers. The only exit is to the south.""", False, [items[4], items[8]]),

    # Stretch: Created kitchen room
    # is_light == True
    'kitchen': Room("Kitchen", """The smell of the food entices you into this kitchen full of yummy food.""", True,
                     [items[10]]),
}

# Stretch: Added LightSource object to list of items and the 'narrow' room
light_1 = LightSource('lamp', 'This will brighten the room!')
items.append(light_1)
room['narrow'].items.append(light_1)

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].e_to = room['kitchen']  # Stretch
room['kitchen'].w_to = room['overlook']  # Stretch
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


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

    is_valid = check_input(user_input)

    if is_valid:
        user_input = user_input.split(' ')
    elif not is_valid:
        print('\nYour input is invalid, please try again!')
        continue

    if len(user_input) == 1:
        if user_input[0] == 'q':
            print('Goodbye!')
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




