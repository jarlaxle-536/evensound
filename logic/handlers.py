import sys

from config import *
from gui import *

def new_file_handler():
    print('will create new file')

def open_file_handler():
    main_widget = GuiMixin.get_application().find_by_classname('MainWidget')
    QFileDialogMixin(widget=main_widget)

def save_file_handler():
    main_widget = GuiMixin.get_application().find_by_classname('MainWidget')
    QFileDialogMixin(widget=main_widget)
    print('will accept new file name')
    print('will save file under entered file name')

def exit_application_handler():
    print('exiting...')
    GuiMixin.get_application().exit()
