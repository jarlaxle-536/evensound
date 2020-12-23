from logic.loader import *

from .composition import *
from .cursor import *

class State(Singleton):
    def setup(self):
        self.adapt(Composition(), name='composition')
#        self.adapt(Cursor(), name='cursor')
        super().setup()
