from .loader import *

from .sound import *

class Beat(Entity):
    fields = [
        'composition',
        'tempo'
    ]
    tempo = 120
    sounds = list()
    def setup(self):
        self.time_signature = TimeSignature()
    @staticmethod
    def get_id(dct):
        return random.getrandbits(128)
    def insert_sound(self, position=None, *args, **kwargs):
        kwargs['beat'] = self
        sound_obj = Sound(**kwargs)
        self.sounds = self.sounds[:]
        self.sounds = insert_into_list(self.sounds, sound_obj, position)
    def __str__(self):
        return f'<BEAT t={self.tempo}, {self.time_signature}>'

class TimeSignature(Root):
    fields = [
        'ts_numerator',
        'ts_denominator'
    ]
    ts_numerator = 4
    ts_denominator = 4
    def __str__(self):
        return f'{self.ts_numerator}/{self.ts_denominator}'
