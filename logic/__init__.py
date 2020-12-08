from logic._02_main_thread import *
from logic.entities import *
from logic.widgets import *

class Application(QApplication):
    def setup(self):
        self._State()
        self._Player()
        super().setup()

class MainWindow(QMainWindow):
    title = 'Evensound'

def create_gui_dict():
    gui_dict = {cls_name: REGISTER.get(cls_name)[0].__call__() for cls_name in [
        'Application',
        'MainWindow',
        'MainWidget'
    ]}
    return gui_dict
