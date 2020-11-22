from .loader import *

class TrackSelector(Singleton, CompositionConnected):
    track_index = 1
    fields = [
        'track_index'
    ]
    @property
    def track(self):
        return self.composition.tracks[self.track_index]
    def change_index(self, index):
        valid_indices = (1, len(self.composition.tracks))
        self.track_index = index if valid_indices[0] <= index <= valid_indices[1]\
            else self.track_index
