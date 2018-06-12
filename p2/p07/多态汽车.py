
class Car(object):
    def __init__(self,name):
        self.name = name
    def feiben(self):
        return('汽车飞奔')

class DaZhong(Car):
    def feiben(self):
        return('汽车大众式飞奔')
class BaoMa(Car):
    def feiben(self):
        return('汽车宝马式飞奔')
class BenChi(Car):
    def feiben(self):
        return('汽车奔驰式飞奔')

class People(object):
    def __init__(self,name):
        self.name = name
    def drive_car(self,car):
        print('%s 开着 %s %s 中泡妞'%(self.name,car.name,car.feiben()))
        #return self.name + '开着' + car.name + car.feiben() + '中泡妞'

dazhong = DaZhong('一汽本田')
baoma = BaoMa('七系宝马')
benchi = BenChi('传说中的大奔')
p1 = People('哪吒')
print(p1.drive_car(dazhong))
print(p1.drive_car(baoma))
print(p1.drive_car(benchi))
