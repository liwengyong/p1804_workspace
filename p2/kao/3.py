
class FatherLwy(object):
    aa = None
    def __init__(self,name):
        self.name = name
        print('__init__')
    def __new__(cls,*b):
        if cls.aa == None:
            cls.aa = object.__new__(cls)
        return cls.aa
    def __str__(self):
        return '__str__'
    def __del__(self):
        print('对象调用已删除')

class SonLwy(FatherLwy):
    pass

ll = SonLwy('lwy')
print(ll)
