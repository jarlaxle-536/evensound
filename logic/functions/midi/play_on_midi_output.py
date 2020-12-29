import time
import pygame.midi

def play_on_midi_output(midi_output):
    pitch_code = 32
    midi_output.set_instrument(1)
    midi_output.note_on(pitch_code, 127)
    time.sleep(0.1)
    midi_output.note_off(pitch_code, 127)
