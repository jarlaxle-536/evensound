import unittest
from PyQt5 import QtTest

from logic.auxiliary import *
from logic._02_file_menu import *

class UnitTest(unittest.TestCase):
    def setUp(self):
        init_test_app(self, LOGIC_DICT)
    def test_file_menu_general(self):
        menubar = self.main_window.gui.menuBar()
        present_menus = [obj for obj in menubar.children()
            if obj.__class__.__name__ == 'QMenu']
        "Verify there is at least one menu in menubar"
        file_menu = present_menus[0]
        "Verify this menu title is File"
        self.assertEqual(file_menu.title(), 'File')
    def test_new_composition_dialog(self):
        pass
    def test_edit_composition_dialog(self):
        pass
    def test_state_general(self):
        "Verify composition is present in state instance dict"
        self.assertIn('composition', self.application.state.__dict__)
        "Verify attached-to-state composition title"
        self.assertEqual(self.application.state.composition.title,
            DEFAULT_COMPOSITION_TITLE)
    def test_composition_general(self):
        "Verify default composition title"
        cmp = Composition()
        self.assertEqual(cmp.title, DEFAULT_COMPOSITION_TITLE)

DEFAULT_COMPOSITION_TITLE = Composition.title

if __name__ == '__main__':
    unittest.main()
