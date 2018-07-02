
class PeopleLwy(object):
    def __init__(self):
        self.__name = 'liwenyong'
    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name = value
        return self.__name
    property(get_name,get_name)

class ZhangSanLwy(PeopleLwy):
    __money = 0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):
        self.__money = value
        return self.__money

a = PeopleLwy()
print(a.get_name())
print(a.set_name('李文永'))
b = ZhangSanLwy()
print(b.money)
b.money = 25
print(b.money)
