from entities.tests.loader import *

class BeatTestCase(unittest.TestCase):
    def setUp(self):
        self.beat = Beat()
    def test_1(self):
        print('beat:', self.beat)

if __name__ == '__main__':
    unittest.main()
