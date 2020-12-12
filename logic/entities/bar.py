from logic.loader import *

from .time_signature import *
from .container import *

class Bar(Entity):
    tempo = 120
    def setup(self):
        super().setup()
        self.adapt(self._TimeSignature(), name='time_signature')
    def __str__(self):
        return f'<Bar t={self.tempo} [{self.time_signature}]>'

class BarContainer(Container):
    _classes = [Bar, ]
