from logic.loader import *

from logic.dialogs.midi_settings_dialog import *

class OpenMidiSettingsDialogAction(QActionMixin):
    text = 'MIDI'
    def action(self):
        dialog = MidiSettingsDialog()
