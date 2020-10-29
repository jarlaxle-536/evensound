import shelve

from .composition import *

class State:
    def __init__(self, **kwargs):
        self.composition = Composition()
    def save(self, filepath):
        with shelve.open(filepath, 'n', writeback=True) as file:
            file['state'] = self
    def load(self, filepath):
        with shelve.open(filepath, 'r') as file:
            loaded = file['state']
        for k, v in loaded.__dict__.items():
            setattr(self, k, v)
