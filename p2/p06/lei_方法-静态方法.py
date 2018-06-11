
class People(object):
    guoji = 'china'   #类属性
    def __init__(self):
        self.name = '小明'   #实例属性

    def get_name(self):
        return self.name
    @classmethod
    def get_guoji(cls):
        return cls.guoji

    @classmethod
    def say_chinese(c):
        print('巴拉巴拉……中国话')

    @classmethod
    def set_chinese(cls):
        cls.guoji = '中国'

    @staticmethod
    def shengqi():  #静态方法
        print('生气了')

People.shengqi()

class Tools(object):
    @staticmethod
    def menu():
        print('*'*10)
        print('1.上上签')
        print('2.桃花签')
        print('3.事业签')
        print('*'*10)

    @staticmethod
    def print_s(s):
        print(s,'1804班级制作')
Tools.menu()
Tools.print_s('hello world')
#people01 = People()

#print(people01.guoji)
#people01.guoji = 'usa'

#print(People.guoji)
#print(people01.guoji)
#del people01.guoji
#print(people01.guoji)
#xiaoming = People()
#print(xiaoming.name)
#print(xiaoming.get_name)

#xiaohua = People()
#print(xiaohua.get_name()

