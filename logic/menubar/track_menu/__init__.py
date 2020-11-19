from .new_track_action import *
from .edit_track_action import *

class TrackMenu(QMenuMixin):
    title = 'Track'
    actions_list = [
        NewTrackAction,
        EditTrackAction
    ]
