from .new_composition_action import *
from .exit_action import *

class FileMenu(QMenu):
    _widgets = [
        'NewCompositionAction',
        'ExitAction'
    ]
    title = 'File'
