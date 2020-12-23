from logic.loader import *

from .track import *
from .bar import *

class Composition(Singleton):
    _fields = ['title']
    title = 'Composition title'
    def setup(self):
        self.adapt(TrackContainer(), name='tracks')
        self.adapt(BarContainer(), name='bars')
        self.tracks.insert(0, Track())
        self.bars.insert(0, Bar())
        super().setup()
