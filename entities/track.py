from .general import *
from .instrument import *

class Track(Root):
    fields = ['name', 'composition']
    name = 'Track'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.name == self.__class__.name:
            self.name = self.default_name
#        self.__dict__.setdefault('name', self.default_name)
        self.instrument = Instrument(**kwargs)

    def __str__(self):
        return f'{self.name} [{self.instrument.name_expanded}]'

    @property
    def default_name(self):
        return f'Track #{self.composition.number_of_tracks + 1}'
