
class SweetPotato:
    def __init__(self):
        self.info = '生地瓜'
        self.lever = 0
        self.Seasoning = []
    def cook(self,t):
        self.lever += t
        if self.lever >= 8 :
            self.info = '烤糊的黑地瓜'
        elif self.lever >= 6 :
            self.info = '火大的黄地瓜'
        elif self.lever >= 5:
            self.info = '新鲜出 出炉的上好烤地瓜'
        elif self.lever >= 3:
            self.info = '半生不熟的硬地瓜'
        else:
            self.info = '生地瓜'
    def AddSeasoning(self,Seasoning):
        self.Seasoning.append(Seasoning)
    def __str__(self):
        for i in self.Seasoning:
            i ='调料是'+i
            self.info += i+','
        self.info = self.info.strip('调料有,')
        return '当前地瓜状态是:%s,烤制此地瓜一共用了%d分钟时间'%(self.info,self.lever)

dg01 = SweetPotato()
print('欢迎品尝烤地瓜')
while True:
    t = int(input('请输入烤地瓜时间'))
    if t == 0 :
        break
    dg01.cook(t)
    l = input('请输入要添加的调料')
    print(dg01.info)
    dg01.AddSeasoning(l)
print(dg01)
