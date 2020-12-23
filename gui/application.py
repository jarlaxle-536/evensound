from gui.loader import *

class QApplication(GuiAdapter):
    _gui_constructor = QtWidgets.QApplication
    _gui_constructor_args = [list(), ]
