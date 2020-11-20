from entities.tests.loader import *

class InstrumentTestCase(unittest.TestCase):
    def setUp(self):
        self.instrument = Instrument()
    def tearDown(self):
        Instrument.instances = dict()
    def test_defaults(self):
        self.assertEqual(self.instrument.program_code, Instrument.program_code)
        self.assertEqual(self.instrument.name,
            MIDI_CODES_FLATTENED.get(str(self.instrument.program_code)))

if __name__ == '__main__':
    unittest.main()
