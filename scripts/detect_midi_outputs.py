import pygame.midi
import time

class NoMidiOutput(pygame.midi.MidiException):
    def __init__(self, *args, **kwargs):
        self.message = 'No valid output midi devices detected.'
    def __str__(self):
        return self.message

def detect_midi_outputs():
    pygame.midi.init()
    pitch_code = 42
    valid_output_device_nums = list()
    total_device_num = pygame.midi.get_count()
    print(f'Total MIDI devices count: {total_device_num}')
    for dev_num in range(pygame.midi.get_count()):
        try:
            info = pygame.midi.get_device_info(dev_num)
            output = pygame.midi.Output(dev_num)
            output.set_instrument(30)
            output.set_instrument(30)
            output.note_on(pitch_code, 127)
            time.sleep(0.1)
            output.note_off(pitch_code, 127)
            valid_output_device_nums += [dev_num]
        except Exception as exc:
            pass
    if not valid_output_device_nums:
        raise NoMidiOutput()
    print(f'Valid MIDI devices count: {len(valid_output_device_nums)}')
    return valid_output_device_nums

if __name__ == '__main__':
    detect_midi_outputs()
