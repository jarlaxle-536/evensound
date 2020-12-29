from logic.entities import *
from logic.widgets import *

class Application(QApplication):
    def setup(self):
        self.adapt(State(), name='state')
#        self.adapt(Player(), name='player')
        super().setup()

class MainWindow(QMainWindow):
    title = 'Evensound'
    _menus = [
        'FileMenu',
        'TrackMenu',
        'SettingsMenu'
    ]

def create_gui_dict():
    gui_dict = {cls_name: REGISTER.get(cls_name)[0].__call__() for cls_name in [
        'Application',
        'MainWindow',
        'MainWidget'
    ]}
    return gui_dict
