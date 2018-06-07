# coding = utf-8  
class Person(object):  
    """人的类"""  
    def __init__(self,name):  
        self.name = name  
        self.gun = None  
        self.hp = 100  
  
    def install_zidan(self,dan_jia_temp,zi_dan_temp):  
        """把子弹装到弹夹中"""  
        dan_jia_temp.save_zidan(zi_dan_temp)  
  
    def install_danjia(self,gun_temp,dan_jia_temp):  
        """把弹夹装到枪上"""  
        gun_temp.save_danjia(dan_jia_temp)  
  
    def take_gun(self,gun_temp):  
        """拿枪"""  
        self.gun = gun_temp  
  
    def __str__(self):  
        if self.hp > 0:  
            if self.gun:  
                return "%s的血量为:%d,他有枪!%s"%(self.name,self.hp,self.gun)  
            else:  
                return "%s的血量为:%d,他没有枪!"%(self.name,self.hp)  
        else:  
            return "%s已经挂了。。。"%(self.name)  
  
    def shoot(self,enemy):  
        """人开枪"""  
        self.gun.fire(enemy)  
  
    def diaoxue(self,hurt_temp):  
        self.hp -= hurt_temp  
  
  
class Gun(object):  
    """枪的类"""  
    def __init__(self,name):  
        self.name = name  
        self.danjia = None  
  
    def save_danjia(self,dan_jia_temp):  
        """进行弹夹保存"""  
        self.danjia = dan_jia_temp  
  
    def __str__(self):  
        if self.danjia:  
            return "枪的信息为:%s,%s"%(self.name,self.danjia)  
        else:  
            return "枪的信息为:%s,这把枪中没有弹夹"%(self.name)  
  
    def fire(self,enemy):  
        """枪从弹夹中获取子弹，子弹射击敌人"""  
        receive_zidan = self.danjia.huoqu_zidan()  
        if receive_zidan:  
            receive_zidan.dazhong(enemy)  
        else:  
            print("没有子弹了。。。")  
  
class Danjia(object):  
    """弹夹的类"""  
    def __init__(self,max_num):  
        self.max_num = max_num  
        self.danjia_list = []  
  
    def save_zidan(self,zi_dan_temp):  
        """弹夹保存子弹"""  
        self.danjia_list.append(zi_dan_temp)  
  
    def __str__(self):  
        return "弹夹的信息为:%s/%s"%(len(self.danjia_list),self.max_num)  
  
    def huoqu_zidan(self):  
        """获取弹夹中最上面的子弹"""  
        if self.danjia_list:  
            return self.danjia_list.pop()  
        else:  
            return None  
  
class Zidan(object):  
    """子弹的类"""  
    def __init__(self,hurt):  
        self.hurt = hurt  
  
    def dazhong(self,enemy):  
        """打中敌人，敌人掉血"""  
        enemy.diaoxue(self.hurt)  
  
  
  
  
  
def main():  
    #1.创建老王对象  
    laowang = Person("老王")  
  
    #2.创建枪对象  
    ak47 = Gun("AK47")  
  
    #3.创建弹夹对象  
    dan_jia = Danjia(30)  
  
    #4.创建子弹对象  
    for i in range(15):  
        zi_dan = Zidan(10)  
        #5.老王把子弹安装到弹夹中  
        laowang.install_zidan(dan_jia,zi_dan)  
    #6.老王把弹夹安装到枪中  
    laowang.install_danjia(ak47,dan_jia)  
  
    #test弹夹的信息  
    print(dan_jia)  
    #test枪的信息  
    print(ak47)  
  
    #7.老王拿枪  
    laowang.take_gun(ak47)  
  
    #test老王  
    print(laowang)  
  
    #8.创建敌人对象  
    guaishou = Person("怪兽")  
    print(guaishou)  
    #9.老王开枪  
    print("="*20)  #信息分割线  
    print("开始开枪")  
    for i in range(10):  
        laowang.shoot(guaishou)  
        print(guaishou)  
        print(laowang)  
    laowang.shoot(guaishou)  
    print(guaishou)  
    print(laowang)  
  
if __name__ == "__main__":  
    main()  
