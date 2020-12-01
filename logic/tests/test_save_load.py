import unittest
from PyQt5 import QtTest

from logic.auxiliary import *
from logic._03_save_load_exit import *

class SaveLoadTest(unittest.TestCase):
    def setUp(self):
        init_test_app(self)
        self.menubar = self.MainWindow.gui.menuBar()
        self.present_menus = [obj for obj in self.menubar.children()
            if obj.__class__.__name__ == 'QMenu']
        self.file_menu = self.present_menus[0]
        self.file_menu_actions = [obj for obj in self.file_menu.children()
            if obj.__class__.__name__ == 'QAction']
        self.present_menu_titles = list(ACTION_TEXTS.values())
    def test_file_menu_general(self):
        self.assertEqual(self.file_menu.title(), 'File')
        for t in self.present_menu_titles:
            self.assertIn(t, [a.text() for a in self.file_menu_actions])
    def test_open_cmp_action(self):
        self.open_cmp_action = Singleton.find('OpenCompositionAction').gui
        self.open_cmp_dialog = Singleton.find('OpenCompositionDialog').gui
        "Ignoring dialog title and visibility checks"
    def test_save_cmp_action(self):
        state1 = self.Application.state
        print(state1.__dict__)
        print(state1.composition.__dict__)
        previous_files = os.listdir(FILES_DIR)
        print(previous_files)
        self.save_cmp_action = Singleton.find('SaveCompositionAction').gui
        self.save_cmp_dialog = Singleton.find('SaveCompositionDialog').gui
        "Ignoring dialog title and visibility checks"
    def test_exit_action(self):
        pass

DIALOGS_TITLES = {k: Root.find_class(k).title for k in [
    'OpenCompositionDialog',
    'SaveCompositionDialog'
]}
ACTION_TEXTS = {k: Root.find_class(k).text for k in [
    'NewCompositionAction',
    'OpenCompositionAction',
    'SaveCompositionAction',
    'ExitAction'
]}

if __name__ == '__main__':
    unittest.main()
