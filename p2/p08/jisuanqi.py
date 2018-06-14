try:
    class Calculator(object):
        __jisuan = None
        __main = False

        def jia(self,x,y):
            return x+y
        def jian(self,x,y):
            return x-y
        def cheng(self,x,y):
            return x*y
        def chu(self,x,y):
            return x/y
        def yun_suan(self,x):
            self.x = x
            while True:
                f = input('请输入运算符号')
                if f == '=':
                    break
                y = int(input('请输入数字'))
                if f == '+':
                    self.x = self.jia(self,x,y)
                elif f == '-':
                    self.x = self.jian(self,x,y)
                elif f == '*':
                    self.x= self.cheng(self,x,y)
                elif f == '/':
                    self.x = self.chu(self,x,y)
                print('运算%d'%self.x)
            print('运算结果:%d'%self.x)
        def __init__(self,name):
            if Calculator.__main == False:
                self.name = name
                Calculator.__main = self.name
        def __new__(cls,*l):
            if cls.__jisuan == None :
                cls.__jisuan = object.__new__(cls)
            return cls.__jisuan
    while True:
        jisuanqi = input('请创建计算器')
        if jisuanqi == 'q':
            break
        jisuanqi = Calculator(jisuanqi)
        print(id(jisuanqi))
        print('%s的计算器为你服务'% jisuanqi.name)
        x = int(input('请输入第一个数字'))
        jisuanqi.yun_suan(x)
except Exception as n :
    print('程序出了问题:%s'%n)


