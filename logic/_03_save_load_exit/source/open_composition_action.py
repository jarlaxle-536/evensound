from .loader import *

from .open_composition_dialog import *

class SomeWidget(QWidgetMixin):
    pass

class OpenCompositionAction(QActionMixin):
    text = 'Open'
    def setup(self):
        self.dialog = OpenCompositionDialog(widget_cls='MainWidget')
        super().setup()
    def action(self):
        self.dialog.get_filepath()
