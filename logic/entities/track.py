from logic.loader import *

from .instrument import *
from .container import *

class Track(Entity):
    name = 'Track'
    def setup(self):
        super().setup()
        self.adapt(self._Instrument(), name='instrument')
    def __str__(self):
        return f'{self.name} [{self.instrument}]'

class TrackContainer(Container):
    _classes = [Track, ]
