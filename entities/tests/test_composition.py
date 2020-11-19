from entities.tests.loader import *

class CompositionTestCase(unittest.TestCase):
    def setUp(self):
        self.composition = Composition()
    def tearDown(self):
        self.composition = None
    def test_insert_track(self):
        added_track = self.composition.tracks[-1]
        self.assertEqual(added_track.name,
            Track.create_track_name(1, Instrument().name))
    def test_insert_beat(self):
        added_beat = self.composition.beats[-1]

if __name__ == '__main__':
    unittest.main()
