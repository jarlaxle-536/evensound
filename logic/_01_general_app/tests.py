import unittest

from logic._01_general_app.general import *

class GeneralAppTest(unittest.TestCase):
    def setUp(self):
        self.app = APP_CLS()
        self.main_window = MAIN_WINDOW_CLS()
        self.main_widget = MAIN_WIDGET_CLS()

if __name__ == '__main__':
    unittest.main()
