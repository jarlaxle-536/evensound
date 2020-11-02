import unittest

from gui.mixins import *

class TestApplication():
    def setUp(self):
        self.app = Application()
    def test_keys(self):
        for key in ['gui', 'state']:
            self.assertTrue(hasattr(self.app, key))
