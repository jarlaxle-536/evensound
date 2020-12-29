import pygame.midi

from logic.functions.midi.get_midi_output_info import *

def detect_midi_outputs():
    print('Detecting MIDI outputs')
    midi_outputs = dict()
    for dev_num in range(pygame.midi.get_count()):
        try:
            current_output = pygame.midi.Output(dev_num)
            info = get_midi_output_info(current_output)
            midi_outputs[dev_num] = current_output
        except Exception as exc:
            pass
    for k, v in midi_outputs.items():
        print(k, v)
    return midi_outputs

if __name__ == '__main__':
    pygame.midi.init()
    detect_midi_outputs()
