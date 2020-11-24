from .loader import *

class Sound(Entity):

    pitch = None
    duration = DEFAULT_QUANTIZATION_PARAMETER
    track = None
    beat = None
    start_index = 1
    fields = ['pitch', 'duration', 'track', 'beat', 'start_index']

    @property
    def note(self):
        return self.get_note_repr()

    def get_note_repr(self, tonality=None):
        """English notation"""
        if self.pitch is None: return 'R'
        v1 = NOTES[self.pitch % 12]
        # check tonality here
        v1 = v1[0]
        v2 = self.pitch // 12 - 1
        return f'{v1}{v2}'

    @property
    def end_index(self):
        return self.start_index + self.duration

    def __lt__(self, other):
        if isinstance(other, Sound):
            values = (
                [self.beat.position, other.beat.position],
                [self.start_index, other.start_index]
            )
            if not None in values[0]:
                if len(set(values[0])) != 1:
                    return values[0][0] < values[0][1]
                else:
                    return values[1][0] < values[1][1]

    def __str__(self):
        return f'<SOUND t={self.track} b={self.beat} n={self.note} s={self.start_index} d={self.duration}>'
