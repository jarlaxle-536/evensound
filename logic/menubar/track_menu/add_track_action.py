from logic.general import *

class AddTrackAction(QActionMixin):
    text = 'Add track'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        print('will show new track dialog')
