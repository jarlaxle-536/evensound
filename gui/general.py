from PyQt5 import QtWidgets

from auxiliary import *

class QApplicationMixin(Root):
    def __init__(self, **kwargs):
        self.gui = QtWidgets.QApplication(list())
        super().__init__(**kwargs)

class QMainWindowMixin(Root):
    constructor = QtWidgets.QMainWindow
    window_size = (1400, 800)
    window_centered = tuple(map(
        lambda t: (t[0] - t[1]) // 2, zip((1400, 800), window_size)
    ))
    def __init__(self, **kwargs):
        self.gui = QtWidgets.QMainWindow()
        
