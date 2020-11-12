import unittest

from auxiliary.general import *

class SingletonTestCase(unittest.TestCase):
    def setUp(self):
        class A(Singleton):
            pass
        self.cls = A
    def test_object_not_created_twice(self):
        a, b = [self.cls() for i in range(2)]
        self.assertEqual(a, b)
