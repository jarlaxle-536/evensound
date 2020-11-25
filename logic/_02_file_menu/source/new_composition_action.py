from .loader import *
from .new_composition_dialog import *

class NewCompositionAction(QActionMixin):
    text = 'New file'
    def action(self):
        dialog = NewCompositionDialog()
