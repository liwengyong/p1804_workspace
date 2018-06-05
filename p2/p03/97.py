
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

chengguohan=People('稱國漢','2.52 Meter',252)
chengguohan.jump()

caotijing = People('草薙京','1.80 Meter',152)
caotijing.run()

buzhihuowu = People('不知火舞','1.78 Meter',102)
buzhihuowu.zhiquan()

bashengan = People('八神痷','1.82 Meter',156)
bashengan.tang()

dashe = People('大蛇','1.96 Meter',168)
dashe.run()
dashe.jump()
dashe.zhiquan()
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
