
class Animal:
    def __init__(self,name,f):
        self.name = name
        self.f = f   #open('name.txt',what)

    def set_name(self,f):
        f=open('name.txt','w')
        f.write(self.name)
        f = open('name.txt','r')
        a = f.read()
        if len(c) != 0:
            a = self.naem
        else:
            print('设置名字')


    def get_name(self):
        self.name = self.f.read()
        return self.name
    def __del__(self):
        self.f.write(self.name)
        self.f.close()
        print('当前对象被销毁')


dog = Animal('阿拉斯加',open('name.txt','r'))
#dog.f= open('name.txt','r')
print(dog.get_name())

dog.f = open('name.txt','w')
dog.f.write('阿拉斯加')
