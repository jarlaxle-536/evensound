class Meta(type):
    """Main metaclass"""
    def __new__(cls, clsname, bases, clsdict):
        clsdict = Meta.set_updatable_fields(clsdict)
        return super().__new__(cls, clsname, bases, clsdict)
    def set_updatable_fields(clsdict):
        field_dependencies = clsdict.get('field_dependencies', list())
        for target, source in field_dependencies:
            clsdict[target] = Updater(target=target, source=source)
        return clsdict

class Basic(metaclass=Meta):
    def __init__(self, **kwargs):
        pass
    def setup(self, **kwargs):
        pass

class Root(Basic):
    """Main class to adapt composed elements"""
    field_dependencies = list()
    def __init__(self, cls=None, **kwargs):
        cls = cls if not cls is None else self.__class__
        cls.setup(self, **kwargs)
        next_class = self._next_class()
        if not next_class is object:
            self.__init__(cls=next_class, **kwargs)
    def setup(self, **kwargs):
        pass
    @property
    def mro_list(self):
        if not hasattr(self, '_mro_list'):
            self._mro_list = iter(self.__class__.mro()[1:])
        return self._mro_list
    def _next_class(self):
#        print(list(self.mro_list))
        return next(self.mro_list)

class Updater:
    """Get-set descriptor for updating elements"""
    source = target = None
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
