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

    def move_rooms(self, direction, next_room):
        if next_room is None:
            print(f'You cannot move {direction} from the {self.current_room.name}.')
            print('Please try another direction.\n')
            return
        self.current_room = next_room
        print(f'You have moved {direction} to the {self.current_room}!')
        self.current_room.print_items()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def set_items(self, verb, item_name):
        affected_item = None

        for item in self.current_room.items:
            if item.name == item_name:
                affected_item = item

        for item in self.items:
            if item.name == item_name:
                affected_item = item

        count_player = self.items.count(affected_item)
        count_room = self.current_room.items.count(affected_item)

        if verb == 'get' or verb == 'take':
            if count_room == 0:
                print(f'The item with the name {item_name} does not exist in this room!\n')
                return
            self.add_item(affected_item)
            self.current_room.remove_item(affected_item)
            affected_item.on_take()
            print(f'You are currently in the {self.current_room}!')
            self.current_room.print_items()
        elif verb == 'drop':
            if count_player == 0:
                print(f'The item with the name {item_name} is not in your collection!\n')
                return
            self.remove_item(affected_item)
            self.current_room.add_item(affected_item)
            affected_item.on_drop()
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

