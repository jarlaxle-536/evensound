import mido
import pygame

output_midi = mido.MidiFile()
track = mido.MidiTrack()

output = mido.open_output('TiMidity:TiMidity port 0 128:0')
msgs = [
    mido.Message('note_on', note=42),
    mido.Message('note_on', note=48),
    mido.Message('note_on', note=54),
]

for msg in msgs:
    track.append(msg)
    output.send(msg)
output_midi.tracks.append(track)

filepath = 'test_mid.mid'

output_midi.save(filepath)

pygame.init()
pygame.mixer.music.load(filepath)
pygame.mixer.music.play()

print(mido.get_output_names())

print(output.__dict__)

mid = mido.MidiFile(filepath)
for msg in mid.play():
    output.send(msg)

with output:
    for msg in output_midi.play():
        output.send(msg)
