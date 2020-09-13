

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'\t- Item: {self.name}\n\t\t description: {self.description}'

    # Function called when player retrieves an item in a room that is naturally lite or a light source exist in the room
    def on_take(self):
        print(f'You have picked up the {self.name}!')

    # Function called when player drops an item in a room that is not a light source
    def on_drop(self):
        print(f'You have dropped the {self.name}!')