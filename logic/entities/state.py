from logic.loader import *

from .composition import *

class State(Singleton):
    def setup(self):
        self.adapt(self._Composition(), name='composition')
        super().setup()
