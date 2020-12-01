import logic._02_file_menu

from .persistent import *

class State(logic._02_file_menu.State, Persistent):
    def save(self, filepath):
        print(f'saving to {filepath}')
        with shelve.open(filepath, 'n', writeback=True) as file:
            file['state'] = self
    def load(self, filepath):
        print(f'loading from {filepath}')
        with shelve.open(filepath, 'r') as file:
            self = file['state']
