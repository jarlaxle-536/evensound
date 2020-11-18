from entities.tests.loader import *

class TrackTestCase(unittest.TestCase):
    def setUp(self):
        self.track = Track()
    def test_1(self):
        print('track:', self.track)
        print(self.track.__dict__)

if __name__ == '__main__':
    unittest.main()
