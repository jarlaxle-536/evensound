from logic.loader import *

from .new_composition_action import *
from .save_composition_action import *
from .open_composition_action import *
from .exit_action import *

class FileMenu(QMenuMixin):
    title = 'File'
    actions_list = [
        NewCompositionAction,
        SaveCompositionAction,
        OpenCompositionAction,
        ExitAction,
    ]
