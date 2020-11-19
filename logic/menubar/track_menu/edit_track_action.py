from logic.loader import *

from logic.dialogs.edit_track_dialog import *

class EditTrackAction(QActionMixin):
    text = 'Edit track'
    def action(self):
        dialog = EditTrackDialog()
