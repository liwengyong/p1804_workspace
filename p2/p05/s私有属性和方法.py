
class People:
    def __init__(self,name,salary):
        self.__name = name   #申明了这个属性为类私有
        self.salary = salary

    def get_name(self):
        return self.__name
    def set_name(self,n):
        self.naem = n
        return self.__name
    def get_salary(self):
        return self.salary

    def send_msg(self):
        print('发送成功')
    def get_msg(self):
        return self.__send_msg()

xiaohua = People('小花',6000)
print(xiaohua.get_name())
xiaohua.set_name('小白')
print(xiaohua.get_name)

laowang = People('老王',2000)
laowang.send_msg()
