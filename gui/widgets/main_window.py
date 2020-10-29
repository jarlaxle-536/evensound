from gui.general import *

class MainWindow(MainWindowAdapter):
    title = 'EVENSOUND'
    def setup(self):
        super().setup()
        self.statusBar()
        menubar = self.menuBar()
        self.file_menu = menubar.addMenu('&File')
        self.file_menu.addAction(NewFileAction().gui)
        self.file_menu.addAction(OpenFileAction().gui)
        self.file_menu.addAction(ExitAction().gui)
        self.tracks_menu = menubar.addMenu('&Tracks')
        self.tracks_menu.addAction(AddTrackAction().gui)
        self.about_menu = menubar.addMenu('&About')
        self.about_menu.addAction(InfoAction().gui)
        self.about_menu.addAction(HelpAction().gui)

class NewFileAction(ActionAdapter):
    text = 'New file'
    shortcut = 'Ctrl+N'
    tip = 'Create new composition'
    def action(self):
        print('will create new file')

class OpenFileAction(ActionAdapter):
    text = 'Open file'
    shortcut = 'Ctrl+O'
    tip = 'Open existing file'
    def action(self):
        print('will show file dialog to choose file for loading')

class ExitAction(ActionAdapter):
    text = 'Exit'
    shortcut = 'Ctrl+Q'
    tip = 'Exit'
    def action(self):
        print('will exit program')

class AddTrackAction(ActionAdapter):
    text = 'Add'
    shortcut = 'Ctrl+A'
    tip = 'Add new track'

class InfoAction(ActionAdapter):
    text = 'Info'
    shortcut = 'Ctrl+I'
    tip = 'Show info on program'

class HelpAction(ActionAdapter):
    text = 'Help'
    shortcut = 'Ctrl+H'
    tip = 'Get help'
