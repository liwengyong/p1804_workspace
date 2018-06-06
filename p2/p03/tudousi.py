
class Tudousi:
    def __init__(self):
        self.info = '生的'
        self.lever = 0
        self.Seasoning = []
    def cook(self,t):
        self.lever += t
        if self.lever >= 8 :
            self.info = '烤糊的土豆丝'
        elif self.lever >= 6 :
            self.info = '火大了的土豆丝'
        elif self.lever >= 5:
            self.info = '新鲜出锅的上好土豆丝'
        elif self.lever >= 3:
            self.info = '半生不熟的土豆丝'
        else:
            self.info = '生土豆丝'
    def AddSeasoning(self,Seasoning):
        self.Seasoning.append(Seasoning)
    def __str__(self):
        for i in self.Seasoning:
            i ='调料是'+i
            self.info += i+','
        self.info = self.info.strip('调料有,')
        return '当前土豆丝状态是:%s,炒这盘土豆丝一共用了%d分钟时间'%(self.info,self.lever)

dg01 = Tudousi()
print('欢迎品尝土豆丝')
while True:
    t = int(input('请输入炒土豆丝的时间'))
    if t == 0 :
        break
    dg01.cook(t)
    l = input('请输入要添加的调料')
    print(dg01.info)
    dg01.AddSeasoning(l)
print(dg01)
