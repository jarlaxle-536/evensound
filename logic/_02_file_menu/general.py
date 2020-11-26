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

@singleton_register('Composition')
class CompositionTitleLabel(QLabelMixin):
    def update(self):
        self.text = self.Composition.title
        super().update()

class MainWidget(general_app.MainWidget):
    def setup(self):
        self.contents['CompositionTitleLabel'] = CompositionTitleLabel
        super().setup()

LOGIC_DICT = general_app.LOGIC_DICT.copy()
LOGIC_DICT['application_class'] = Application
LOGIC_DICT['main_window_class'] = MainWindow
LOGIC_DICT['main_widget_class'] = MainWidget
