from room import Room
from player import Player
from item import Item

# Create list of items
items = [
    Item('sword', 'This is a very sharp sword.'),
    Item('book', 'This book is full of magical spells.'),
    Item('chest', 'This chest can be used to store all your stuff.'),
    Item('lighter', 'This can be used to light a fire on cold nights.'),
    Item('basketball', 'This basketball is full of air and ready for a game.'),
    Item('gloves', 'A pair of gloves that are fire retardant.'),
    Item('bicycle', 'This bicycle is in good shape and ready to be ridden.'),
    Item('notebook', 'This notebook has plenty of space for all your thoughts.'),
    Item('pencil', 'A #2 pencil sharpened and ready for you to write or draw anything.'),
    Item('helmet', 'A helmet that can protect you in certain situations.'),
]

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", [items[0]]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""",
                  [items[1], items[5]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
                      Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                     [items[2], items[6], items[9]]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. 
                      The smell of gold permeates the air.""", [items[3], items[7]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already  
                      been completely emptied by earlier adventurers. The only exit is to the south.""",
                     [items[4], items[8]]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

def check_input(inp):
    pl_inp = inp.split(' ')

    if len(pl_inp) > 2:
        print(f'The number of inputs is invalid, please try again.\n')
        return
    elif pl_inp[0] != 'q' and pl_inp[0] != 'n' and pl_inp[0] != 's' and pl_inp[0] != 'e' and pl_inp[0] != 'w' \
            and pl_inp[0] != 'take' and pl_inp[0] != 'drop':
        print(f'Your input is invalid, please try again!\n')
        return


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

while len(name_input) == 0:
    print('\nYour name must be at least one character long!')
    name_input = input(f'Enter your name: ')

p1 = Player(name_input, room['outside'])

print(f'\nHello {p1.name}, welcome to the game!')

while True:
    print(f'You are currently in the {p1.current_room.name}!')
    p1.current_room.print_items()
    p1.print_items()

    user_input = input("\nEnter a direction ('n', 's', 'e', 'w') to move or 'take item_name' or 'drop item_name' "
                       "('q' to quit): ")
    check_input(user_input)
    u_input = user_input.split(' ')

    if len(u_input) == 1:
        if u_input[0] == 'q':
            print('Goodbye!')
            break
        elif u_input[0] == 'n':
            p1.move_room('north', p1.current_room.n_to)
        elif u_input[0] == 's':
            p1.move_room('south', p1.current_room.s_to)
        elif u_input[0] == 'e':
            p1.move_room('east', p1.current_room.e_to)
        elif u_input[0] == 'w':
            p1.move_room('west', p1.current_room.w_to)

    if len(u_input) == 2:
        p1.set_items(u_input[0], u_input[1])




