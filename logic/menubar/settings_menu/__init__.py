from .open_midi_settings_dialog_action import *

class SettingsMenu(QMenuMixin):
    title = 'Settings'
    actions_list = [
        OpenMidiSettingsDialogAction,
    ]
