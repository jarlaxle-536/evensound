from auxiliary import *

from .persistent import *
from .general import *
from .track import *
from .beat import *

class Composition(Entity):

    title = 'Composition title'
    fields = ['title']
    tracks = list()

    def setup(self):
        print(f'{self.__class__.__name__} title is {self.title.upper()}')
        self.add_track()
        self.beats = [Beat(), ]

    @property
    def number_of_tracks(self):
        return len(self.tracks)

    def add_track(self, **kwargs):
        print('Adding track to composition')
        kwargs['composition'] = self
        track_obj = Track(**kwargs)
        print(f'Track object: {track_obj.__dict__}')
        print(f'Instrument object: {track_obj.instrument.__dict__}')
        self.tracks += [track_obj]

    def __str__(self):
        return str(self.title)

    @staticmethod
    def get_id(dct):
        print(f'composition get id with {dct}')
        return 1
