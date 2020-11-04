import sys

from gui import *

def exit_application():
    print('exiting...')
    GuiMixin.get_application().exit()
