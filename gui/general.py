from .loader import *

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
    def action(self):
        pass
    @staticmethod
    def get_application():
        return QtWidgets.QApplication.instance().adapter
    @property
    def application(self):
        return self.get_application()

class GuiConnectMeta(type):
    def __new__(meta, name, bases, cls_dict):
        base_cls = bases[0]
        gui_links = cls_dict.get('gui_links', dict())
        for k, v in gui_links.items():
            cls_dict[k] = GuiConnectedField(base_cls.__dict__[k], gui_classes=v)
        obj = super().__new__(meta, name, bases, cls_dict)
        return obj

class GuiConnectedField:

    def __init__(self, value=None, gui_classes=list()):
        self.gui_classes = gui_classes
        self.value = self.__class__.value = value

    def __get__(self, target, owner):
        if target is None: return self.value
        dct = target.__dict__
        dct.setdefault(self.__name, self.value)
        return dct.get(self.__name)

    def __set__(self, target, value):
        print(target, value)
        target.__dict__[self.__name] = value
        for cls_name in self.gui_classes:
            if not cls_name in target.__dict__:
                obj = GuiMixin.find(cls_name)
                if not obj is None:
                    setattr(target, cls_name, obj)
            try:
                getattr(target, cls_name).update()
            except Exception as exc:
                pass

    def __set_name__(self, owner, name):
        self.__name = name


class QApplicationMixin(GuiMixin):
    constructor = QtWidgets.QApplication
    constructor_args = (list(), )

class QMainWindowMixin(GuiMixin):
    constructor = QtWidgets.QMainWindow
    title = 'Main window'
    window_size = MAX_WINDOW_SIZE
    menus = list()
    def update(self):
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.setWindowTitle(self.title)
        self.create_menubar()
    def setup(self):
        self.update()
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
    def update(self):
        self.setTitle(self.title)
    def setup(self):
        self.update()
        menu = self.menubar.addMenu(self.title)
        for action_cls in self.actions_list:
            action_cls(menu=menu)

class QActionMixin(GuiMixin):
    constructor = QtWidgets.QAction
    text = 'Action'
    shortcut = None
    fields = ['menu']
    def update(self):
        self.setText(self.text)
    def setup(self):
        self.update()
        if not self.shortcut is None:
            self.setShortcut(self.shortcut)
        self.qmenu = self.menu.addAction(self.text)
        self.connect_to_func(self.action)
    def connect_to_func(self, func):
        self.qmenu.triggered.connect(func)

class QWidgetMixin(GuiMixin):
    constructor = QtWidgets.QWidget
    layout_type = QtWidgets.QVBoxLayout
    contents = dict()
    def update(self):
#        self.layout.clear()
        for k, v in self.contents.items():
            obj = v.__call__()
            setattr(self, k, obj)
            self.layout.addWidget(obj.gui)
    def setup(self):
        self.layout = self.layout_type.__call__()
        self.update()
        self.setLayout(self.layout)

class QListWidgetMixin(GuiMixin):
    constructor = QtWidgets.QListWidget
    contents = dict()
    def update(self):
        print(f'Updating {self.__class__.__name__}')
        self.clear()
        for k, v in self.contents.items():
            print(k)
            self.addItem(k)
    def setup(self):
        self.update()
        self.currentRowChanged.connect(self.index_changed)
    def index_changed(self, index):
        pass

class QLabelMixin(GuiMixin):
    constructor = QtWidgets.QLabel
    text = 'Label'
    fields = ['text']
    def update(self):
        self.setText(self.text)
    def setup(self):
        self.update()

class QPushButtonMixin(GuiMixin):
    constructor = QtWidgets.QPushButton
    text = 'Button'
    def update(self):
        self.setText(self.text)
    def setup(self):
        self.update()
        self.connect_to_func(self.action)
    def connect_to_func(self, action):
        self.clicked.connect(action)

class QDialogMixin(GuiMixin):
    constructor = QtWidgets.QDialog
    title = 'Dialog'
    window_size = (600, 300)
    layout_type = QtWidgets.QVBoxLayout
    central_widget = QWidgetMixin
    def update(self):
        self.setWindowTitle(self.title)
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.layout.addWidget(self.central_widget.__call__().gui)
    def setup(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.update()
        self.setLayout(self.layout)

class FileDialogMixin(GuiMixin):
    constructor = QtWidgets.QFileDialog
    title = 'File dialog'
    window_size = (320, 240)
    fields = ['widget_cls']
    def update(self):
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.options = self.Options()
        self.options |= self.DontUseNativeDialog
        self.options |= self.DontUseCustomDirectoryIcons
    def setup(self):
        self.update()
    @property
    def widget(self):
        return self.find(self.widget_cls)
    def get_filepath(self):
        raise TypeError('Should be specified in subclass')
