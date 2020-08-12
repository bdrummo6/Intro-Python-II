from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
                      Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. 
                      The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already  
                      been completely emptied by earlier adventurers. The only exit is to the south."""),
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

# Make a new player object that is currently in the 'outside' room.
p1 = Player('Brad', room['outside'])
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
print(f'Hello {p1.name}, welcome to the game!')
print(f'{p1.name}, you are currently in the {p1.current_room.name}.')
while True:
    user_input = input('Input a direction to move rooms or press q to quit the game: ')
    if user_input.lower() == 'q':
        print('Goodbye!')
        break

    if user_input.lower() == 'north':
        if p1.current_room.n_to is None:
            print('You cannot move north from your current room.\n')
            continue
        p1.current_room = p1.current_room.n_to
        print(f'You have moved to the {p1.current_room.name}.\n')
    elif user_input == 'south':
        if p1.current_room.s_to is None:
            print('You cannot move south from your current room.\n')
            continue
        p1.current_room = p1.current_room.s_to
        print(f'You have moved to the {p1.current_room.name}.\n')
    elif user_input == 'east':
        if p1.current_room.e_to is None:
            print('You cannot move east from your current room.\n')
            continue
        p1.current_room = p1.current_room.e_to
        print(f'You have moved to the {p1.current_room.name}.\n')
    elif user_input == 'west':
        if p1.current_room.w_to is None:
            print('You cannot move west from your current room.\n')
            continue
        p1.current_room = p1.current_room.w_to
        print(f'You have moved to the {p1.current_room.name}.\n')


