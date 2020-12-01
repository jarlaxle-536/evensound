from logic.loader import *

from logic.gui.dialogs import *

class SaveCompositionAction(QActionMixin):
    text = 'Save as'
    def setup(self):
        self.dialog = SaveCompositionDialog(widget_cls='MainWidget')
        super().setup()
    def action(self):
        self.dialog.get_filepath()
