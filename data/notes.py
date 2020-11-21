NOTES = [
    ['C'],
    ['C#', 'Db'],
    ['D'],
    ['D#', 'Eb'],
    ['E'],
    ['F'],
    ['F#', 'Gb'],
    ['G'],
    ['G#', 'Ab'],
    ['A'],
    ['A#', 'Bb'],
    ['B']
]

def get_note_repr(pitch_code, tonality=None):
    v1 = NOTES[pitch_code % 12]
    v1 = v1[0]
    v2 = pitch_code // 12 - 1
    return f'{v1}{v2}'

assert get_note_repr(21) == 'A0'
assert get_note_repr(25) == 'C#1'
assert get_note_repr(42) == 'F#2'
