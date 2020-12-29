import random

from logic.loader import *

from logic.entities import *

class AlterButton(QPushButton):
    text = 'Alter'
    def action(self):
        current_bar = list(self._Bar._instances.values())[0]
        current_bar.notes = NoteContainer()
        quant_dur = Note.quantized_duration / 16
        ratio = current_bar.time_signature.ratio
        number_of_notes = int(ratio/quant_dur)
        print(f'number of notes: {number_of_notes}')
        for i in range(number_of_notes):
            note = Note(
                pitch=random.randint(30, 60),
                start_position=i*Note.quantized_duration
            )
            print(note)
            current_bar.notes.insert(note)
