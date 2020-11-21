from .loader import *

from .instrument import *
from .beat import *

class Track(Entity):

    fields = [
        'composition',
        'instrument_program_code',
        'name',
    ]
    name = None
    composition = None
    instrument_program_code = Instrument.program_code
    sounds = list()

    def setup(self):
        self.instrument = Instrument(program_code=self.instrument_program_code)

    def __str__(self):
        return f'{self.name}'

    def insert_sound(self, position=None, *args, **kwargs):
        kwargs['beat'] = self
        sound_obj = Sound(**kwargs)
        self.sounds = self.sounds[:]
        heapq.heappush(self.sounds, sound_obj)

    @staticmethod
    def get_id(dct):
        return dct.get('name', 0)

    @staticmethod
    def create_track_name(index, instrument_name):
        return f'Track #{index}'
