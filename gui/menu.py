from auxiliary import *

from .widget_composer import *

class QMenu(GuiAdapter, WidgetComposer):
    _gui_constructor = QtWidgets.QMenu
    title = 'Menu'
    def setup(self):
        super().setup()
        WidgetComposer.compose(
            self, composing_func=lambda gui: self.gui.addAction(gui))
        self.setTitle(self.title)
