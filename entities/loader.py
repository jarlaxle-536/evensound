import random
import pygame.midi
import shelve
import heapq

from config import *
from data_loader import *
from auxiliary import *

from scripts.midi_output_handlers import *

class CompositionNotFoundError(Exception): pass

class CompositionConnected(Root):
    @property
    def composition(self):
        if not getattr(self, '_composition'):
            self._composition = Singleton.find('Composition')
#            if self._composition is None:
#                raise CompositionNotFoundError()
        return self._composition
