from .general import *
from .instrument import *

class Track(Entity):
    name = 'Track'
    fields = [
        'name',
    ]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.setdefault('instrument', Instrument(**kwargs))
        self.__dict__.setdefault('name', self.default_name)

    @property
    def default_name(self):
        return f'Track {self.composition.number_of_tracks + 1}'
