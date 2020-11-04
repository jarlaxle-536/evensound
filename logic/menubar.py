from gui import *
from .actions import *

class NewFileAction(QActionMixin):
    text = 'New file'

class OpenFileAction(QActionMixin):
    text = 'Open file'

class SaveFileAsAction(QActionMixin):
    text = 'Save file'

class ExitAction(QActionMixin):
    text = 'Exit'

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

class DeleteTrackAction(QActionMixin):
    text = 'Delete'

class TrackPropertiesAction(QActionMixin):
    text = 'Properties'

class TrackMenu(QMenuMixin):
    title = 'Track'
    actions_list = [
        AddTrackAction,
        DeleteTrackAction,
        TrackPropertiesAction
    ]
