from logic.loader import *

class ExitAction(QAction):
    text = 'Exit'
    def action(self):
        self._Application.object().exit()
