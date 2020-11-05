import unittest
import os

from auxiliary.general import *
from entities.state import *

class StateTestCase(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.original_state_dict = self.state.__dict__.copy()
        self.test_filepath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'state.cmp')
    def tearDown(self):
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)
    def test_saving(self):
        self.state.save(self.test_filepath)
        self.state.load(self.test_filepath)
        self.assertEqual(self.original_state_dict, self.state.__dict__)
