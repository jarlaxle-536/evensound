import unittest

from logic.auxiliary import *
from logic._01_general_app import *

class GeneralAppTest(unittest.TestCase):
    def setUp(self):
        init_test_app(self, LOGIC_DICT)
    def test_window_title(self):
        self.assertEqual(self.main_window.gui.windowTitle(), 'EVENSOUND')

if __name__ == '__main__':
    unittest.main()
