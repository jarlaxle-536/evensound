from .track_dialog import *

class EditTrackWidget(QWidgetMixin, FormDataMixin):
    pass

class EditTrackDialog(QDialogMixin):
    title = 'Edit track'
    central_widget = EditTrackWidget
