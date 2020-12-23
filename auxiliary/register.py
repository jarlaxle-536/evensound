class ClassesNotFoundInRegister(Exception):
    pass

class Register:
    classes = dict()
    def add(self, *classes):
        self.classes.update({cls.__name__: cls for cls in classes})
    def get(self, *classes):
        res = tuple([
            self.classes.get(cls) if isinstance(cls, str) else cls
            for cls in classes
        ])
#        print(f'REGISTER:get \n  {classes} => {res}')
        return res
    def find(self, cls):
        return self.get(cls)[0]

REGISTER = Register()
