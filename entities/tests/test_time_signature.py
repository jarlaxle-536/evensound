from entities.tests.loader import *

class TimeSignatureTestCase(unittest.TestCase):
    def setUp(self):
        self.ts = TimeSignature()
    def tearDown(self):
        del self.ts
    def test_correct_creation(self):
        for ts_num, ts_den, ratio in [
            (4, 4, 1),
            (6, 4, 1.5),
            (7, 4, 1.75)
        ]:
            self.ts = TimeSignature(numerator=ts_num, denominator=ts_den)
            self.assertEqual(
                [getattr(self.ts, f) for f in [
                    'numerator',
                    'denominator',
                    'ratio'
                ]], [ts_num, ts_den, ratio])

if __name__ == '__main__':
    unittest.main()
