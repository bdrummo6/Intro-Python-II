# Write a class to hold player information, e.g. what room they are in
# currently.

from lightsource import LightSource


class Player:
    def __init__(self, name, current_room, items=None):
        if items is None:
            items = []
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f'{self.name}, {self.current_room}'

    def move_rooms(self, direction, next_room):
        if next_room is None:
            print(f'You cannot move {direction} from the {self.current_room.name}.')
            print('Please try another direction.\n')
            return
        self.current_room = next_room
        print(f'You have moved {direction} to the {self.current_room}')
        for item in self.current_room.items:
            if isinstance(item, LightSource) or self.current_room.is_light:
                self.current_room.print_items()
                return
            for item_2 in self.items:
                if isinstance(item_2, LightSource):
                    self.current_room.print_items()
                    return
        print("It's pitch black!")

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

        if verb == 'get' or verb == 'take':
            if count_room == 0:
                print(f'The item with the name {item_name} does not exist in this room!')
                return
            if not isinstance(it, LightSource) and not self.current_room.is_light:
                print('Good Luck finding that in the dark!')
                return
            self.add_item(it)
            self.current_room.remove_item(it)
            it.on_take()
            print(f'You are currently in the {self.current_room}!')
            self.current_room.print_items()
        elif verb == 'drop':
            if count_player == 0:
                print(f'The item with the name {item_name} is not in your collection!')
                return
            self.remove_item(it)
            self.current_room.add_item(it)
            it.on_drop()
            print(f'You are currently in the {self.current_room}!')
            self.current_room.print_items()

    def print_items(self):
        if not self.items:
            print(f'You currently have no items in your inventory.\n')
            return
        print(f'You have the following items in your inventory: ')
        for item in self.items:
            print(item)
        print()
