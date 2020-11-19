from .loader import *

from .persistent import *
from .track import *

class Composition(Singleton, Persistent):

    title = 'Composition title'
    fields = ['title']
    tracks = list()

    def setup(self):
        print(f'{self.__class__.__name__} title is {self.title.upper()}')
        self.insert_track()

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
        return Track.create_track_name(index, track_obj.instrument.name)

    def __str__(self):
        return str(self.title)

    @staticmethod
    def get_id(dct):
        print(f'composition get id with {dct}')
        return dct.get('title', Composition.title)
