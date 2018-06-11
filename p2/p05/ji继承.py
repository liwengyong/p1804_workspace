
class Animal:
    def __init__(self):
        self.__legs = 4
        self.weiba = 1
    def get_legs(self):
        return self.__legs
    def eat(self):
        print('动物天生吃东西能力')
    def drink(self):
        print('动物天生喝水的能力')
    def sleep(self):
        print('倒头就睡的能力')

class Dog(Animal):
    def jiao(self):
        print('小狗 汪汪')

class Shapi(Dog):
    pass

gou = Dog()
ll = gou.get_legs()
print('小狗天生'+str(ll)+'条腿')
