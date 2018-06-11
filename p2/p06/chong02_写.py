
class Father(object):
    def kaiche(self):
        print('是个老司机……')

class Son(Father):
    def kaiche(self):
        #Father.kaiche(self)
        #super().kaiche()
        super(Son,self).kaiche()
        print('是个赛车手……')

s = Son()
s.kaiche()
