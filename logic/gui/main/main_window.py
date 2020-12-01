from logic.loader import *

from logic.gui.menubar import *

class MainWindow(QMainWindowMixin):
    title = 'EVENSOUND'
    menus = [
        FileMenu,
    ]
