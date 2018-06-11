
import sys
class People:
    def __init__(self,name,salary):
        self.__name = name
        self.salary = salary
class Worker:
    def __init__(self,name,salary):
        self.__name = name
        self.salary = salary

hua01 = People('小花01',5000)
hua02 = hua01
hua03 = hua01
print(sys.getrefcount(hua01))    #对象被引用了多少次，数量显示要比实际引用次数多1
print(isinstance(hua03,People))   #查询对象是否属于指定的类
