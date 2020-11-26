import logic._02_file_menu

from .file_menu import *

class MainWindow(logic._02_file_menu.MainWindow):
    menus = [
        FileMenu,
    ]
