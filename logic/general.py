from entities import *
from gui import *

class Application(QApplicationMixin, StateMixin):
    pass

class MainWindow(QMainWindowMixin):
    title = 'EVENSOUND'

class MainWidget(QWidgetMixin):
    pass
