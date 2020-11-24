from .loader import *

from .persistent import *
from .track import *
from .beat import *

class Composition(Singleton):

    title = 'Composition title'
    fields = ['title']
    beats = list()
    tracks = list()

    def insert_track(self, position=None, *args, **kwargs):
        track_obj = Track(**kwargs)
        self.tracks = insert_into_list(self.tracks, track_obj, position)
        return track_obj

    def insert_beat(self, position=None, *args, **kwargs):
        beat_obj = Beat(**kwargs)
        self.beats = insert_into_list(self.beats, beat_obj, position)
        if position is not None:
            for beat in self.beats[position + 1:]:
                del beat._position
        return beat_obj

    def remove_beat(self, position):
        self.beats = remove_from_list(self.beats, position)
        for beat in self.beats[position:]:
            del beat._position

    def create_midi(self):
        pass

    def __str__(self):
        return f'<COMPOSITION "{self.title}" n_tracks={len(self.tracks)} n_beats={len(self.beats)}>'
