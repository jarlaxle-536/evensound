from .general import *
from .track import *
from .beat import *

class Composition(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tracks = [Track(), ]
        self.beats = [Beat(), ]
