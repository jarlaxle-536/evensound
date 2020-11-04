from gui import *

class NewFileAction(QActionMixin):
    text = 'New file'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.triggered.connect

class OpenFileAction(QActionMixin):
    text = 'Open file'

class SaveFileAsAction(QActionMixin):
    text = 'Save file'

class ExitAction(QActionMixin):
    text = 'Exit'
