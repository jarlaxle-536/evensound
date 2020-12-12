from .new_composition_action import *
from .exit_action import *

class FileMenu(QMenu):
    title = 'File'
    _widgets = [
        'NewCompositionAction',
        'ExitAction'
    ]
