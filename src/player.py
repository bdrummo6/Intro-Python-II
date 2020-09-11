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

    def set_items(self, verb, item_name):
        it = None

        for item in self.current_room.items:
            if item.name == item_name:
                it = item

        for item in self.items:
            if item.name == item_name:
                it = item

        count_player = self.items.count(it)
        count_room = self.current_room.items.count(it)

        if verb == 'take':
            if count_room == 0:
                print(f'The item with the name {item_name} does not exist in this room!')
                return
            self.add_item(it)
            self.current_room.remove_item(it)
            it.on_take()
        elif verb == 'drop':
            if count_player == 0:
                print(f'The item with the name {item_name} is not in your collection!')
                return
            self.remove_item(it)
            self.current_room.add_item(it)
            it.on_drop()

    def print_items(self):
        if not self.items:
            print(f'{self.name} currently has no items')
            return
        print(f'{self.name} has the following items: ')
        for item in self.items:
            print(item)

