from entities import *
from gui import *

from logic.menubar_actions import *

class Application(QApplicationMixin, StateMixin):
    pass

class MainWindow(QMainWindowMixin):
    title = 'EVENSOUND'
    menubar_dict = {
        'File': [
            NewFileAction,
            OpenFileAction,
            SaveFileAsAction,
            ExitAction
        ],
        'Track': [

        ],
        'About': [

        ]
    }

class MainWidget(QWidgetMixin):
    pass
