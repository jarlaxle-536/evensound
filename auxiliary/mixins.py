class Meta(type):
    def __new__(cls, clsname, bases, clsdict):
#        print(cls, clsname, bases, clsdict)
        Meta.set_updatable_fields(clsdict)
        return super().__new__(cls, clsname, bases, clsdict)
    def set_updatable_fields(clsdict):
        field_dependencies = clsdict.get('field_dependencies', list())
#        print('field deps:', field_dependencies)
        for target, source in field_dependencies:
            "field_dependencies 'keys' should be defined in clsdict"
#            print(f'will trigger {target}.update() on change of "{source}".')
            clsdict[target] = Updater(target=target, source=source)

class Root(metaclass=Meta):
    constructor_args = tuple()
    constructor_kwargs = dict()
    def __init__(self, **kwargs):
        self.adapt()
        super().__init__(**kwargs)
    def adapt(self):
        for base in self.__class__.__bases__:
            setattr(self, base.adapted_name, base.create_object())
    @classmethod
    def create_object(cls):
        obj = cls.constructor(*cls.constructor_args, **cls.constructor_kwargs)
        return obj

class Updater:
    source = target = None
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class GuiAdapterMixin(Root):
    adapted_name = 'gui'

class StatefulMixin(Root):
    adapted_name = 'state'
