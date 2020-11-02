from entities.mixins import *
from gui.mixins import *

class Application(QApplicationMixin, StateMixin):
    pass

class MainWindow(QMainWindowMixin):
    pass
