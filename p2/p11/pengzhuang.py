import pygame,random

class Base(object):
    def __init__(self,img_path,screen,x,y):
        self.screen = screen  # 创建的窗口 对象
        self.x = x
        self.y = y
        self.img_path = img_path

class Plane(Base):
    def __init__(self, img_path, screen,x,y):
        super().__init__(img_path,screen,x,y)
        self.w = 100
        self.h = 124
        self.plane = pygame.image.load(self.img_path)#飞机图片
        # 定义好的位置，和尺寸
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        # 列表保存发出的子弹
        self.bullet_list = []
        self.bao_tu = []

        self.hit = False
        self.create_image()
        self.image_num = 0
        self.image_index = 0
    def create_image(self):
        self.bao_tu.append(pygame.image.load('./images/hero_blowup_n1.png'))
        self.bao_tu.append(pygame.image.load('./images/hero_blowup_n2.png'))
        self.bao_tu.append(pygame.image.load('./images/hero_blowup_n3.png'))
        self.bao_tu.append(pygame.image.load('./images/hero_blowup_n4.png'))
    def bao(self):
        self.hit = True
    def peng(self):
        if self.hit == True:
            self.screen.blit(self.bao_tu[self.image_num],self.rect)
            self.image_index += 1
            if self.image_index == 10:
                self.image_num += 1
                self.image_index = 0
            if self.image_num > 3:
                self.rect.x = 750
                self.rect.y = 750
                exit()
    def display(self):
        self.screen.blit(self.plane, self.rect)#设置飞机
        # 显示子弹
        for i in self.bullet_list:
            if i.judge():
                self.bullet_list.remove(i)
            i.display()#子弹的对象.display()
            i.move()

class BaseBullet(Base):
    def __init__(self, img_path, screen,x,y):
        super().__init__(img_path,screen,x,y)
        self.bullet = pygame.image.load(self.img_path)#子弹图片

    def display(self):
        self.screen.blit(self.bullet, (self.x, self.y))#设置子弹


class EnemyPlane(Plane):
    '''这是敌人飞机的抽象类'''
    def __init__(self, img_path, screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def move(self):
        if self.flag == 'right':
            self.rect.x += 2
        else:
            self.rect.x -= 2

        if self.rect.x >= 330 :
            self.flag = 'left'
            self.rect.y += 60
        elif self.rect.x <= 0 :
            self.flag = 'right'
            self.rect.y += 60

    def fire(self):
        self.bullet_list.append(EnemyBullet('./images/bullet1.png', self.screen,self.rect.x,self.rect.y))

class HeroPlane(Plane):
    '''这是飞机的抽象类'''
    def __init__(self, img_path, screen):
        Plane.__init__(self,img_path,screen,(400-100)/2,350)

    def fire(self):
        self.bullet_list.append(Bullet('./images/bullet.png', self.screen,self.rect.x,self.rect.y))

class Bullet(BaseBullet):
    '''这是 子弹 的抽象类'''
    def display(self):
        self.screen.blit(self.bullet, (self.x, self.y))#设置子弹

    def move(self):
        self.y -= 2

    def judge(self):
        #判断子弹是否飞出了屏幕外
        if self.y < 0 :
            return True  #表示子弹飞出了屏幕
        else:
            return False
class EnemyBullet(BaseBullet):
    '''这是 敌人子弹 的抽象类'''
    def __init__(self, img_path, screen,x,y):
        BaseBullet.__init__(self,img_path,screen,x+40,y+20)

    def display(self):
        self.screen.blit(self.bullet, (self.x, self.y))#设置子弹

    def move(self):
        self.y += 2

    def judge(self):
        #判断子弹是否飞出了屏幕外
        if self.y > 500 :
            return True  #表示子弹飞出了屏幕
        else:
            return False

def jihui(hero,enemy_hero):
    for i in enemy_hero.bullet_list:
        if (i.x >= hero.rect.x and i.x <= hero.rect.x + 100) and (i.y >= hero.rect.y and i.y <= hero.rect.y+124):
            hero.bao()

def key_control(hero, move_step):
    # 游戏事件的监听 控制
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#退出游戏
            print('游戏退出')
            pygame.quit()
            exit() #退出程序
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.fire()
        #elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         rect.y -= move_step
        #     elif event.key == pygame.K_DOWN:
        #         rect.y += move_step
        #     elif event.key == pygame.K_LEFT:
        #         rect.x -= move_step
        #     elif event.key == pygame.K_RIGHT:
        #         rect.x += move_step
        # elif event.type == pygame.KEYUP:
        #     pass

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x < 400 - hero.rect.width:
            hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x > 0:  # - hero.rect.width:
            hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y > 0:  # - hero.rect.width:
            hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y < 500 - hero.rect.height:
            hero.rect.y += move_step
    if keys_pressed[pygame.K_SPACE]:
        hero.fire()
    if keys_pressed[pygame.K_b]:
        hero.create_image()
        hero.bao()
        hero.peng()
        # 定义好的位置，和尺寸
        #hero = HeroPlane('./image/hero_blowup_n3.png',hero.screen)

def main():
    # 创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)

    # 把本地文件夹的图片，获取到 代码中
    background = pygame.image.load('./images/background.png')

    # 初始化飞机
    hero = HeroPlane('./images/hero1.png', screen)
    enemy_hero = EnemyPlane('./images/enemy1.png',screen)

    clock = pygame.time.Clock() #获得游戏时钟 控制器

    move_step = 10 # 移动的步长值

    while True:
        # 把图片 加载 到 游戏窗口上
        screen.blit(background, (0,0))
        hero.display()
        hero.peng()
        enemy_hero.move()
        enemy_hero.display()
        jihui(hero,enemy_hero)
        if random.randint(1,52) == 5:
            enemy_hero.fire()

        key_control(hero, move_step)
        #if hero.rect.x <= 0:
        #    hero.rect.x =400
        #elif hero.rect.y <= 0:
        #    hero.rect.y = 350
        #elif hero.rect.x >= 400:
        #    hero.rect.x = 0
        #elif hero.rect.y >= 350:
        #    hero.rect.y = 0
        # 刷新显示
        pygame.display.update()
        clock.tick(60) # 让游戏时钟，1/60秒运行一次


if __name__ == '__main__':
    main()
