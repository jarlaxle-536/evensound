from logic._02_file_menu.source import file_menu as fm_without_saveload

from .loader import *
from .save_composition_action import *
from .open_composition_action import *

class FileMenu(fm_without_saveload.FileMenu):
    actions_list = fm_without_saveload.FileMenu.actions_list + [
        SaveCompositionAction,
        OpenCompositionAction
    ]
