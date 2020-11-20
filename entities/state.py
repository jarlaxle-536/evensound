from .loader import *

from .persistent import *
from .composition import *
from .cursor import *

class State(Singleton, Persistent):
    db_fields = ['composition', ]
    def setup(self):
        self.composition = Composition()
        self.cursor = Cursor()
        print(f'{self}, {self.composition}, {self.cursor}')
    def save(self, filepath):
#        print(f'will save {self.__dict__} under {filepath}')
        with shelve.open(filepath, 'n', writeback=True) as file:
            file['state'] = self
    def load(self, filepath):
#        print(f'will load state from {filepath}')
        with shelve.open(filepath, 'r') as file:
            self = file['state']
    def set_composition(self, composition):
        self.composition = composition
    @staticmethod
    def get_id(dct):
        print(f'state get id with {dct}')
        return 1

class StateMixin(Root):
    def setup(self):
        self.state = State()
