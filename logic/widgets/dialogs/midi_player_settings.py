from logic.loader import *

class MIDIPlayerSettingsDialog(QDialog):
    title = 'MIDI player settings'
    _widgets = [
        'SelectMIDIOutputWidget',
        'TestMIDIOutputButton',
    ]

class SelectMIDIOutputWidget(QComboBoxWithLabel):
    _text = 'Select MIDI output:'
    def setup(self):
        self._options = [(str(out), out)
            for out in self._Player.object().midi_outputs]
        super().setup()
    def set_selected(self, obj):
        super().set_selected(obj)
        self._Player.object().midi_output = obj

class TestMIDIOutputButton(QPushButton):
    text = 'Test MIDI output'
    def action(self):
        current_midi_output = self._Player.object().midi_output
        print(f'Will play smth on {self._Player.object().midi_output}')
