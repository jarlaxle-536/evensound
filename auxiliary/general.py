import inspect
import sys

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
    fields = list()
    def __init__(self, **kwargs):
        for k in self.fields:
            setattr(self, k, kwargs.get(k, None))
        self.setup()
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

class Singleton(Root):
    instance = None
    objects = dict()
    def __new__(cls, *args, **kwargs):
        if getattr(cls, 'instance') is None:
            cls.instance = object.__new__(cls)
        return cls.instance
    def find(self, cls_name):
        defined = dict(inspect.getmembers(sys.modules['__main__']))
        self.objects[cls_name] = defined.get(cls_name, None).instance
        return self.objects[cls_name]

class Entity(Root):
    instances = dict()
    def __new__(cls, *args, **kwargs):
        obj_id = cls.get_id(kwargs)
        if cls.instances.get(obj_id) is None:
            cls.instances[obj_id] = object.__new__(cls)
        return cls.instances[obj_id]
