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

class Root(Basic):
    """Main class to adapt composed elements"""
    field_dependencies = list()
    def __init__(self, **kwargs):
        self.setup()
        super().__init__(**kwargs)
    def __getattr__(self, attr_name):
        """Sufficient for single-level adaptation"""
        for k, v in self.__dict__.items():
            res = getattr(v, attr_name, None)
            if not res is None:
                return res
    def setup(self):
        pass
    def adapt(self, obj, name='adapted', related_name='adapter'):
        setattr(self, name, obj)
        setattr(getattr(self, name), related_name, self)

class Updater:
    """Get-set descriptor for updating elements"""
    source = target = None
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
