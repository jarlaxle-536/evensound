from auxiliary import *

from .widget_composer import *

class QDialog(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QDialog
    _layout_type = QtWidgets.QVBoxLayout
    window_size = (600, 300)
    title = 'Dialog'
    def setup(self):
        super().setup()
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.setWindowTitle(self.title)
        self._layout = self._layout_type.__call__()
        WidgetComposer.compose(
            self, composing_func=lambda gui: self._layout.addWidget(
                gui))
        self.setLayout(self._layout)
