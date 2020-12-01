from logic.loader import *

from .composition import *

class State(Singleton):
    def setup(self):
        self.composition = Composition()
