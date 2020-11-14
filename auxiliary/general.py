import inspect
import sys

class Root(object):
    """Main class to adapt composed elements"""
    fields = list()
    def __init__(self, **kwargs):
        for k in self.fields:
            setattr(self, k, kwargs.get(k, getattr(self, k)))
        self.setup()
    def __getattr__(self, attr_name):
        """Sufficient for single-level adaptation"""
#        print(f'getting {attr_name} of {self}')
        for k, v in self.__dict__.items():
            res = getattr(v, attr_name, None)
            if not res is None:
                return res
    def setup(self):
        print(f'{self.__class__.__name__} SETUP.')
    def adapt(self, obj, name='adapted', related_name='adapter'):
        setattr(self, name, obj)
        setattr(getattr(self, name), related_name, self)

class Singleton(Root):
    instance = None
    def __new__(cls, *args, **kwargs):
        if getattr(cls, 'instance') is None:
            cls.instance = object.__new__(cls)
        return cls.instance
