import logic._01_general_app

from .file_menu import *

class MainWindow(logic._01_general_app.MainWindow):
    menus = [
        FileMenu,
    ]
    def setup(self):
        print('main window')
        super().setup()
