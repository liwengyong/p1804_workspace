
class Cat :
    def eat(self):
        print('%s 喵喵要小魚幹……'%self.name)
    def drink(self):
        print('%s 喵喵要喝奈奈……'%self.name)
    def introduce(self):
        print('我的名字是%s,我今年%d歲了'%(self.name,self.age))

tom = Cat()
tom.age = 60
tom.color = 'blue'
tom.name = '湯姆'
tom.lover = 'jerry'
tom.introduce()
tom.eat()

hongmao = Cat()
hongmao.name = '紅帽'
hongmao.age = 24
hongmao.color = 'red'
hongmao.introduce()
hongmao.drink()
