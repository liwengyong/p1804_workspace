
class People(object):
    def __init__(self):
        self.__money = 1
    def get_money(self):
        return self.__money
    def set_money(self,value):
        self.__money = value
    #通过property 把set,get 方法属性化，可以直接使用
    money = property(get_money,set_money)

class People1(object):
    def __init__(self):
        self.__money = 1
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):   #注解方法 装饰器
        if isinstance(value,int):
            self.__money = value
        else:
            print(value)
    #通过property 把set,get 方法属性化，可以直接使用


p = People1()
print(p.money)
p.money = 25252525
print(p.money)
#print(p.get_money())
#p.set_money(999)
#print(p.get_money())
