
import random,time
class Xrk:
    def __init__(self,name,hair,color):
        self.name = name
        self.hair = 'flower'
        self.color = 'bulinbulinbulin'
    def Xingwei(self):
        print('%s開始生產陽光'% self.name)
    def __str__(self):
        s = '種植向日葵'+self.name+'開始生產陽光'+xrk.color
        return s
xrk = Xrk('向日葵','花','黃色')
xrk.Xingwei()
print(xrk)
time.sleep(0.2)
print(' ')
class Wd:
    def __init__(self,name,hair,color,power):
        self.name = name
        self.hair = 'leaf'
        self.color = 'green + blue'
        self.power = str(random.randint(1,25))
    def xingwei(self):
        print('搖了搖搖了頭並且醞釀發炮')
    def __str__(self):
        s = '投放'+self.name+'然後血量爲'+self.power
        return s
wd = Wd('豌豆','葉子','綠色和藍色','血量')
print(wd)
wd.xingwei()
time.sleep(0.2)
print(' ')
class Jg:
    def __init__(self,name,power,species):
        self.name = name
        self.power = str(random.randint(1,25))
        self.species = '肉'
    def xingwei(self):
        print('成功阻擋了僵屍的一次進攻')
    def __str__(self):
        s = '投放堅果'+self.name+'然後血量为'+self.power
        return s
jg = Jg('堅果','血量','肉')
print(jg)
jg.xingwei()
time.sleep(0.2)
print(' ')
class Js:
    def __init__(self,color,power,species,speed):
        self.color = '灰色'
        self.power = str(random.randint(1,25))
        self.species = '啊啊啊'
        self.speed = '较快'
    def xingwei(self):
        print('边跑边跳，被坚果挡住了')
        time.sleep(0.2)
        print('边跑边跳，吃掉了你的叶子')
        time.sleep(0.2)
        print('边跑边跳，吃掉了你的脑子')
        time.sleep(0.2)
    def __str__(self):
        s = '僵尸来了'+self.species+'血量是'+self.power
        return s
js = Js('灰色','血量','类型','sudo')
print(js)
js.xingwei()
