
class People:
    def __init__(self,name,heigh,weight):
        self.name = name
        self.heigh = heigh
        self.weight = weight

    def jump(self):
        print('%s :You jump!I jump.'% self.name)
    def run(self):
        print('%s :runing……'% self.name)
    def zhiquan(self):
        print('%s :直拳……'% self.name)
    def tang(self):
        print('%s :begin裝傻……'% self.name)

def bisha(item):
    item.jump()
    item.run()
    item.zhiquan()
def bisha2(item):
    item.tang()
    item.jump()
    item.run()
    item.zhiquan()

chengguohan=People('稱國漢','2.52 Meter',252)
bisha(chengguohan)

caotijing = People('草薙京','1.80 Meter',152)
bisha2(caotijing)

bashengan = People('八神痷','1.82 Meter',156)
bisha2(bashengan)

dashe = People('大蛇','1.96 Meter',168)
bisha(dashe)

'''
chengguohan = People()
chengguohan.name = '稱國漢'
chengguohan.height = '2.52 Meter'
chengguohan.weight = 252

caitijing = People()
caitijing.name = '草薙京'
caitijing.height = '1.80 Meter'
caitijinh.weight = 152
'''
