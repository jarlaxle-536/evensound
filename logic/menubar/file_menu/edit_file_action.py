from logic.loader import *

from logic.dialogs.edit_composition_dialog import *

class EditFileAction(QActionMixin):
    text = 'Edit file'
    def action(self):
        dialog = EditCompositionDialog()
