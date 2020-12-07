from logic.tests_loader import *

class GeneralAppTestCase(unittest.TestCase):
    def setUp(self):
        init_ut_instance(self, GUI_DICT)
    def test_title(self):
        self.assertEqual(self.MainWindow.gui.windowTitle(), 'Evensound')

if __name__ == '__main__':
    unittest.main()
