from logic.loader import *

class MidiPlayerSettingsDialog(QDialog):
    title = 'MIDI player settings'
    _widgets = [
        'BlaLabel',
    ]

class BlaLabel(QLabel):
    text = 'some text'
