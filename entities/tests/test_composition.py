from entities.tests.loader import *

class CompositionTestCase(unittest.TestCase):
    pass
#    def test_insert_track(self):
#        added_track = self.composition.tracks[-1]
#        self.assertEqual(added_track.name,
#            Track.create_track_name(1, Instrument().name))
#    def test_insert_beat(self):
#        added_beat = self.composition.beats[-1]

class CompositionConnectedTestCase(unittest.TestCase):
    def setUp(self):
        class A(CompositionConnected):
            pass
        self.inst = A()
    def test_presence(self):
        with self.assertRaises(NotFoundError):
            self.inst.composition
        cmp = Composition()
        self.assertEqual(cmp, self.inst.composition)

if __name__ == '__main__':
    unittest.main()
