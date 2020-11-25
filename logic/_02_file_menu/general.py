import logic._01_general_app as general_app

from .source import *

class Application(general_app.Application):
    def setup(self):
        self.state = State()

class MainWindow(general_app.MainWindow):
    title = 'EVENSOUND'
    menus = [
        FileMenu,
    ]

LOGIC_DICT = general_app.LOGIC_DICT.copy()
LOGIC_DICT['application_class'] = Application
LOGIC_DICT['main_window_class'] = MainWindow
