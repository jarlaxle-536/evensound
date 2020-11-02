import unittest

from gui.general import *

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    def test_keys(self):
        for key in ['gui', 'state']:
            self.assertTrue(hasattr(self.app, key))
