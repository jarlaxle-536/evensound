from PyQt5 import QtWidgets

from auxiliary import *
from entities import *

class QApplicationAdapter(GuiAdapterMixin):
    constructor = QtWidgets.QApplication
    constructor_args = (list(), )

class StateAdapter(StatefulMixin):
    constructor = State

class Application(QApplicationAdapter, StateAdapter):
    pass
