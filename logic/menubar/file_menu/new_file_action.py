from logic.loader import *

from logic.dialogs.new_composition_dialog import *

class NewFileAction(QActionMixin):
    text = 'New file'
    def action(self):
        dialog = NewCompositionDialog()
