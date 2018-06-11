
class Donkey(object):
    def manzou(self):
        print('走路慢……')
    def jiao(self):
        print('驴在欢叫%……')

class Horse(object):
    def naili(self):
        print('马力足，持久强……')
    def jiao(self):
        print('马在嘶鸣')

class Mule(Donkey,Horse):
    pass
    def jiao(self):
        print('骡子在唱歌')

骡子一号 = Mule()
骡子一号.manzou()
骡子一号.naili()
骡子一号.jiao()
print(Mule.__mro__)

