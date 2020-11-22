from .loader import *

from .persistent import *
from .track import *
from .beat import *

class Composition(Singleton, Persistent):

    title = 'Composition title'
    fields = [
        'title'
    ]
    tracks = list()
    beats = list()

    def setup(self):
        print(f'{self.__class__.__name__} title is {self.title.upper()}')
#        self.insert_track()
#        self.insert_beat()
#        self.tracks[0].insert_sound()

    @property
    def number_of_tracks(self):
        return len(self.tracks)

    def insert_track(self, position=None, *args, **kwargs):
        kwargs['composition'] = self
        track_obj = Track(**kwargs)
        self.tracks = insert_into_list(self.tracks, track_obj, position)
        if track_obj.name == Track.name:
            track_obj.name = self.get_default_name_for_track(track_obj)

    def get_default_name_for_track(self, track_obj):
        index = self.tracks.index(track_obj) + 1
        print(track_obj.__dict__)
        print(track_obj.instrument.__dict__)
        return Track.create_track_name(index, track_obj.instrument.name)

    def insert_beat(self, position=None, *args, **kwargs):
        kwargs['composition'] = self
        beat_obj = Beat(**kwargs)
        self.beats = insert_into_list(self.beats, beat_obj, position)

    def create_midi(self):
        pass

    def __str__(self):
        return str(self.title)
