from gui.loader import *

class QMainWindow(GuiAdapter):
    _gui_constructor = QtWidgets.QMainWindow
    _menus = list()
    title = 'Main window'
    window_size = MAX_WINDOW_SIZE
    def setup(self):
        super().setup()
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.setWindowTitle(self.title)
        self.create_menubar()
        self.show()
    def create_menubar(self):
        self.statusBar()
        self.menubar = self.menuBar()
        for menu_name in self._menus:
            menu_obj, created = REGISTER.find(menu_name).get_or_create()
            self.menubar.addMenu(menu_obj.gui)
