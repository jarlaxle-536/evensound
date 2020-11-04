from entities import *
from gui import *

from logic.menubar import *

class Application(QApplicationMixin, StateMixin):
    pass

class MainWindow(QMainWindowMixin):
    title = 'EVENSOUND'
    menus = [
        FileMenu,
        TrackMenu,
    ]

class MainWidget(QWidgetMixin):
    pass
