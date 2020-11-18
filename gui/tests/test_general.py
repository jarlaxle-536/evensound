from gui.tests.loader import *

class GuiGeneralTestCase(unittest.TestCase):
    def setUp(self):
        self.app = QApplicationMixin()
        self.main_window = QMainWindowMixin()
    def test_search(self):
        print('app:', self.app)
        self.assertEqual(self.app.application, GuiMixin.get_application())
        for attr_name in ['app', 'main_window']:
            self.assertEqual(getattr(self, attr_name).application, self.app)

if __name__ == '__main__':
    unittest.main()
