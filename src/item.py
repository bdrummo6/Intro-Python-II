

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'\t- name: {self.name}\n\t\t description: {self.description}'
