# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'{self.name}, {self.current_room}'

    def _set_name_(self, name):
        self._name = name

    def _get_name_(self):
        return self._name

    def _set_room_(self, current_room):
        self._current_room = current_room

    def _get_room_(self):
        return self._current_room

    name = property(_get_name_, _set_name_)
    current_room = property(_get_room_, _set_room_)