from auxiliary import *

class Persistent(Entity):
    db_fields = list()
    def __getstate__(self):
        print(f'calling getstate for {self.__class__.__name__}')
        return {k: getattr(self, k) for k in self.db_fields}
    def __setstate__(self, dct):
        print(f'calling setstate for {self.__class__.__name__}')
        for k, v in dct.items():
            setattr(self, k, v)
