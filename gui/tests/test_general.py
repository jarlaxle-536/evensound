import unittest

from gui.general import *

class SingletonTestCase(unittest.TestCase):
    def setUp(self):
        self.app = QApplicationMixin()
        self.main_window = QMainWindowMixin()
    def test_search(self):
        self.assertEqual(self.app.application, GuiMixin.get_application())
        for attr_name in ['app', 'main_window']:
            self.assertEqual(getattr(self, attr_name).application, self.app)
