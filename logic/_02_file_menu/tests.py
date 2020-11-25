import unittest
from PyQt5 import QtTest

from logic.auxiliary import *
from logic._02_file_menu import *

class UnitTest(unittest.TestCase):
    def setUp(self):
        init_test_app(self, LOGIC_DICT)
        self.menubar = self.main_window.gui.menuBar()
        self.present_menus = [obj for obj in self.menubar.children()
            if obj.__class__.__name__ == 'QMenu']
        self.file_menu = self.present_menus[0]
        self.file_menu_actions = [obj for obj in self.file_menu.children()
            if obj.__class__.__name__ == 'QAction']
        self.present_menu_titles = ['New composition']
        self.new_composition_action = [a for a in self.file_menu_actions
                    if a.text() == 'New composition'][0]
        self.new_composition_dialog = Singleton.find('NewCompositionDialog').gui
    def test_file_menu_general(self):
        "Verify this menu title is File"
        self.assertEqual(self.file_menu.title(), 'File')
        "Verify both new cmp and edit cmp actions are present in File menu"
        for t in self.present_menu_titles:
            self.assertIn(t, [a.text() for a in self.file_menu_actions])
    def test_new_cmp_action(self):
        "Check dialog properties"
        self.assertEqual(self.new_composition_dialog.windowTitle(),
            'New composition')
        "Verify dialog visibility"
        test_attribute_toggled(
            self,
            self.new_composition_dialog.isVisible,
            self.new_composition_action.trigger,
            False
        )
    def test_new_cmp_dialog_cancel_button(self):
        self.new_composition_action.trigger()
        cancel_button = Singleton.find('NewCompositionCancelButton').gui
        test_attribute_toggled(
            self,
            self.new_composition_dialog.isVisible,
            cancel_button.click,
            True
        )
    def test_new_cmp_dialog_ok_button(self):
        self.new_composition_action.trigger()
        cancel_button = Singleton.find('NewCompositionOKButton').gui
        test_attribute_toggled(
            self,
            self.new_composition_dialog.isVisible,
            cancel_button.click,
            True
        )
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
