from auxiliary.gui_templates import *

def test():
    class A(Singleton):
        pass
    a1, c1 = A.get_or_create()
    a2, c2 = A.get_or_create()
    assert a1 == a2
    assert c1
    assert not c2

if __name__ == '__main__':
    test()
