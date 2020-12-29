import pygame.midi

from logic.functions.midi.get_midi_output_info import *

def detect_midi_outputs():
    print('Detecting MIDI outputs')
    midi_outputs = list()
    for dev_num in range(pygame.midi.get_count()):
        try:
            current_output = pygame.midi.Output(dev_num)
            info = get_midi_output_info(current_output)
            dct = {
                'dev_num': dev_num,
                'output_obj': current_output,
                'info': info
            }
            midi_outputs += [dct]
        except Exception as exc:
            pass
    return midi_outputs

if __name__ == '__main__':
    detect_midi_outputs()
