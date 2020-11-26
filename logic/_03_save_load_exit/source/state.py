import logic._02_file_menu

from .persistent import *

class State(logic._02_file_menu.State, Persistent):
    def save(self, filepath):
        with shelve.open(filepath, 'n', writeback=True) as file:
            file['state'] = self
    def load(self, filepath):
        with shelve.open(filepath, 'r') as file:
            self = file['state']
