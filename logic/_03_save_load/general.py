import logic._02_file_menu as added_file_menu
from logic._02_file_menu.source import *

from .source import *

class MainWindow(added_file_menu.MainWindow):
    menus = [
        FileMenu,
    ]

LOGIC_DICT = added_file_menu.LOGIC_DICT.copy()
LOGIC_DICT['main_window_class'] = MainWindow

print(LOGIC_DICT)
