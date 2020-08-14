# Implement a class to hold room information. This should have name and description attributes.

class Room:
    def __init__(self, name, description, items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.items = items
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.n_to = None

    def __str__(self):
        return f'{self.name}\n\t- description: {self.description}'



