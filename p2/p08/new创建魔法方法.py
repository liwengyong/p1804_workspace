
class Car(object):
    __instace = None   #用于保存实例化的对象
    __init_flag = True   # 表示 init 一次都没有执行
    def __init__(self,name):
        if Car.__init_flag == True:   #这里表示第一次执行
            self.name = name
            Car.__init_flag = False   #标记为已经执行了一次了，以后不要再执行了
    def __new__(cls,*k):
        if cls.__instace == None:   #表示第一次 创建实例对象
            cls.__instace = object.__new__(cls)
        return cls.__instace   #将对象的引用传递到init中

c1 = Car('奔驰')
print(c1.name)
c2 = Car('宝马')
print(c2.name)
print(id(c1))
print(id(c2))
