import unittest

from logic.auxiliary import *
from logic._01_general_app import *

class GeneralAppTest(unittest.TestCase):
    def setUp(self):
        init_test_app(self)
    def test_main_window(self):
        self.assertEqual(self.MainWindow.gui.windowTitle(), 'EVENSOUND')

if __name__ == '__main__':
    unittest.main()
