import logic._01_general_app as general_app

from .source.file_menu import *

class MainWindow(general_app.MainWindow):
    title = 'EVENSOUND'
    menus = [
        FileMenu,
    ]

LOGIC_DICT = general_app.LOGIC_DICT.copy()
LOGIC_DICT['main_window_class'] = MainWindow
