from PyQt5 import QtWidgets, QtCore, QtGui

from auxiliary import *
from config import *

class GuiUpdater(Root):
    pass

class GuiMixin(Singleton):
    constructor = lambda *args, **kwargs: None
    constructor_args = tuple()
    constructor_kwargs = dict()
    def __init__(self, **kwargs):
        self.adapt()
        Root.__init__(self, **kwargs)
    def adapt(self, *args, **kwargs):
        obj = self.constructor(
            *self.constructor_args, **self.constructor_kwargs)
        Root.adapt(self, obj, name='gui')
    @staticmethod
    def get_application():
        return QtWidgets.QApplication.instance().adapter
    @property
    def application(self):
        return self.get_application()

class QApplicationMixin(GuiMixin):
    constructor = QtWidgets.QApplication
    constructor_args = (list(), )

class QMainWindowMixin(GuiMixin):
    constructor = QtWidgets.QMainWindow
    title = 'Main window'
    window_size = MAX_WINDOW_SIZE
    menus = list()
    def setup(self):
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.setWindowTitle(self.title)
        self.create_menubar()
        self.show()
    def create_menubar(self):
        if not self.menus: return
        menubar = self.menuBar()
        for menu_cls in self.menus:
            menu_cls(menubar=menubar)

class QMenuMixin(GuiMixin):
    title = 'Menu'
    constructor = QtWidgets.QMenu
    actions_list = list()
    fields = ['menubar']
    def setup(self):
        self.setTitle(self.title)
        menu = self.menubar.addMenu(self.title)
        for action_cls in self.actions_list:
            action_cls(menu=menu)

class QActionMixin(GuiMixin):
    constructor = QtWidgets.QAction
    text = 'Action'
    shortcut = None
    fields = ['menu']
    def setup(self):
        self.setText(self.text)
        if not self.shortcut is None:
            self.setShortcut(self.shortcut)
        self.qmenu = self.menu.addAction(self.text)
    def connect_to_func(self, func):
        self.qmenu.triggered.connect(func)

class QWidgetMixin(GuiMixin):
    constructor = QtWidgets.QWidget
    layout_type = QtWidgets.QVBoxLayout
    contents = dict()
    def setup(self):
        self.layout = self.layout_type.__call__()
        for k, v in self.contents.items():
            obj = v.__call__()
            setattr(self, k, obj)
            self.layout.addWidget(obj.gui)
        self.setLayout(self.layout)

class QListWidgetMixin(GuiMixin):
    constructor = QtWidgets.QListWidget
    contents = dict()
    def setup(self):
        for k, v in self.contents.items():
            self.addItem(k)

class QLabelMixin(GuiMixin):
    constructor = QtWidgets.QLabel
    text = 'Label'
    fields = ['text']
    def setup(self):
        self.setText(self.text)

class QPushButtonMixin(GuiMixin):
    constructor = QtWidgets.QPushButton
    text = 'Button'
    def setup(self):
        self.setText(self.text)
    def connect_to_func(self, action):
        self.clicked.connect(action)

class QDialogMixin(GuiMixin):
    constructor = QtWidgets.QDialog
    title = 'Dialog'
    window_size = (600, 300)
    layout_type = QtWidgets.QVBoxLayout
    central_widget = QWidgetMixin
    def setup(self):
        self.setWindowTitle(self.title)
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.show()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.central_widget.__call__().gui)
        self.setLayout(self.layout)

class FileDialogMixin(GuiMixin):
    constructor = QtWidgets.QFileDialog
    title = 'File dialog'
    window_size = (320, 240)
    fields = ['widget']
    def setup(self):
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.options = self.Options()
        self.options |= self.DontUseNativeDialog
        self.options |= self.DontUseCustomDirectoryIcons
        self.get_filepath()
    def get_filepath(self):
        raise TypeError('Should be specified in subclass')
