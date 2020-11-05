import mido

output_midi = mido.MidiFile()
track = mido.MidiTrack()

msg = mido.Message('note_on', note=42)

msg.copy(channel=2)
track.append(msg)
output_midi.tracks.append(track)

output_midi.save('test_mid.mid')
