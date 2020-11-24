from .loader import *

from .menubar import *
from .widgets import *
from .dialogs import *
from .threads import *
from .dependencies import *

class Application(QApplicationMixin, StateMixin):
    pass

class MainWindow(QMainWindowMixin):
    title = 'EVENSOUND'
    menus = [
        FileMenu,
        TrackMenu,
        SettingsMenu
    ]
