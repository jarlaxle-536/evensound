from entities.tests.loader import *

class TimeSignatureTestCase(unittest.TestCase):
    def setUp(self):
        self.ts = TimeSignature()
    def tearDown(self):
        del self.ts
    def test_defaults(self):
        self.assertEqual(
            (self.ts.numerator, self.ts.denominator, self.ts.ratio),
            (4, 4, 1)
        )
    def test_custom(self):
        self.ts = TimeSignature(numerator=6, denominator=4)
        self.assertEqual(
            (self.ts.numerator, self.ts.denominator, self.ts.ratio),
            (6, 4, 1.5)
        )

if __name__ == '__main__':
    unittest.main()
