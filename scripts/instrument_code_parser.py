import json
import os

from config import *

def parser1():
    instruments_dict = dict()
    splitted = text.split('\n\n')
    for piece in splitted:
        first, *other = piece.strip().split('\n')
        title = first.strip().replace(':', '')
        crr_dict = instruments_dict[title] = dict()
        for tabbed in other:
            code, name = tabbed.strip().split('\t')
            crr_dict[code] = name
    return instruments_dict

def parser2():
    instruments_dict = dict()
    splitted = text.split('\n\n')
    for piece in splitted:
        first, *other = piece.strip().split('\n')
        title = first.strip().replace(':', '')
        for tabbed in other:
            code, name = tabbed.strip().split('\t')
            instruments_dict[code] = name
    return instruments_dict

txt_filepath = os.path.join(DATA_DIR, 'midi_codes.txt')
json_filepath = os.path.join(DATA_DIR, 'midi_codes.json')

with open(txt_filepath) as file:
    text = file.read().replace('\"', '')

result = parser2()

if os.path.exists(json_filepath):
    os.remove(json_filepath)

with open(json_filepath, 'a') as file:
    json.dump(result, file, indent=2)
