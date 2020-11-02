from PyQt5 import QtWidgets

from auxiliary.mixins import *

class QApplicationMixin(GuiMixin):
    constructor = QtWidgets.QApplication
    constructor_args = (list(), )

class QMainWindowMixin(GuiMixin):
    constructor = QtWidgets.QMainWindow
    window_size = (1400, 800)
    window_centered = tuple(map(
        lambda t: (t[0] - t[1]) // 2, zip((1400, 800), window_size)
    ))
    def setup(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.window_centered, *self.window_size)
        self.show()
        super().setup()

class QWidgetMixin(GuiMixin):
    layout_type = QtWidgets.QVBoxLayout
    def setup(self):
        layout = self.layout_type()
        for component in self.contents.values():
#            layout.addWidget(component.gui)
            print(f'will add {component}')
        self.setLayout(layout)
        super().setup()
