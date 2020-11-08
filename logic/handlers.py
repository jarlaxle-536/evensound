import sys
import os

from .dialogs import *
from gui import *

def new_file_handler():
    print('will create new file')

def open_file_handler():
    app = GuiMixin.get_application()
    main_widget = app.find_by_classname('MainWidget')
    dialog = OpenCmpDialog(widget=main_widget)
    if os.path.exists(dialog.filepath):
        app.load(dialog.filepath)

def save_file_handler():
    app = GuiMixin.get_application()
    main_widget = app.find_by_classname('MainWidget')
    dialog = SaveCmpDialog(widget=main_widget)
    app.save(dialog.filepath)

def exit_application_handler():
    print('exiting...')
    GuiMixin.get_application().exit()
