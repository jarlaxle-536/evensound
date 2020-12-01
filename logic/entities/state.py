from logic.loader import *

from .composition import *
from .persistent import *

class State(Singleton, Persistent):
    def setup(self):
        self.composition = Composition()
    def save(self, filepath):
        print(f'saving to {filepath}')
        with shelve.open(filepath, 'n', writeback=True) as file:
            file['state'] = self
    def load(self, filepath):
        print(f'loading from {filepath}')
        with shelve.open(filepath, 'r') as file:
            self = file['state']
