from logic.loader import *

from .composition import *
from .cursor import *

class State(Singleton):
    def setup(self):
        self.adapt(self._Composition(), name='composition')
        self.adapt(self._Cursor(), name='cursor')
        super().setup()
