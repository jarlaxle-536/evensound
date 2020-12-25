from logic.loader import *

from .time_signature import *
from .note import *
from .container import *

class Bar(Entity):
    tempo = 120
    def setup(self):
        super().setup()
        self.adapt(TimeSignature(), name='time_signature')
        self.adapt(NoteContainer(), name='notes')
    def __str__(self):
        return f'<Bar t={self.tempo} [{self.time_signature}]>'

class BarContainer(Container):
    _classes = [Bar, ]
