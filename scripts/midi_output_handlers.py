import pygame.midi
import time

class NoMidiOutput(pygame.midi.MidiException):
    def __str__(self):
        return 'No valid output midi devices detected.'

def detect_midi_outputs():
    global MIDI_OUTPUTS
    MIDI_OUTPUTS = dict()
    for dev_num in range(pygame.midi.get_count()):
        try:
            current_output = pygame.midi.Output(dev_num)
            test_midi_output(current_output)
            MIDI_OUTPUTS[dev_num] = current_output
        except Exception as exc:
            pass
    if not MIDI_OUTPUTS:
        raise NoMidiOutput()

def test_midi_output(midi_output):
    info = pygame.midi.get_device_info(midi_output.device_id)

def play_on_midi_output(midi_output):
    pitch_code = 64
    midi_output.set_instrument(0)
    midi_output.note_on(pitch_code, 127)
    time.sleep(0.1)
    midi_output.note_off(pitch_code, 127)

pygame.midi.init()

detect_midi_outputs()
