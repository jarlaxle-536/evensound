import pygame.midi

def get_midi_output_info(midi_output):
    info = pygame.midi.get_device_info(midi_output.device_id)
    return info[1].decode('utf-8')
