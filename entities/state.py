import shelve

from .composition import *

class State(Root):
    def setup(self, **kwargs):
        self.composition = Composition()
