from gui import *
from .handlers import *

class NewFileAction(QActionMixin):
    text = 'New file'
    def setup(self):
        super().setup()
        self.connect_to_func(new_composition_handler)

class OpenFileAction(QActionMixin):
    text = 'Open file'
    def setup(self):
        super().setup()
        self.connect_to_func(open_file_handler)

class SaveFileAsAction(QActionMixin):
    text = 'Save file'
    def setup(self):
        super().setup()
        self.connect_to_func(save_file_handler)

class ExitAction(QActionMixin): # done
    text = 'Exit'
    def setup(self):
        super().setup()
        self.connect_to_func(exit_application_handler)

class FileMenu(QMenuMixin):
    title = 'File'
    actions_list = [
        NewFileAction,
        OpenFileAction,
        SaveFileAsAction,
        ExitAction
    ]

class AddTrackAction(QActionMixin):
    text = 'Add'
    def setup(self):
        super().setup()
        self.connect_to_func(add_track_handler)

class DeleteTrackAction(QActionMixin):
    text = 'Delete'
    def setup(self):
        super().setup()
        self.connect_to_func(delete_track_handler)

class TrackPropertiesAction(QActionMixin):
    text = 'Properties'
    def setup(self):
        super().setup()
        self.connect_to_func(track_properties_handler)

class TrackMenu(QMenuMixin):
    title = 'Track'
    actions_list = [
        AddTrackAction,
        DeleteTrackAction,
        TrackPropertiesAction
    ]

class SettingsMenu(QMenuMixin):
    title = 'Settings'
