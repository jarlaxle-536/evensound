from logic.loader import *

class ExitAction(QActionMixin): # done
    text = 'Exit'
    def action(self):
        print('Exiting...')
        GuiMixin.get_application().exit()
