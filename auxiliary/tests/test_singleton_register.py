from auxiliary.tests.loader import *

class A(Singleton):
    pass

@singleton_register('A')
class B(Singleton):
    pass

@singleton_register('A', 'B')
class C(Root):
    pass

class SingletonRegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.a = A()
        self.b = B()
        self.c = C()
    def test1(self):
        self.assertEqual(self.b.A, self.a)
        self.assertEqual(self.c.A, self.a)
        self.assertEqual(self.c.B, self.b)

if __name__ == '__main__':
    unittest.main()
