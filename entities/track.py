import random

from .instrument import *

class Track:
    name = 'Track'
    def __init__(self, **kwargs):
        self.instrument = Instrument()
        kwargs.setdefault('name', f'track #{random.randint(1, 10000)}')
        self.__dict__.update(kwargs)
        if 'instrument_code' in kwargs:
            self.instrument.__dict__.setdefault('code', kwargs['instrument_code'])
