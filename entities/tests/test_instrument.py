from entities.tests.loader import *

class InstrumentTestCase(unittest.TestCase):
    def setUp(self):
        self.instrument = Instrument()
    def test_defaults(self):
        print('instrument:', self.instrument.__dict__)
        """instrument default program code is its' class one"""
        self.assertEqual(self.instrument.program_code, Instrument.program_code)

if __name__ == '__main__':
    unittest.main()
