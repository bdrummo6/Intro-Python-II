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

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        if self.items == []:
            print(f'{self.name} currently has no items')
            return
        print(f'{self.name} has the following items: ')
        for item in self.items:
            print(item)
