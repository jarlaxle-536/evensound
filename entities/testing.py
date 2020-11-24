import time
import mido

from entities.loader import *

from entities.composition import *

def intro(composition):
    sep = '  '
    print('Composition:')
    print(f'{sep}{composition}')
    tracks = composition.tracks
    print('Tracks:')
    for t in tracks:
        print(f'{sep}{t}')
    beats = composition.beats
    sounds = list()
    print('Beats:')
    for b in beats:
        print(f'{sep}{b}')
        sounds += b.sounds
    print('Sounds:')
    for s in sounds:
        print(f'{sep}{s}')

def create_randomly():
    number_of_tracks = random.randint(3, 8)
    number_of_tracks = 3
    program_codes = [30, 16, 35]
    number_of_beats = random.randint(10, 30)
    number_of_sounds = random.randint(200, 500)
    composition = Composition()
    for i in range(number_of_tracks):
        some_program_code = random.randint(1, 128)
        some_program_code = program_codes[i]
        composition.insert_track(instrument_program_code=some_program_code)
    for i in range(number_of_beats):
        some_numerator = random.randint(2, 8)
        some_tempo = random.randint(100, 170)
        composition.insert_beat(tempo=some_tempo, ts_numerator=some_numerator)
    for i in range(number_of_sounds):
        some_track = random.choice(composition.tracks)
        some_beat = random.choice(composition.beats)
        some_start_index = 4 * random.randint(1, some_beat.quantum_number // 4)
        some_duration = random.choice(QUANTIZATION_PARAMETERS)
        scale = [0, 2, 1, 2, 2, 1, 2, 2]
        acc_scale = [0]
        for s in scale:
            acc_scale += [acc_scale[-1] + s]
        allowed_notes = sorted(set([36 + 12 * i + acc_scale[j] for i in range(4) for j in range(len(acc_scale))]))
        some_pitch = random.randint(36, 120)
        some_pitch = random.choice(allowed_notes)
        print(some_track, some_beat, some_start_index, some_duration, some_pitch)
        some_beat.insert_sound(pitch=some_pitch, track=some_track, start_index=some_start_index, duration=some_duration)
    return composition

def play(composition):
    print('will play composition')
    midi_output = list(MIDI_OUTPUTS.values())[1]
    midi_output.set_instrument(1)
    cmds_list = list()
    test_midi_output(midi_output)
#    midi = composition.create_midi()
    current_time = 0
    for b in composition.beats[:]:
        quantum_duration = b.quantum_duration
        for sound in b.sounds:
            sound_start_time = (sound.start_index - 1) * quantum_duration
            sound_end_time = (sound.end_index - 1) * quantum_duration
#            heapq.heappush(cmds_list, (current_time + sound_start_time, 'set_instrument', sound.track))
            heapq.heappush(cmds_list, (current_time + sound_start_time, 'note_on', sound.pitch, 127))
            heapq.heappush(cmds_list, (current_time + sound_end_time, 'note_off', sound.pitch, 127))
        total_duration = b.total_duration
        current_time += total_duration
    test_midi_file = 'test_mid.mid'
    if os.path.exists(test_midi_file):
        os.remove(test_midi_file)
    midi_file = mido.MidiFile()
    tracks_dict = {
        track: mido.MidiTrack()
            for track in composition.tracks
    }
    for track_obj, mido_track in tracks_dict.items():
        mido_track.append(mido.Message('program_change',
            program=track_obj.instrument.program_code, time=0))
    current_time = 0
    for b in composition.beats:
        quantum_duration = b.quantum_duration
        for s in b.sounds:
            mido_track = tracks_dict.get(s.track)
            mido_track.append(mido.Message(
                'note_on',
                note=s.pitch,
                velocity=127,
                time = int(32 * (current_time + (s.start_index - 1) * quantum_duration))))
            mido_track.append(mido.Message(
                'note_off',
                note=s.pitch,
                velocity=127,
                time = int(32 * (current_time + (s.end_index - 1) * quantum_duration))))
        total_duration = b.total_duration
        current_time += total_duration
    for mido_track in tracks_dict.values():
        midi_file.tracks.append(mido_track)
    midi_file.save(test_midi_file)
    return

    current_time = 0
    delta = 10 ** (-2)
    pending = None
    while True:
#        print(current_time)
        if pending is None:
            try:
                pending = heapq.heappop(cmds_list)
            except IndexError:
                break
        if pending[0] <= current_time:
            meth_name, *args = pending[1:]
            if meth_name == 'set_instrument':
                args[0] = args[0].instrument.program_code
            getattr(midi_output, meth_name).__call__(*args)
            pending = None
        time.sleep(delta)
        current_time += delta
#        print(', '.join(map(str, b.sounds)))
#        print(dir(heapq))
#        beat_sounds = heapq.heapsort(b.sounds)
#    pitch_code = 42
#    midi_output.set_instrument(30)
#    midi_output.note_on(pitch_code, 127)
#    time.sleep(0.1)
#    midi_output.note_off(pitch_code, 127)

cmp = create_randomly()
intro(cmp)
play(cmp)
