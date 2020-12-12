from logic.loader import *

from .track_container import *

class Composition(Singleton):
    _fields = ['title']
    title = 'Composition title'
    def setup(self):
        self.adapt(TrackContainer(), name='tracks')
