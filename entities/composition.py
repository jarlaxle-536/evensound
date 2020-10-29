from .track import *
from .beat import *

class Composition:
    def __init__(self, **kwargs):
        self.tracks = [Track(), ]
        self.beats = [Beat(), ]
