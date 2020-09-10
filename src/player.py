# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, items=None):
        if items is None:
            items = []
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f'{self.name}, {self.current_room}'

    def move_room(self, direction, next_room):
        if next_room is None:
            print(f'You cannot move to {direction} from the {self.current_room.name}.')
            print('Please try another direction.\n')
            return
        self.current_room = next_room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        if not self.items:
            print(f'{self.name} currently has no items')
            return
        print(f'{self.name} has the following items: ')
        for item in self.items:
            print(item)
