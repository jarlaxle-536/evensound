import time

from entities.loader import *

from entities.sound import *

class Composition(Singleton):

    title = 'Composition title'
    beats = list()
    tracks = list()

#    def setup(self):
#        self.insert_track()
#        self.insert_beat()

    def insert_track(self, position=None, *args, **kwargs):
        track_obj = Track(**kwargs)
        self.tracks = insert_into_list(self.tracks, track_obj, position)

    def insert_beat(self, position=None, *args, **kwargs):
        beat_obj = Beat(**kwargs)
        self.beats = insert_into_list(self.beats, beat_obj, position)

    def create_midi(self):
        pass

    def __str__(self):
        return f'<COMPOSITION "{self.title}" n_tracks={len(self.tracks)} n_beats={len(self.beats)}>'

class Instrument(Entity):

    program_code = 1
    fields = [
        'program_code',
    ]
    midi_codes = MIDI_CODES.copy()

    @property
    def name(self):
        return MIDI_CODES_FLATTENED.get(str(self.program_code))

    @staticmethod
    def find_program_code_by_name(name):
        return (lambda l: int(l[0]) if l else None)(
            [k for k, v in MIDI_CODES_FLATTENED.items() if v == name])

    def __str__(self):
        return f'{self.name}'

class Track(Entity, CompositionConnected):
    name = 'Track'
    fields = [
        'name',
        'instrument_program_code'
    ]
    instrument_program_code = Instrument.program_code

    def setup(self):
        self.instrument = Instrument(program_code=self.instrument_program_code)

    @staticmethod
    def create_track_name(index, instrument_name):
        return f'Track #{index}'

    def __str__(self):
        return f'<TRACK "{self.name}" [{self.instrument}]>'

class TimeSignature(Root):

    numerator = 4
    denominator = 4
    fields = [
        'numerator',
        'denominator'
    ]

    @property
    def ratio(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

class Beat(Entity, CompositionConnected):
    tempo = 120
    starting_index = None
    fields = [
        'starting_index',
        'tempo',
        'ts_numerator',
        'ts_denominator'
    ]
    ts_numerator = TimeSignature.numerator
    ts_denominator = TimeSignature.denominator
    quantization_parameter = MAX_QUANTIZATION_PARAMETER
    sounds = list()

    def setup(self):
        self.time_signature = TimeSignature(
            numerator=self.ts_numerator,
            denominator=self.ts_denominator
        )

    def insert_sound(self, position=None, *args, **kwargs):
        kwargs['beat'] = self
        sound_obj = Sound(**kwargs)
        self.sounds = self.sounds[:]
        heapq.heappush(self.sounds, sound_obj)

    @property
    def quantum_number(self):
        return int((self.time_signature.ratio) * self.quantization_parameter)

    @property
    def total_duration(self):
        return 120 / self.tempo * self.time_signature.ratio

    @property
    def quantum_duration(self):
        return self.total_duration / self.quantum_number

    def __str__(self):
        return f'<BEAT t={self.tempo} s={self.time_signature}>'

class Sound(Entity):

    pitch = None
    duration = DEFAULT_QUANTIZATION_PARAMETER
    track = None
    beat = None
    start_index = 1
    fields = ['pitch', 'duration', 'track', 'beat', 'start_index']

    @property
    def note(self):
        return self.get_note_repr()

    def get_note_repr(self, tonality=None):
        """In English notation"""
        if self.pitch is None: return 'R'
        v1 = NOTES[self.pitch % 12]
        # check tonality here
        v1 = v1[0]
        v2 = self.pitch // 12 - 1
        return f'{v1}{v2}'

    @property
    def end_index(self):
        return self.start_index + self.duration

    def __lt__(self, other):
        if isinstance(other, Sound):
            return self.start_index < other.start_index

    def __str__(self):
        return f'<SOUND t={self.track.name} b={self.beat.tempo} n={self.note} s={self.start_index} d={self.duration}>'

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
    number_of_tracks = random.randint(5, 25)
    number_of_beats = random.randint(5, 25)
    number_of_sounds = random.randint(25, 100)
    composition = Composition()
    for i in range(number_of_tracks):
        some_program_code = random.randint(1, 128)
        composition.insert_track(instrument_program_code=some_program_code)
    for i in range(number_of_beats):
        some_numerator = random.randint(2, 8)
        some_tempo = random.randint(100, 170)
        composition.insert_beat(tempo=some_tempo, ts_numerator=some_numerator)
    for i in range(number_of_sounds):
        some_track = random.choice(composition.tracks)
        some_beat = random.choice(composition.beats)
        some_start_index = random.randint(1, some_beat.quantum_number)
        some_duration = random.choice(QUANTIZATION_PARAMETERS)
        some_pitch = random.randint(24, 48)
        print(some_track, some_beat, some_start_index, some_duration, some_pitch)
        some_beat.insert_sound(pitch=some_pitch, track=some_track, start_index=some_start_index, duration=some_duration)
    return composition

def play(composition):
    print('will play composition')
    midi_output = list(MIDI_OUTPUTS.values())[1]
    midi_output.set_instrument(1)
    cmds_list = list()
#    midi = composition.create_midi()
    current_time = 0
    for b in composition.beats[:]:
        quantum_duration = b.quantum_duration
        while True:
            try:
                sound = heapq.heappop(b.sounds)
                sound_start_time = (sound.start_index - 1) * quantum_duration
                sound_end_time = (sound.end_index - 1) * quantum_duration
                heapq.heappush(cmds_list, (current_time + sound_start_time, 'note_on', sound.pitch, 127))
                heapq.heappush(cmds_list, (current_time + sound_end_time, 'note_off', sound.pitch, 127))
            except IndexError:
                break
        total_duration = b.total_duration
        current_time += total_duration
        print(current_time)
    print(cmds_list)
    current_time = 0
    delta = 10 ** (-2)
    pending = None
    while True:
        print(current_time)
        if pending is None:
            try:
                pending = heapq.heappop(cmds_list)
            except IndexError:
                break
        if pending[0] <= current_time:
            meth_name, *args = pending[1:]
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
