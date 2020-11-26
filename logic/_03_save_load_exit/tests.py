import unittest
from PyQt5 import QtTest

from logic.auxiliary import *
from logic._03_save_load_exit import *

class UnitTest(unittest.TestCase):
    def setUp(self):
        init_test_app(self)

if __name__ == '__main__':
    unittest.main()
