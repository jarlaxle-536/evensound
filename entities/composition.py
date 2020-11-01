from .general import *
from .track import *
from .beat import *

from gui.updaters import TrackListUpdater

class Composition(Entity):

    tracks = TrackListUpdater(source=list())

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
