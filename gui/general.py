from PyQt5 import QtWidgets, QtCore

from auxiliary import *

class GuiMixin(Root):
    constructor = lambda *args, **kwargs: None
    constructor_args = tuple()
    constructor_kwargs = dict()
    def __init__(self, **kwargs):
        print(f'{self.__class__.__name__} init')
        self.adapt()
        Root.__init__(self, **kwargs)
    def adapt(self, *args, **kwargs):
        obj = self.constructor(
            *self.constructor_args, **self.constructor_kwargs)
        Root.adapt(self, obj, name='gui')
    @property
    def application(self):
        return QtWidgets.QApplication.instance().adapter

class QApplicationMixin(GuiMixin):
    constructor = QtWidgets.QApplication
    constructor_args = (list(), )

class QMainWindowMixin(GuiMixin):
    constructor = QtWidgets.QMainWindow
    title = 'Main window'
    window_size = (1400, 800)
    window_centered = tuple(map(
        lambda t: (t[0] - t[1]) // 2, zip((1400, 800), window_size)
    ))
    menubar_dict = dict()
    def setup(self):
        self.setGeometry(*self.window_centered, *self.window_size)
        self.setWindowTitle(self.title)
        self.create_menubar()
        self.show()
    def create_menubar(self):
        menubar = self.menuBar()
        for menu_title, actions in self.menubar_dict.items():
            print(f'will add menu {menu_title} to {self} menubar')
            menu = menubar.addMenu(menu_title)
            setattr(self, f'{menu_title.lower()}_menu', menu)
            for action_cls in actions:
                action = action_cls.__call__()
                menu.addAction(action.gui)

class QActionMixin(GuiMixin):
    constructor = QtWidgets.QAction
    text = 'Action'
    shortcut = None
    def setup(self):
        self.setText(self.text)
        if not self.shortcut is None:
            self.setShortcut(self.shortcut)
    def connect_to_func(self, func):
        self.triggered.connect()

class QWidgetMixin(GuiMixin):
    constructor = QtWidgets.QWidget
    contents = dict()
    layout_type = QtWidgets.QVBoxLayout
    def setup(self):
        self.layout = self.layout_type.__call__()
        for k, v in self.contents.items():
            obj = v.__call__()
            setattr(self, k, obj)
            self.layout.addWidget(obj)
        self.setLayout(self.layout)
