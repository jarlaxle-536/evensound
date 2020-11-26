import logic._02_file_menu

from .loader import *
from .save_composition_action import *
from .open_composition_action import *
from .exit_action import *

class FileMenu(logic._02_file_menu.FileMenu):
    actions_list = logic._02_file_menu.FileMenu.actions_list + [
        OpenCompositionAction,
        SaveCompositionAction,
        ExitAction
    ]
