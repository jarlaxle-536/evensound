from logic.loader import *

class ExitAction(QActionMixin): # done
    text = 'Exit'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        print('Exiting...')
        GuiMixin.get_application().exit()
