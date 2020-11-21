from logic.loader import *

class MidiOutputRowLabel(FormRowLabelMixin):
    name = 'MIDI output'

class MidiOutputRowInput(QLineEditMixin):
    def setup(self):
        self.entered_text = self.application.state.composition.title
        super().setup()

class MidiOutputComboBox(QComboBoxMixin):
    def setup(self):
        self.player = Singleton.find('Player')
        self.options = [pygame.midi.get_device_info(out.device_id)[1].decode('utf-8')
            for out in self.player.midi_outputs.values()]
        super().setup()
    def on_change(self, new_index):
        device_number = list(self.player.midi_outputs)[new_index]
        self.player.midi_device_number = device_number
        self.player.update()
        super().action()

class MidiOutputRow(FormRowMixin):
    label_class = MidiOutputRowLabel
    input_class = MidiOutputComboBox

class TestMidiOutputButton(QPushButtonMixin):
    text = 'Test sound'
    def action(self):
        current_output = self.application.state.player.midi_output
        play_on_midi_output(current_output)
        super().action()

class MidiSettingsDialogOKButton(QPushButtonMixin):
    text = 'OK'
    def action(self):
        dialog = self.find('MidiSettingsDialog')
        dialog.close()
        super().action()

class MidiSettingsWidget(QWidgetMixin, FormDataMixin):
    contents = {cls.__name__: cls for cls in [
        MidiOutputRow,
        TestMidiOutputButton,
        MidiSettingsDialogOKButton
    ]}

class MidiSettingsDialog(QDialogMixin):
    title = 'MIDI settings'
    central_widget = MidiSettingsWidget
