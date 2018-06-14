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
            x = input('请输入第一个数字')
            while True:
                f = ('请输入运算符')
                if y == 'q':
                    break
                y = int(input('请输入下一个数字'))
                if f == '+':
                    return x+y
                elif f == '-':
                    return x-y
                elif f == '*':
                    return x*y
                elif f == '/':
                     return x/y
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
        jisuanqi.yun_suan(x)
except Exception as n :
    print('程序出了问题:%s'%n)


