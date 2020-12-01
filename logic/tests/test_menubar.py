from logic.tests.loader import *

class MenubarTest(unittest.TestCase):
    def setUp(self):
        init_test_app(self)
        self.menubar = self.MainWindow.gui.menuBar()
        self.present_menus = [obj for obj in self.menubar.children()
            if obj.__class__.__name__ == 'QMenu']
        self.file_menu = self.present_menus[0]
        self.file_menu_actions = [obj for obj in self.file_menu.children()
            if obj.__class__.__name__ == 'QAction']
        self.present_menu_titles = list(ACTION_TEXTS.values())
        self.new_composition_action = [a for a in self.file_menu_actions
                    if a.text() == ACTION_TEXTS['NewCompositionAction']][0]
        self.new_composition_dialog = Singleton.find('NewCompositionDialog').gui
        self.composition = Singleton.find('Composition')
        self.composition.title = DEFAULT_COMPOSITION_TITLE
    def test_file_menu_general(self):
        self.assertEqual(self.file_menu.title(), 'File')
        for t in self.present_menu_titles:
            self.assertIn(t, [a.text() for a in self.file_menu_actions])
    def test_new_cmp_action(self):
        "Check dialog properties"
        self.assertEqual(self.new_composition_dialog.windowTitle(),
            DIALOGS_TITLES['NewCompositionDialog'])
        "Verify dialog visibility"
        test_attribute_toggled(
            self,
            self.new_composition_dialog.isVisible,
            self.new_composition_action.trigger,
            False
        )
    def test_new_cmp_dialog_randomize_title_button(self):
        self.new_composition_action.trigger()
        title1 = self.composition.title
        randomize_button = Singleton.find('RandomizeCompositionTitleButton').gui
        randomize_button.click()
        title2 = self.composition.title
        self.assertNotEqual(title1, title2)
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
        composition = Singleton.find('Composition')
        self.new_composition_action.trigger()
        cancel_button = Singleton.find('NewCompositionOKButton').gui
        test_attribute_toggled(
            self,
            self.new_composition_dialog.isVisible,
            cancel_button.click,
            True
        )
        data = Singleton.find('NewCompositionWidget').acquire()
        self.assertIn('title', data)
    def test_state_general(self):
        "Verify composition is present in state instance dict"
        self.assertIn('composition', self.Application.state.__dict__)
        "Verify attached-to-state composition title"
        self.assertEqual(self.Application.state.composition.title,
            DEFAULT_COMPOSITION_TITLE)
    def test_composition_general(self):
        "Verify default composition title"
        cmp = Composition()
        self.assertEqual(cmp.title, DEFAULT_COMPOSITION_TITLE)

PRESENT_MENUS = [
    'File',
]
DEFAULT_COMPOSITION_TITLE = Composition.title
DIALOGS_TITLES = {k: Root.find_class(k).title for k in [
    'NewCompositionDialog'
]}
ACTION_TEXTS = {k: Root.find_class(k).text for k in [
    'NewCompositionAction'
]}

if __name__ == '__main__':
    unittest.main()
