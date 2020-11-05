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
        SettingsMenu
    ]

class SomeLabel(QLabelMixin):
    text = 'lorem ipsum'

class Widget1(QWidgetMixin):
    contents = {
        'label1': SomeLabel,
        'label2': SomeLabel,
        'label3': SomeLabel,
    }

class MainWidget(QWidgetMixin):
    contents = {
        'widget1': Widget1
    }
