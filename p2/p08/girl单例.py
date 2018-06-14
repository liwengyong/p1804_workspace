
class Wife(object):
    __instace = None
    __init_flag = False
    def __init__(self,name):
        if Wife.__init_flag == False:
            self.name = name
            Wife.__init_flag = True
    def __new__(cls,*k):
        if cls.__instace == None:
            cls.__instace = object.__new__(cls)
        return cls.__instace

girl = Wife('1号')
print(girl.name)
girlfriend = Wife('2号')
print(girlfriend.name)
print(id(girl))
print(id(girlfriend))


