import json
from config import *

def get_notation_for_pitch(pitch_code):
    return {
        'notes': NOTES_ARRAY[pitch_code % 12],
        'octave': pitch_code // 12 - 1
    }

with open(os.path.join(DATA_DIR, 'notes.json')) as file:
    NOTES_ARRAY = json.load(file)

for p in [48, 64]:
    print(p, get_notation_for_pitch(p))
