from logic.loader import *

from .container import *
from logic.functions import *

class Note(Entity):
    _fields = ['pitch', 'quantized_duration', 'start_position']
    pitch = -1
    quantized_duration = 4
    start_position = 0
    def __str__(self):
        return f'<Note p={self.pitch} d={self.quantized_duration} s={self.start_position}>'
    @property
    def ending_position(self):
        return self.start_position + self.quantized_duration
    @property
    def notation_repr(self):
        dct = get_notation_for_pitch(self.pitch)
        return f'{dct["notes"][0]}{dct["octave"]}'

class NoteContainer(Container):
    _classes = [Note, ]
