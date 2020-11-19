from logic.loader import *

class SaveFileAsAction(QActionMixin):
    text = 'Save file'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        print('will open save cmp dialog')
