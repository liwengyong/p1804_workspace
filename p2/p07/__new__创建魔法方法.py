
class Car(object):
    def __init__(self,name):
        self.name = name
        print('----__init__方法被调用----')
    def __del__(self):
        print('-----__del__方法被调用————')
    def __new__(cls,*k,**kv):
        print('----__new__方法被调用----')
        return object.__new__(cls)

c = Car('大众')
c1 = Car('宝马')
print(id(c))
print(id(c1))

def Tool(a,*b,**c):
    print(a)
    print(b)
    print(c)

Tool(1,'a','b','c',{'k','v'})

'''
class Father(object):
    def kaiche(self):
        print('老司机')
class son(Father):
    def kaiche(self,name):
        if name == '好朋友':
            Father.kaiche(self)
        else:
            print('我是一个赛车手')

s = son()
s.kaiche(s)
'''
