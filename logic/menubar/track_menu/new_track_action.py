from logic.loader import *

from logic.dialogs.new_track_dialog import *

class NewTrackAction(QActionMixin):
    text = 'New track'
    def action(self):
        dialog = NewTrackDialog()
