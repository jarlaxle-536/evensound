from .new_file_action import *
from .edit_file_action import *
from .open_file_action import *
from .save_file_action import *
from .exit_action import *

class FileMenu(QMenuMixin):
    title = 'File'
    actions_list = [
        NewFileAction,
        EditFileAction,
        OpenFileAction,
        SaveFileAsAction,
        ExitAction
    ]
