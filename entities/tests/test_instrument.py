from entities.tests.loader import *

class InstrumentTestCase(unittest.TestCase):
    def setUp(self):
        self.instrument = Instrument()
    def test_1(self):
        print('instrument:', self.instrument)

if __name__ == '__main__':
    unittest.main()
