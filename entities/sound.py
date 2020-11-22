from .loader import *

class Sound(Entity):
    track = None
    beat = None
    start_index = 1
    duration = DEFAULT_QUANTIZATION_PARAMETER
    pitch = None
    fields = [
        'track',
        'beat',
        'start_index',
        'duration',
        'pitch'
    ]
    @property
    def note(self):
        return get_note_repr(self.pitch) if self.pitch is not None else 'R'
    @property
    def end_index(self):
        return self.start_index + self.duration
    def __str__(self):
        return f'<SOUND i={self.start_index} t={self.track} p={self.pitch} d={self.duration}>'
    def __lt__(self, other):
        if isinstance(other, Sound):
            return self.index <= other.index

def get_note_repr(pitch_code, tonality=None):
    """In English notation"""
    v1 = NOTES[pitch_code % 12]
    # check tonality here
    v1 = v1[0]
    v2 = pitch_code // 12 - 1
    return f'{v1}{v2}'
