from logic.loader import *

from .track import *
from .bar import *

class Composition(Singleton):
    _fields = ['title']
    title = 'Composition title'
    def setup(self):
        self.adapt(self._TrackContainer(), name='tracks')
        self.adapt(self._BarContainer(), name='bars')
        self.tracks.insert(0, self._Track())
        self.bars.insert(0, self._Bar())
        super().setup()
