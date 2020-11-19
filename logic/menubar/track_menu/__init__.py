from .add_track_action import *

class TrackMenu(QMenuMixin):
    title = 'File'
    actions_list = [
        AddTrackAction
    ]
