from gui.loader import *
from gui.widget_composer import *

class QStackedWidget(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QStackedWidget
    def setup(self):
        super().setup()
        WidgetComposer.compose(self,
            composing_func=lambda gui: self.addWidget(gui))
    def set_widget(self, cls_name):
        new_index, obj = self._contents.get(cls_name, (0, ) * 2)
        self.setCurrentIndex(new_index)
