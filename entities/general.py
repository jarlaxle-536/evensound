from auxiliary import *
from .state import *

class StateMixin(Root):
    """Adapting mixin for State, with additional .save and .load methods"""
    def setup(self):
        self.state = State()
    def save(self, filepath):
        print(f'will save {self.__dict__} under {filepath}')
        with shelve.open(filepath, 'n', writeback=True) as file:
            file['state'] = self.state
    def load(self, filepath):
        with shelve.open(filepath, 'r') as file:
            loaded = file['state']
        for k, v in loaded.__dict__.items():
            setattr(self.state, k, v)
