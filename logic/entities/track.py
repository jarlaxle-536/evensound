from logic.loader import *

from .instrument import *
from .container import *

class Track(Entity):
    name = 'Track'
    def setup(self):
        super().setup()
        self.adapt(Instrument(), name='instrument')
    def __str__(self):
        return f'{self.name} [{self.instrument}]'

class TrackContainer(Container):
    _cls = Track
