from entities.tests.loader import *

class SoundTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_note_repr(self):
        sound1 = Sound(pitch=24)
        sound2 = Sound(pitch=42)
        self.assertEqual(sound1.note, 'C1')
        self.assertEqual(sound2.note, 'F#2')

if __name__ == '__main__':
    unittest.main()
