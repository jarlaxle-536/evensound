from .entity import *

class Singleton(Entity):
    @classmethod
    def get_id(cls, **kwargs):
        return 0
    @classmethod
    def object(cls):
        return cls._instances.get(0, DummyObject.get_or_create()[0])

class DummyObject(Singleton):
    def __getattr__(self, attr_name):
        return self
    def __call__(self, *args, **kwargs):
        print(f'{self} called with {args}, {kwargs}')
