import sys
import os

from .dialogs import *
from gui import *

def new_composition_handler():
    dialog = NewCompositionDialog()

def open_file_handler():
    app = GuiMixin.get_application()
    main_widget = app.find_by_classname('MainWidget')
    dialog = OpenCompositionDialogMixin(widget=main_widget)
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

def add_track_handler():
    dialog = AddTrackDialog()

def delete_track_handler():
    print('will delete current track')

def track_properties_handler():
    print('will open track properties dialog')
