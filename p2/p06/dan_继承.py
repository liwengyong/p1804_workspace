
class Father(object):
    def __init__(self):
        self.xing = '王'
        self.__height = '155'
    def kaiche(self):
        print('是个老司机……')
    def __dubo(self):
        print('赌博赖帐，卖媳妇。')
class Son(Father):
    pass
    def kaiche(self):
        print('是个赛车手')
大头儿子 = Son()
大头儿子.xing = '西门'

print(大头儿子.xing)
大头儿子.height = '180'
print(大头儿子.height)
大头儿子.kaiche()

