
class People:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.gun = None  #枪

    def __str__(self):
        return self.name+'剩余血量为:'+str(self.hp)

    def Loading(self,gun,clip,bullet):  #安子弹 弹夹 子弹
        clip.Save(bullet)  #枪保存子弹

    def SecuriltyClip(self,gun,clip):   #安弹夹 枪 弹夹
        gun.connection(clip)   #枪连接弹夹

    def TakeAGun(self,gun):   #拿枪
        self.gun = gun

    def Shou(self,enemy):   #开枪 敌人
        self.gun.she(enemy)

    def BllodDrop(self,killed):   #掉血 杀伤了
        self.hp -= killed

class Clip:
    def __init__(self,capacity):  # 容量
        self.capacity = capacity
        self.capList = []

    def __str__(self):
        return '弹夹当前的子弹数量为:' + str(len(self.capList)) + '/' + str(self.capacity)

    def Save(self,bullet):  #保存子弹
        if len(self.capList) < self.capacity:
            self.capList.append(bullet)

    def Bullets(self):  #出子弹
        if len(self.capList) > 0:
            bullet = self.capList[-1]
            self.capList.pop()
            return bullet
        else:
            return None


class Gun:
    def __init__(self):
        self.clip = None

    def __str__(self):
        if self.clip:
            return '枪当前有弹夹'
        else:
            return '枪没有弹夹'

    def Save(self,clip,bullet):
        self.clip = clip
    def Connection(self,clip):
        if not self.clip :
            self.clip = clip

    def Shot(self,enemy):
        bullet = self.clip.Bullet()
        if bullet:
            bullet.Hurt(enemy)
        else:
            print('没有子弹了，放了空枪……')

class Bullet(Gun):
    def __init__(self,killed):
        self.killed = killed

    def Hurt(self,enemy):  # 伤害 敌人
        enemy.BllodDrop(self.killed)  #敌人掉血
laowang = People('老王')

clip = Clip(20)
print(clip)


i = 0
while i < 5:
    bullet = Bullet(5)
    laowang.Loading(clip,bullet,clip)
    i+=1
print(clip)

gun = Gun()
print(gun)

laowang.Loading(gun,bullet,clip)
print(gun)

enemy = People('敌人')
print(enemy)

laowang.TakeAGun(gun,clip)

laowang.Shot(enemy)
print(enemy)
print(clip)

laowang.shot(enemy)
print(enemy)
print(clip)


