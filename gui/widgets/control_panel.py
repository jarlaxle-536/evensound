from gui.general import *
from gui.widgets.track_creation_form import *

class ControlPanel(WidgetAdapter):
    layout_type = QtWidgets.QHBoxLayout
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            SaveButton,
            LoadButton,
            AddTrackButton,
            PlayOrStopButton,
        ]}
        super().setup()

class SaveButton(ButtonAdapter):
    title = 'Save as'
    def action(self):
        print('will show file dialog')

class LoadButton(ButtonAdapter):
    title = 'Load'
    def action(self):
        print('will show file dialog')

class AddTrackButton(ButtonAdapter):
    title = 'Add track'
    def action(self):
        print('will show dialog')
        self.dialog = TrackCreationForm()

class PlayOrStopButton(ButtonAdapter):
    thread_dependent_titles = {True: 'Play', False: 'Stop'}
    def setup(self):
        self.play_thread = PlayThread()
        super().setup()
        self.update()
    def update(self):
        self.title = self.thread_dependent_titles.get(
            self.play_thread.waiting, 'ERROR')
        self.setText(self.title)
    def action(self):
        print('playing or stopping')
        self.play_thread.toggle_activity()
        self.update()

class PlayThread(ThreadAdapter):
    def action(self):
        print('PLAY THREAD')
