import inspect
import sys

class Updater:
    """Getset descriptor, on source value change calls .update() for all specified gui elements"""
    source = None
    targets = list()
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def __set_name__(self, owner, name):
        self.__name = name
    def __getattr__(self, attr):
        return getattr(self.source, attr)
    def __get__(self, instance, owner):
        dct = instance.__dict__
        dct.setdefault(self.__name, self.source)
        return dct[self.__name]
    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value
        defined = dict(inspect.getmembers(sys.modules['__main__']))
        for target_cls_name in self.targets:
            target_cls = defined.get(target_cls_name, None)
            for instance in getattr(target_cls, 'instances', list()):
                instance.setup()

class TrackListUpdater(Updater):
    targets = [
        'TracksList'
    ]
