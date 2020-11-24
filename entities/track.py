from .loader import *

from .instrument import *
from .beat import *

class Track(Entity, CompositionConnected):
    
    name = 'Track'
    fields = [
        'name',
        'instrument_program_code'
    ]
    instrument_program_code = Instrument.program_code

    def setup(self):
        self.instrument = Instrument(program_code=self.instrument_program_code)

    @staticmethod
    def create_track_name(index, instrument_name):
        return f'Track #{index}'

    def __str__(self):
        return f'<TRACK "{self.name}" [{self.instrument}]>'
