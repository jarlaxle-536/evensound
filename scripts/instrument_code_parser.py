import json
import os

data_dirpath = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'data')
midi_codes_filepath = os.path.join(data_dirpath, 'midi_codes.txt')
target_filepath = os.path.join(data_dirpath, 'midi_codes.json')

with open(midi_codes_filepath) as file:
    text = file.read().replace('\"', '')

instruments_dict = dict()
splitted = text.split('\n\n')

for piece in splitted:
    first, *other = piece.strip().split('\n')
    title = first.strip().replace(':', '')
    crr_dict = instruments_dict[title] = dict()
    for tabbed in other:
        code, name = tabbed.strip().split('\t')
        crr_dict[code] = name

if os.path.exists(target_filepath):
    os.remove(target_filepath)

with open(target_filepath, 'a') as file:
    json.dump(instruments_dict, file, indent=2)
