from .general import *
from .aux_data import *

class GuiAdapter(Singleton):
    _gui_constructor = lambda *args, **kwargs: None
    _gui_constructor_args = list()
    _gui_constructor_kwargs = dict()
    def setup(self):
        self.adapt(
            self._gui_constructor(
                *self._gui_constructor_args,
                **self._gui_constructor_kwargs
            ), name='gui'
        )
        super().setup()

class QApplication(GuiAdapter):
    _gui_constructor = QtWidgets.QApplication
    _gui_constructor_args = [list(), ]

class QMainWindow(GuiAdapter):
    _gui_constructor = QtWidgets.QMainWindow
    _menus = list()
    title = 'Main window'
    window_size = MAX_WINDOW_SIZE
    def setup(self):
        super().setup()
        self.create_menubar()
        self.show()
    def create_menubar(self):
        self.statusBar()
        self.menubar = self.menuBar()
        for menu_name in self._menus:
            menu_obj, created = REGISTER.get(menu_name)[0].get_or_create()
            self.menubar.addMenu(menu_obj.gui)
    def update(self):
        super().update()
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.setWindowTitle(self.title)

class WidgetComposer(Root):
    _widgets = list()
    _contents = dict()
    def compose(self, composing_func):
        for cls_name in self._widgets:
            obj, created = REGISTER.get(cls_name)[0].get_or_create()
            composing_func.__call__(obj.gui)
            self._contents = self._contents.copy()
            self._contents[cls_name] = (len(self._contents), obj)

class QWidget(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QWidget
    _layout_type = QtWidgets.QVBoxLayout
    def setup(self):
        super().setup()
        self._layout = self._layout_type.__call__()
        WidgetComposer.compose(
            self, composing_func=lambda gui: self._layout.addWidget(
                gui, alignment=QtCore.Qt.AlignCenter))
        self.setLayout(self._layout)

class QStackedWidget(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QStackedWidget
    def setup(self):
        super().setup()
        WidgetComposer.compose(self,
            composing_func=lambda gui: self.addWidget(gui))
    def set_widget(self, cls_name):
        new_index, obj = self._contents.get(cls_name, (0, ) * 2)
        self.setCurrentIndex(new_index)

class QMenu(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QMenu
    title = 'Menu'
    def setup(self):
        self._gui_constructor_args = [self.parent, ]
        super().setup()
        WidgetComposer.compose(self,
            composing_func=lambda gui: self.addAction(gui))
    def update(self):
        self.setTitle(self.title)
        super().update()

class QLabel(GuiAdapter):
    _gui_constructor = QtWidgets.QLabel
    text = 'Label'
    def update(self):
        super().update()
        self.setText(self.text)

class QPushButton(GuiAdapter):
    _gui_constructor = QtWidgets.QPushButton
    text = 'Button'
    def update(self):
        super().update()
        self.setText(self.text)
    def setup(self):
        super().setup()
        self.clicked.connect(self.action)
    def action(self):
        print(f'{self} clicked.')

class QAction(GuiAdapter):
    _gui_constructor = QtWidgets.QAction
    text = 'Action'
    def update(self):
        self.setText(self.text)
    def setup(self):
        super().setup()
        self.triggered.connect(self.action)
    def action(self):
        print(f'{self} triggered.')
