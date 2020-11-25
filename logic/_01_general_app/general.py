from gui import *

class Application(QApplicationMixin):
    pass

class MainWindow(QMainWindowMixin):
    title = 'EVENSOUND'

class MainWidget(QWidgetMixin):
    pass

LOGIC_DICT = {
    'application_class': Application,
    'main_window_class': MainWindow,
    'main_widget_class': MainWidget
}
