from .track import *
from .beat import *

class Composition:
    def __init__(self, **kwargs):
        self.tracks = [
            Track(),
            Track(instrument_code=2) 
        ]
        self.beats = [Beat(), ]
