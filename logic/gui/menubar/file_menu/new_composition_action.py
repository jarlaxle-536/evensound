from logic.loader import *

from logic.gui.dialogs import *

class NewCompositionAction(QActionMixin):
    text = 'New'
    def setup(self):
        self.dialog = NewCompositionDialog()
        super().setup()
    def action(self):
        self.dialog.show()
