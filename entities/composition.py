from auxiliary import *

from .persistent import *
from .general import *
from .track import *
from .beat import *

class Composition(Persistent):

    title = None
    tracks = list()

    def setup(self):
        self.add_track()
        self.beats = [Beat(), ]

    @property
    def number_of_tracks(self):
        return len(self.tracks)

    def add_track(self, **kwargs):
        kwargs['composition'] = self
        track_obj = Track(**kwargs)
        self.tracks += [track_obj]

    def __str__(self):
        return str(self.title)
