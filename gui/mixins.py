from PyQt5 import QtWidgets

from auxiliary import *

class GuiMixin(Root):
    adapted_name = 'gui'
    @classmethod
    def gui_element(cls, inst):
        return getattr(inst, cls.adapted_name)
    @property
    def application(self):
        return QtWidgets.QApplication.instance().adapter

class QApplicationMixin(GuiMixin):
    def setup(self, **kwargs):
        self.gui = QtWidgets.QApplication([])

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
    constructor = QtWidgets.QWidget
    layout_type = QtWidgets.QVBoxLayout
    def setup(self):
        layout = self.layout_type()
        for component in self.contents.values():
            print(f'will add {component}')
        self.setLayout(layout)
        super().setup()

class QLabelMixin(GuiMixin):
    constructor = QtWidgets.QLabel
    text = 'Label'
    def setup(self):
        self.setText(self.text)
        super().setup()

class QButtonMixin(GuiMixin):
    constructor = QtWidgets.QPushButton
    text = 'Button'
    def setup(self):
#        self.gui.clicked.connect(self.action)
        super().setup()
    def action(self):
        print(f'Doing action for {self.__class__.__name__}')
