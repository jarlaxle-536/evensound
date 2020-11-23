from .loader import *

class Sound(Entity):
    pitch = None
    duration = DEFAULT_QUANTIZATION_PARAMETER
    fields = ['pitch', 'duration']
    def __lt__(self, other):
        if isinstance(other, Sound):
            return self.index <= other.index
    @property
    def note(self):
        return self.get_note_repr()
    def get_note_repr(self, tonality=None):
        """In English notation"""
        if self.pitch is None: return 'R'
        v1 = NOTES[self.pitch % 12]
        # check tonality here
        v1 = v1[0]
        v2 = self.pitch // 12 - 1
        return f'{v1}{v2}'
    def __str__(self):
        return f'<SOUND n={self.note} t={self.duration}>'
