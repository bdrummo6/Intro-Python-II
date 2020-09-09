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

def set_items(pl, verb, it_name):
    it = None
    it_2 = None
    for item in pl.current_room.items:
        if item.name == it_name:
            it = item

    for item2 in pl.items:
        if item2.name == it_name:
            it_2 = item2

    count_room = pl.current_room.items.count(it)
    count_player = pl.items.count(it_2)
    if verb == 'take':
        if count_room == 0:
            print(f'The item with the name {it_name} does not exist in this room!')
            return
        pl.items.append(it)
        pl.current_room.items.remove(it)
        it.on_take()
    elif verb == 'drop':
        if count_player == 0:
            print(f'The item with the name {it_name} is not in your collection!')
            return
        pl.items.remove(it_2)
        pl.current_room.items.append(it_2)


def get_items(obj):
    for item in obj.items:
        return item


def print_items(obj):
    if obj.items == []:
        print(f'{obj.name} currently has no items')
        return
    print(f'{obj.name} has the following items: ')
    for item in obj.items:
        print(item)


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
    print_items(p1.current_room)
    print_items(p1)

    user_input = input("\nEnter a direction ('n', 's', 'e', 'w') to move or 'take item_name' or 'drop item_name' "
                       "('q' to quit): ")
    u_input = user_input.split(' ')

    if len(u_input) == 1:
        if u_input[0] == 'q':
            print('Goodbye!')
            break
        elif u_input[0] == 'n':
            if p1.current_room.n_to is None:
                print(f'You cannot move north from the {p1.current_room.name}!')
                continue
            p1.current_room = p1.current_room.n_to
            print_items(p1.current_room)
            print_items(p1)
        elif u_input[0] == 's':
            if p1.current_room.s_to is None:
                print(f'You cannot move south from the {p1.current_room.name}!')
                continue
            p1.current_room = p1.current_room.s_to
            print_items(p1.current_room)
            print_items(p1)
        elif u_input[0] == 'e':
            if p1.current_room.e_to is None:
                print(f'You cannot move east from the {p1.current_room.name}')
                continue
            p1.current_room = p1.current_room.e_to
            print(f'You have moved to the {p1.current_room}.')
            print_items(p1.current_room)
            print_items(p1)
        elif u_input[0] == 'w':
            if p1.current_room.w_to is None:
                print(f'You cannot move west from the {p1.current_room.name}!')
                continue
            p1.current_room = p1.current_room.w_to
            print_items(p1.current_room)
            print_items(p1)

    if len(u_input) == 2:
        set_items(p1, u_input[0], u_input[1])


