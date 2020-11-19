from .track_dialog import *

class NewTrackWidget(QWidgetMixin, FormDataMixin):
    pass

class NewTrackDialog(QDialogMixin):
    title = 'New track'
    central_widget = NewTrackWidget
