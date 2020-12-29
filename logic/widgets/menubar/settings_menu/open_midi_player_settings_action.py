from logic.loader import *

from logic.widgets.dialogs import *

class OpenMidiPlayerSettingsAction(QAction):
    text = 'MIDI player'
    def setup(self):
        super().setup()
        self.adapt(MidiPlayerSettingsDialog(), name='dialog')
    def action(self):
        self.dialog.show()
