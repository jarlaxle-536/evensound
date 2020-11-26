from .loader import *

class ExitAction(QActionMixin):
    text = 'Exit'
    def action(self):
        self.application.quit()
