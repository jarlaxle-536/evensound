import shelve

from .composition import *
from .persistent import *

class State(Persistent):
    db_fields = ['composition', ]
    def setup(self, **kwargs):
        self.composition = Composition()
    def save(self, filepath):
#        print(f'will save {self.__dict__} under {filepath}')
        with shelve.open(filepath, 'n', writeback=True) as file:
            file['state'] = self
    def load(self, filepath):
#        print(f'will load state from {filepath}')
        with shelve.open(filepath, 'r') as file:
            self = file['state']
