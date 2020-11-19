from .loader import *

from .instrument import *
from .beat import *

class Track(Entity):
    fields = ['name', 'composition']
    name = 'Track'
    beats = list()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('after init:', self.__dict__)
        if self.name == self.__class__.name:
            print('default name:', self.default_name)
            self.name = self.default_name
        self.__dict__.setdefault('name', self.default_name)
        self.instrument = Instrument(**kwargs)
        self.insert_beat()

    def insert_beat(self, position=None, *args, **kwargs):
        kwargs['track'] =  self
        beat_obj = Beat(*args, **kwargs)
        self.beats = insert_into_list(self.beats, beat_obj, position)

    def __str__(self):
        return f'{self.name}'

    @property
    def default_name(self):
        if not self.composition is None:
            return f'Track #{self.composition.number_of_tracks + 1} [{self.instrument.name}]'
        return f'Unbounded track #{len(self.__class__.instances) + 1}'

    @staticmethod
    def get_id(dct):
        return dct.get('name', 0)
