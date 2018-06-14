
class GirlFriend(object):
    __girl = None
    __only_you = False
    def __init__(self,name):
        if self.__only_you == False:
            self.name = name
            self.__only_you = True
    def __new__(cls,*args):
        if cls.__girl == None:
            cls.__girl = object.__new__(cls)
        return cls.__girl

girl01 = GirlFriend('哈哈')
print(girl01.name)
girl02 = GirlFriend('呵呵')
print(girl02.name)
print(id(girl01))
print(id(girl02))
