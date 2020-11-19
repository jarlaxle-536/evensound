from logic.loader import *

class NewFileAction(QActionMixin):
    text = 'New file'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        print('will open new cmp dialog')
