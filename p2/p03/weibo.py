
class WeiBo:
    def __init__(self,name):
        self.info = '生的'
        self.lever = 0
        self.Seasoning = []
        self.name = name
    def cook(self,t):
        self.lever +=t
        if self.lever >=10:
            self.info = '烤糊的黑'+self.name
        elif self.lever >= 8:
            self.info = '火大的黄'+self.name
        elif self.lever >= 6:
            self.info = '微微有点焦的'+self.name
        elif self.lever >=5 :
            self.info = '新鲜出炉的上好'+self.name
        elif self.lever >=3:
            self.info = '半生不熟的'+self.name
        elif self.lever >=1:
            self.info = '还有比这个难吃的东西吗'
        else:
            self.info = '卧槽，还真有'
    def AddSeasoning(self,Seasoning):
        self.Seasoning.append(Seasoning)
    def __str__(self):
        for i in self.Seasoning:
            i = '调料是'+i
            self.info +=i+','
        self.info = self.info.strip('调料有,')
        return '当前 %s 状态是: %s ,烤制此 %s 一共用了 %d 分钟时间'%(self.name,self.info,self.name,self.lever)

print('欢迎使用微波炉')
n = input('请输入要烘焙的东西:')
entity = WeiBo(n)
while True:
    t = int(input('请输入要烘焙的时间:'))
    if t == 0 :
        print('你真的这样就走了吗')
        break
    entity.cook(t)
    l = input('请输入要添加的调料:')
    print(entity.info)
    entity.AddSeasoning(l)
print(entity)


