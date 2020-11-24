from entities.tests.loader import *

class SoundTestCase(unittest.TestCase):
    def setUp(self):
        self.sound = Sound()
        print(self.sound)
    def tearDown(self):
        del self.sound
    def test_note_repr(self):
        self.sound.pitch = 24
        self.assertEqual(self.sound.note, 'C1')
        self.sound.pitch = 42
        self.assertEqual(self.sound.note, 'F#2')

if __name__ == '__main__':
    unittest.main()
