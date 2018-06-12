
class Duck(object):
    def walk(self):
        print('小黄鸭在摇摆着行走……')
    def swim(self):
        print('小黄鸭在湖水中游泳……')

class People(object):
    def walk(self):
        print('老王在摇摆着行走……')
    def swim(self):
        print('老王在湖水中裸泳……')

def Func(obj):   #同样的一个函数，定义的时候 不知道结果是什么
    obj.walk()
    obj.swim()

#好处：1 代码灵活 2. 减少代码 冗余
duck = Duck()
p01 = People()
Func(p01)
Func(duck)
