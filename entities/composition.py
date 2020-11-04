from .general import *
from .track import *
from .beat import *

class Composition(Entity):

    tracks = list()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_track()
        self.beats = [Beat(), ]

    @property
    def number_of_tracks(self):
        return len(self.tracks)

    def add_track(self, **kwargs):
        kwargs['composition'] = self
        track_obj = Track(**kwargs)
        self.tracks += [track_obj]
