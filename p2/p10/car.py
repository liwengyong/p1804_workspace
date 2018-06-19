
class CarStore(object):
    def createCar(self,name):
        pass
    def neng(self,name):
        self.car = self.createCar(name)
        self.car.move()
        self.car.stop()
        self.chang = chang()
        return self.chang.createCar(name)

class car(object):
    def move(self):
        print('----动了----')
    def stop(self):
        print('----又停了-----')

class SonCar(car):
    pass

class chang(object):
    def createCar(self,name):
        self.name = name
        name = input('请输入车')
        if self.name == name :
            self.car = SonCar()
        return self.car
name = CarStore()
name.neng(name)
