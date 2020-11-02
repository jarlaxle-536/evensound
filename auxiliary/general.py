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

class Root(metaclass=Meta):
    """Main class to adapt composed elements"""
    adapted_name = 'adapted'
    constructor = lambda *args, **kwargs: None
    constructor_args = tuple()
    constructor_kwargs = dict()
    def __init__(self, **kwargs):
        for cls in self.__class__.__bases__:
            cls.adapt(self)
        self.setup()
    @classmethod
    def adapt(cls, inst):
        setattr(inst, cls.adapted_name, cls.create_object())
    @classmethod
    def create_object(cls):
        return cls.constructor(*cls.constructor_args, **cls.constructor_kwargs)
    def setup(self):
        pass
    def update(self):
        pass
    def __getattr__(self, attr_name):
        return getattr(self, attr_name)

class Updater:
    """Get-set descriptor for updating elements"""
    source = target = None
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
