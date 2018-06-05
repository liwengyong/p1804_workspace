
class Car:
    def __init__(self,lz_num,color,name):
        self.lunzi = lz_num
        self.color = color
        self.name = name
    def run(self):
        print('%s的%s跑起來了%d個輪子跑得飛快'% (self.color,self.name,self.lunzi))
    def shout(self):
        print('%s的%s大聲吼叫%d個輪子跑得飛快'% (self.color,self.name,self.lunzi))
    def zhuiwei(self):
        print('%s的%s準備要追別人的尾了%d個輪子跑得飛快'% (self.color,self.name,self.lunzi))

    def __str__(self):
        s = '車的名字是:'+self.name+'車的顏色是:'+self.color
        return s
bmw = Car(8,'紅色','寶馬')
print('汽車的名稱是:',bmw)
print('寶馬的內存地址是%d'%id(bmw))
'''
bmw.name = '寶馬'
bmw.run()
bmw.shout()
bmw.zhuiwei()
print('$'*52)
#print('奧迪的內存地址是%d'%id(aodi))
aodi = Car(3,'綠色')
aodi.name = '奧迪'
aodi.run()
aodi.shout()
aodi.zhuiwei()
'''
