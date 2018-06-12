
class Dog(object):
    def game(self):
        return ('普通狗只是简单的玩耍')

class XiaoTianQuan(Dog):
    def game(self):
        return ('哮天犬需要在天上玩耍')
class Person(object):
    def play_with_dog(self,dog):
        print('杨戬带着',dog.game())


d = Dog()
p = Person()
p.play_with_dog(d)
