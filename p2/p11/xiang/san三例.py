
class Class(object):
    aa = None
    bb =  0
    def __init__(self,):
        pass
    def __new__(cls):
        if cls.bb <= 3 or cls.aa == None:
            cls.aa = object.__new__(cls)
            cls.bb += 1
        #else:
        return cls.aa


c = Class()
print(id(c))
print(c)
d = Class()
print(id(d))
print(d)
e = Class()
print(id(e))
print(e)
f = Class()
print(id(f))
print(f)
g = Class()
print(id(g))
print(g)
h = Class()
print(id(h))
print(h)
