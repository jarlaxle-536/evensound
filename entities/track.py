from .loader import *

from .instrument import *
from .beat import *

class Track(Entity):

    fields = ['name', 'composition']
    name = None
    composition = None
    beats = list()

    def setup(self):
        self.instrument = Instrument()

    def insert_beat(self, position=None, *args, **kwargs):
        kwargs['track'] =  self
        beat_obj = Beat(*args, **kwargs)
        self.beats = insert_into_list(self.beats, beat_obj, position)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_id(dct):
        return dct.get('name', 0)

    @staticmethod
    def create_track_name(index, instrument_name):
        return f'<Track #{index} [{instrument_name}]>'
