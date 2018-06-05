
class People:
    def eat(self): #行爲  方法
        print('吃吃吃!!!')
    def work(self):
        print('工作ing……')

xiaohong = People()   #調用人類創建 具體的 xiaohong 對象
a = xiaohong.age = 20  #給對象設置屬性
print(a)
xiaohong.name = 'xiaozhang'   #給對象設置屬性
xiaohong.eat()   # 具體對象 執行 繼承的能力
xiaohong.work()
