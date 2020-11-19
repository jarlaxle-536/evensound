from logic.loader import *

class SaveFileAsAction(QActionMixin):
    text = 'Save file'
    def action(self):
        print('will open save cmp dialog')
