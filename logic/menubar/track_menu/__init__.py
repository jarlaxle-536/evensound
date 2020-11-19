from .add_track_action import *

class TrackMenu(QMenuMixin):
    title = 'Track'
    actions_list = [
        AddTrackAction
    ]
