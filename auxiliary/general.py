from .loader import *

class Root(object):
    """Main class to adapt composed elements"""
    instances = dict()
    fields = list()
    def __init__(self, **kwargs):
        for k in self.fields:
            setattr(self, k, kwargs.get(k, getattr(self, k)))
        self.setup()
    def __getattr__(self, attr_name):
        """Single-level adaptation"""
        for k, v in self.__dict__.items():
            res = getattr(v, attr_name, None)
            if not res is None:
                return res
    def setup(self):
        print(f'{self.__class__.__name__} SETUP.')
    def adapt(self, obj, name='adapted', related_name='adapter'):
        setattr(self, name, obj)
        setattr(getattr(self, name), related_name, self)
    @staticmethod
    def find_class(cls_name, modules=['__main__']):
        defined = dict()
        for m in modules:
            if m in sys.modules:
                defined.update(dict(inspect.getmembers(sys.modules[m])))
        return defined.get(cls_name)
    @classmethod
    def test_constructor_kwargs(cls, kwargs):
#        print(f'Testing if {kwargs} are suitable for {cls.__name__}')
        return True

class Entity(Root):
    def __new__(cls, *args, **kwargs):
        obj_id = cls.get_id(kwargs)
        if cls.instances.get(obj_id) is None:
            cls.register(obj_id=obj_id, **kwargs)
        return cls.instances[obj_id]
    @classmethod
    def register(cls, obj_id, **kwargs):
        if not cls.test_constructor_kwargs(kwargs): return
        cls.instances = cls.instances.copy()
        cls.instances[obj_id] = object.__new__(cls)
        return cls.instances[obj_id]
    @staticmethod
    def get_id(dct):
        return random.getrandbits(128)
    @classmethod
    def clear(cls):
        cls.instances = dict()

def entity_field_hr(fieldname):
    return fieldname.replace('_', ' ').capitalize()

class NotFoundError(Exception): pass

class Singleton(Entity):
    key = 'object'
    @staticmethod
    def get_id(dct):
        return Singleton.key
    @staticmethod
    def find(cls_name, obj_id=None, modules=['__main__']):
        cls = Root.find_class(cls_name, modules)
#        if not cls.key in cls.instances:
#            raise NotFoundError()
        return cls.instances.get(cls.key)

# class decorator for singleton object finding
def singleton_register(*singleton_classes):
    def getter(cls_name):
        def meth(instance):
            if not getattr(instance, f'_{cls_name}'):
                setattr(instance, f'_{cls_name}', Singleton.find(cls_name))
            return getattr(instance, f'_{cls_name}')
        return meth
    def wrapper(cls, *args, **kwargs):
        for singleton_cls_name in singleton_classes:
            setattr(cls, singleton_cls_name,
                property(getter(singleton_cls_name)))
        return cls
    return wrapper
