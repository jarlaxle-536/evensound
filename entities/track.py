import random

from .general import *
from .instrument import *

class Track(Entity):
    name = 'Track'
    fields = [
        'name',
    ]
    def __init__(self, **kwargs):
        kwargs.setdefault('name', f'track #{random.randint(1, 10000)}')
        super().__init__(**kwargs)
        self.instrument = Instrument(**kwargs)
