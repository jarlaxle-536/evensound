from .base import *

class Adaptable(Base):
    _adapted = dict()
    def adapt(self, obj, name=None):
#        print(f'{self}:adapt "{name}" \n  {obj}')
#        name = name or obj.__class__.__name__
        if obj is None: return
        setattr(self, name, obj)
        setattr(obj, 'adapter', self)
        self._adapted = self._adapted.copy()
        self._adapted[name] = obj
    def __getattr__(self, attr_name):
        res = None
        for adapted_name in self.__dict__.get('_adapted', list()):
            obj = getattr(self, adapted_name)
            found = getattr(obj, attr_name, None)
            if not found is None:
                res = found
                break
#        print(f'{self}:getattr {attr_name}\n  {res}')
        return res
