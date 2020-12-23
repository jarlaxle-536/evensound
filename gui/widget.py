from gui.loader import *
from gui.widget_composer import *

class QWidget(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QWidget
    _layout_type = QtWidgets.QVBoxLayout
    def setup(self):
        super().setup()
        self._layout = self._layout_type.__call__()
        WidgetComposer.compose(
            self, composing_func=lambda gui: self._layout.addWidget(
                gui))
        self.setLayout(self._layout)
