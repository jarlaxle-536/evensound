from .loader import *

from .state import *

class Application(QApplication):
    def setup(self):
        self.adapt(self._State(), name='state')
        super().setup()

class MainWindow(QMainWindow):
    title = 'Evensound'

class MainWidget(QWidget):
    pass
