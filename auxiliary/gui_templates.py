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
        for menu_name in self._menus:
            menu_obj = REGISTER.get(menu_name)[0].get_or_create()
            print(f'will add {menu_obj}')
        self.show()
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
    def compose(self, target):
        print(self, self._widgets)
        for cls_name in self._widgets:
            obj, created = REGISTER.get(cls_name)[0].get_or_create()
            target.addWidget(obj.gui)
            self._contents = self._contents.copy()
            self._contents[cls_name] = (len(self._contents), obj)

class QWidget(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QWidget
    _layout_type = QtWidgets.QVBoxLayout
    def setup(self):
        super().setup()
        self._layout = self._layout_type.__call__()
        WidgetComposer.compose(self, target=self._layout)
        self.setLayout(self._layout)

class QStackedWidget(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QStackedWidget
    def setup(self):
        super().setup()
        WidgetComposer.compose(self, target=self)
    def set_widget(self, cls_name):
        new_index, obj = self._contents.get(cls_name, (0, ) * 2)
        self.setCurrentIndex(new_index)

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
