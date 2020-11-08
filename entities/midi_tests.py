import mido

output_midi = mido.MidiFile()
track = mido.MidiTrack()

output = mido.open_output('TiMidity:TiMidity port 0 128:0')
msg1 = mido.Message('program_change', program=31)
msg2 = mido.Message('note_on', note=42)
msg3 = mido.Message('note_off', note=42)

#msg2.copy(channel=2)
for m in [msg1, msg2, msg3]:
    track.append(m)
    output.send(m)
output_midi.tracks.append(track)

output_midi.save('test_mid.mid')

print(mido.get_output_names())

print(output.__dict__)
