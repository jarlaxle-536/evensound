from auxiliary.tests.loader import *

class A(Singleton):
    pass

class B(Singleton):
    pass

class SingletonTestCase(unittest.TestCase):
    def setUp(self):
        self.cls1 = A
        self.cls2 = B
    def test_object_not_created_twice(self):
        a1, a2 = [self.cls1() for i in range(2)]
        print(a1, a2)
        self.assertEqual(a1, a2)
        self.assertEqual(a1, self.cls1.instances[Singleton.key])
    def test_find(self):
        a = self.cls1()
        self.assertEqual(a, self.cls1.find('A',
            modules=['__main__', 'auxiliary.tests.test_singleton']))
    def test_no_collisions(self):
        a, b = self.cls1(), self.cls2()
        self.assertTrue(isinstance(a, self.cls1))
        self.assertTrue(isinstance(b, self.cls2))

if __name__ == '__main__':
    unittest.main()
