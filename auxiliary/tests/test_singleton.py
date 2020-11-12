import unittest

from auxiliary.general import *

class A(Singleton):
    pass

class SingletonTestCase(unittest.TestCase):
    def setUp(self):
        self.cls = A
    def test_object_not_created_twice(self):
        a, b = [self.cls() for i in range(2)]
        self.assertEqual(a, b)
        self.assertEqual(a, self.cls.instance)
    def test_find(self):
        a = self.cls()
        self.assertEqual(a, self.cls.find('A',
            modules=['__main__', 'auxiliary.tests.test_singleton']))
