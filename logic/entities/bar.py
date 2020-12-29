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
    def get_commands_list(self):
        res = list()
        time_factor = self.duration / 16
        for note in self.notes:
            heapq.heappush(res, (
                time_factor * note.start_position,
                MIDICommand(**{'type': 'note_on', 'pitch': note.pitch})
                )
            )
            heapq.heappush(res, (
                time_factor * note.ending_position,
                MIDICommand(**{'type': 'note_off', 'pitch': note.pitch})
                )
            )
        return res
    @property
    def duration(self):
        return 4 * self.time_signature.ratio
    def __str__(self):
        return f'<Bar t={self.tempo} [{self.time_signature}]>'

class BarContainer(Container):
    _cls = Bar

class MIDICommand(Entity):
    _fields = ['type', 'pitch']
    def update(self):
        super().update()
        self.output = self._Player.object().midi_output
    def execute(self):
        getattr(self.output, self.type)(self.pitch, 127)
    def __lt__(self, other):
        assert isinstance(other, MIDICommand)
        return True
