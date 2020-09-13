# Implement a class to hold room information. This should have name and description attributes.

from lightsource import LightSource

class Room:
    def __init__(self, name, description, is_light, items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.is_light = is_light  # Stretch: True if room is naturally lite, False if not
        self.items = items
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.n_to = None

    def __str__(self):
        return f'{self.name}\n\t- description: {self.description}'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    # Function prints all the items in a room
    def print_items(self):
        if not self.items:
            print(f'The {self.name} currently has no items.')
            return
        print(f'The {self.name} has the following items: ')
        for item in self.items:
            print(item)









