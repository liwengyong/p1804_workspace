
class Fute:
    def __init__(self):
        self.info = '零件'
        self.lever = 0
    def make(self,t):
        self.lever += t
        if self.lever >= 10 :
            self.info = '您的豪华版天子座驾定制成功，请提走'
        elif self.lever >= 8 :
            self.info = '目前没有敞篷，您确定要提走吗'
        elif self.lever >= 6 :
            self.info = '目前没有天窗，您确定要提走吗'
        elif self.lever >= 5:
            self.info = '目前没有玻璃，您确定要提走吗'
        elif self.lever >= 3:
            self.info = '目前没有车壳，您确定要提走吗'
        else:
            self.info = '瞎着急，连引擎都没有呢'
    def __str__(self):
        return '当前车的状态是:%s,制作这辆车一共用了%d个月时间'%(self.info,self.lever)
class Benchi:
    def __init__(self):
        self.info = '零件'
        self.lever = 0
    def make(self,t):
        self.lever += t
        if self.lever >= 10 :
            self.info = '您的豪华版天子座驾定制成功，请提走'
        elif self.lever >= 8 :
            self.info = '目前没有敞篷，您确定要提走吗'
        elif self.lever >= 6 :
            self.info = '目前没有天窗，您确定要提走吗'
        elif self.lever >= 5:
            self.info = '目前没有玻璃，您确定要提走吗'
        elif self.lever >= 3:
            self.info = '目前没有车壳，您确定要提走吗'
        else:
            self.info = '瞎着急，连引擎都没有呢'
    def __str__(self):
        return '当前车的状态是:%s,制作这辆车一共用了%d个月时间'%(self.info,self.lever)
ft = Fute()
bc = Benchi()
print('欢迎来到我们独家定制豪华座驾')
while True:
    t = int(input('请输入您的预期提车时间'))
    if t == 0 :
        break
    ft.make(t)
    bc.make(t)
    print(ft.info)
    print(bc.info)
print(ft)
print(bc)
