from .loader import *
from .new_composition_dialog import *

class NewCompositionAction(QActionMixin):
    text = 'New'
    def setup(self):
        self.dialog = NewCompositionDialog()
        super().setup()
    def action(self):
        self.dialog.show()
