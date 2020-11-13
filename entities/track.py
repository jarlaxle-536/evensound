from .general import *
from .instrument import *

class Track(Entity):
    fields = ['name', 'composition']
    name = 'Track'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.name == self.__class__.name:
            self.name = self.default_name
#        self.__dict__.setdefault('name', self.default_name)
        self.instrument = Instrument(**kwargs)

    def __str__(self):
        return f'{self.name}'

    @property
    def default_name(self):
        return f'Track #{self.composition.number_of_tracks + 1} [{self.instrument.name}]'

    @staticmethod
    def get_id(dct):
        return dct.get('name', 0)
