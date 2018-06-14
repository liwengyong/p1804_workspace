try:
    class Fa(object):
        aa=None
        bb=True
        def __init__(self,name):
            if Fa.bb==True:
                self.name=name
                Fa.bb=self.name
        def cheng(self,a,b):
            return a*b
        def chu(self,a,b):
            return a/b
        def jia(self,a,b):
            return a+b
        def jian(self,a,b):
            return a-b
        def jisuan(self,a):
            self.a=a
            while True:
                fuhao=input('请选择运算符号')
                if fuhao=='=':
                    break
                b=int(input('请输入运算数字'))
                if fuhao=='+':
                    self.a=self.jia(self.a,b)
                elif fuhao=='-':
                    self.a=self.jian(self.a,b)
                elif fuhao=='*':
                    self.a=self.cheng(self.a,b)
                elif fuhao=='/':
                    self.a=self.chu(self.a,b)
                print('运算%d'% self.a)
            print('运算结果：%d'%self.a)

        def __new__(cls,*k):
            if cls.aa==None:
                cls.aa=super().__new__(cls)
            return cls.aa
    while True:
        dui=input('你想要创建的计算机名字')
        if dui=='q':
            break
        dui=Fa(dui)
        print(id(dui))
        print('%s牌计算机为你服务'% dui.name)
        a=int(input('请输入第一个运算数字'))
        dui.jisuan(a)
except Exception as r:
    print('程序跑报错了：%s'%r)

