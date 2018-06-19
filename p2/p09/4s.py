
class Car(object):

    def move(self):
        print('-----车在移动-----')

    def stop(self):
        print('-----停车-----')

class CarStore(object):
    def order(self):
        self.car = Car()
        self.car.move()
        self.car.stop()
