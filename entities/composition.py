from auxiliary import *

from .general import *
from .track import *
from .beat import *

class Composition(Root):

    fields = [
        'title',
    ]
    title = 'Composition'
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
