from logic.tests_loader import *

class FileMenuTest(unittest.TestCase):
    def setUp(self):
        init_ut_instance(self, GUI_DICT)
        self.application = REGISTER.get('Application')[0].object().gui
        self.menubar = REGISTER.get('MainWindow')[0].object().gui.menuBar()
        self.menus = {m.text(): m for m in self.menubar.actions()}
        self.file_menu = self.menus.get('File').menu()
        self.file_menu_actions = {m.text(): m for m in self.file_menu.actions()}
    def tearDown(self):
        pass
    def test_new_composition_action(self):
        new_cmp_action = self.file_menu_actions.get('New')
        self.assertTrue(not new_cmp_action is None)
        new_cmp_action.trigger()
    def test_exit_action(self):
        exit_action = self.file_menu_actions.get('Exit')
        self.assertTrue(not exit_action is None)
        exit_action.trigger()

if __name__ == '__main__':
    unittest.main()
