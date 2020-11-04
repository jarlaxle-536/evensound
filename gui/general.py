from PyQt5 import QtWidgets

from auxiliary import *

class QApplicationMixin(Root):
    def __init__(self, **kwargs):
        self.adapt(QtWidgets.QApplication(list()), name='gui')
        super().__init__(**kwargs)

class QMainWindowMixin(Root):
    title = 'Main window'
    window_size = (1400, 800)
    window_centered = tuple(map(
        lambda t: (t[0] - t[1]) // 2, zip((1400, 800), window_size)
    ))
    def __init__(self, **kwargs):
        self.adapt(QtWidgets.QMainWindow(), name='gui')
        self.setGeometry(*self.window_centered, *self.window_size)
        self.setWindowTitle(self.title)
        self.show()
        super().__init__(**kwargs)

class QWidgetMixin(Root):
    contents = dict()
    layout_type = QtWidgets.QVBoxLayout
    def __init__(self, **kwargs):
        self.adapt(QtWidgets.QWidget(), name='gui')
        self.layout = self.layout_type.__call__()
        for k, v in self.contents.items():
            obj = v.__call__()
            setattr(self, k, obj)
            self.layout.addWidget(obj)
        self.setLayout(self.layout)
        super().__init__(**kwargs)
