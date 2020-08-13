from room import Room
from player import Player
from item import Item
import textwrap

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


def get_room_items(rm):
    if rm.items is None:
        print(f'The {rm.name} contains no items.')
    else:
        print(f'{rm.name} contains the following items: ')
        for it in rm.items:
            return it


def get_player_items(pl):
    print(f'{pl.name} has the following items: ')
    if pl.items is None:
        return 'You currently have no items'
    for it in pl.items:
        return it


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

p1 = Player(name_input, room['outside'])

print(f'Hello {p1.name}, welcome to the game!')

while True:
    user_input = input("\nEnter a direction to move in ('n', 's', 'e', 'w') or 'q' to quit: ")
    if user_input == 'q':
        print('Goodbye!')
        break

    if user_input == 'n':
        if p1.current_room.n_to is None:
            print(f'You cannot move north from the {p1.current_room.name}!')
            continue
        p1.current_room = p1.current_room.n_to
        print(f'You have moved to the {p1.current_room}.')
        print(get_room_items(p1.current_room))
    elif user_input == 's':
        if p1.current_room.s_to is None:
            print(f'You cannot move south from the {p1.current_room.name}!')
            continue
        p1.current_room = p1.current_room.s_to
        print(f'You have moved to the {p1.current_room}.')
        print(get_room_items(p1.current_room))
    elif user_input == 'e':
        if p1.current_room.e_to is None:
            print(f'You cannot move east from the {p1.current_room.name}')
            continue
        p1.current_room = p1.current_room.e_to
        print(f'You have moved to the {p1.current_room}.')
        print(get_room_items(p1.current_room))
    elif user_input == 'w':
        if p1.current_room.w_to is None:
            print(f'You cannot move west from the {p1.current_room.name}!')
            continue
        p1.current_room = p1.current_room.w_to
        print(f'You have moved to the {p1.current_room}.')
        print(get_room_items(p1.current_room))

