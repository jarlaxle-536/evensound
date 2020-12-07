import unittest

from auxiliary import *
from logic import *

def init_ut_instance(ut, gui_dict):
    for k, v in gui_dict.items():
        setattr(ut, k, v)

GUI_DICT = create_gui_dict()
