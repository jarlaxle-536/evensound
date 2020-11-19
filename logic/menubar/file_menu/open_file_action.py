from logic.loader import *

class OpenFileAction(QActionMixin):
    text = 'Open file'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        print('will open open cmp dialog')
