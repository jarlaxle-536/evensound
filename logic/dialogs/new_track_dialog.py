from .track_dialog import *

class NewTrackCancelButton(QPushButtonMixin):
    text = 'Cancel'
    def action(self):
        dialog = self.find('NewTrackDialog')
        dialog.close()

class NewTrackOKButton(QPushButtonMixin):
    dependent_gui_classes = {
        'TrackListWidget',
    }
    text = 'OK'
    def action(self):
        data = self.find('NewTrackWidget').acquire()
        composition = self.application.state.composition
        composition.insert_track(**data)
        dialog = self.find('NewTrackDialog')
        dialog.close()
        super().action()

class NewTrackControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {cls.__name__: cls for cls in [
        NewTrackCancelButton,
        NewTrackOKButton
    ]}

class NewTrackWidget(QWidgetMixin, FormDataMixin):
    form_fields = [
        'TrackNameRow',
        'InstrumentTimbreRow',
        'InstrumentNameRow'
    ]
    contents = {cls.__name__: cls for cls in [
        TrackNameRow,
        InstrumentTimbreRow,
        InstrumentNameRow,
        NewTrackControlPanel,
    ]}
    def refine_data(self, data):
        res = {
            'name': data['name'],
            'instrument_program_code': Instrument.find_program_code_by_name(
                data['instrument_name'])
        }
        return res

class NewTrackDialog(QDialogMixin):
    title = 'New track'
    central_widget = NewTrackWidget
