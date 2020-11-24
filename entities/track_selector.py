from .loader import *

@singleton_register('Composition')
class TrackSelector(Singleton):
    track_index = 1
    fields = [
        'track_index'
    ]
    @property
    def track(self):
        return self.Composition.tracks[self.track_index]
    def change_index(self, index):
        valid_indices = (1, len(self.Composition.tracks))
        self.track_index = index if valid_indices[0] <= index <= valid_indices[1]\
            else self.track_index
