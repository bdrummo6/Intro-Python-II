

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'\t- Item: {self.name}\n\t\t description: {self.description}'

    def on_take(self):
        print(f'You have picked up the {self.name}!')

    def on_drop(self):
        print(f'You have dropped the {self.name}!')