import pygame,random

class HeroPlane(object):
    '''这是飞机的抽象类'''
    def __init__(self, img_path, screen):
        self.screen = screen  # 创建的窗口 对象
        self.x = (400-100)/2
        self.y = 350
        self.w = 100
        self.h = 124
        self.img_path = img_path
        self.hero_plane = pygame.image.load(self.img_path)#飞机图片
        # 定义好的位置，和尺寸
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        # 列表保存发出的子弹
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.hero_plane, self.rect)#设置飞机
        # 显示子弹
        for i in self.bullet_list:
            i.display()#子弹的对象.display()
            i.move()

    def fire(self):
        self.bullet_list.append(Bullet('./images/bullet.png', self.screen,self.rect.x,self.rect.y))

    def fire1(self):
        self.bullet_list.append(Bullet('./images/bullet1.png', self.screen,self.rect.x + 80 ,self.rect.y))
class Bullet(object):
    '''这是 子弹 的抽象类'''
    def __init__(self, img_path, screen,x,y):
        self.screen = screen
        self.x = x  #(400-100)/2
        self.y =  y #350
        self.img_path = img_path
        self.bullet = pygame.image.load(self.img_path)#子弹图片

    def display(self):
        self.screen.blit(self.bullet, (self.x, self.y))#设置子弹

    def move(self):
        self.y -= 2
class EnemyPlane(object):
    '''这是敌机的抽象类'''
    def __init__(self, imgpath, screen):
        self.screen = screen  # 创建的窗口 对象
        self.x = 0
        self.y = 0
        self.imgpath = imgpath
        self.enemy_plane = pygame.image.load(self.imgpath)#飞机图片
        # 定义好的位置，和尺寸
        self.yidong = pygame.Rect(self.x, self.y,51,39)
        # 列表保存发出的子弹
        self.enemy_bullet_list = []

    def dis_play(self):
        self.screen.blit(self.enemy_plane, self.yidong)#设置飞机
        # 显示子弹
        for i in self.enemy_bullet_list:
            i.dis_play()#子弹的对象.display()
            i.enemy_move()

    def fire(self):
        self.enemy_bullet_list.append(EnemyBullet('./images/bullet1.png', self.screen,self.yidong.x,self.yidong.y))

class EnemyBullet(object):
    '''这是 子弹 的抽象类'''
    def __init__(self, imgpath, screen,x,y):
        self.screen = screen
        self.x = x
        self.y =  y
        self.imgpath = imgpath
        self.enemy_bullet = pygame.image.load(self.imgpath)#子弹图片

    def dis_play(self):
        self.screen.blit(self.enemy_bullet, (self.x, self.y))#设置子弹
    def enemy_move(self):
        self.y += 2


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
    if keys_pressed[pygame.K_SPACE]:
        hero.fire()
        hero.fire1()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        hero.rect.y += move_step

def main():
    # 创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)

    # 把本地文件夹的图片，获取到 代码中
    background = pygame.image.load('./images/background.png')

    # 初始化飞机
    hero = HeroPlane('./images/hero1.png', screen)
    enemy = EnemyPlane('./images/enemy0.png',screen)
    clock = pygame.time.Clock() #获得游戏时钟 控制器

    move_step = 10 # 移动的步长值

    while True:
        # 把图片 加载 到 游戏窗口上
        screen.blit(background, (0,0))
        hero.display()
        enemy.dis_play()
        #for i in enemy.enemy_bullet_list:
        #    if i % 5  == 0 :

        for i in str(random.randint(1,10)):
            if enemy.yidong.x % 10 == 0 :
                enemy.fire()

        enemy.yidong.x += 1
        if enemy.yidong.x > 400 :
            enemy.yidong.x = 0
            enemy.yidong.y += 40


        key_control(hero, move_step)
        if hero.rect.x < 0:
            hero.rect.x =0
        elif hero.rect.y < 0:
            hero.rect.y = 0
        elif hero.rect.x > 300:
            hero.rect.x = 300
        elif hero.rect.y > 370:
            hero.rect.y = 370
        # 刷新显示
        pygame.display.update()
        clock.tick(60) # 让游戏时钟，1/60秒运行一次


if __name__ == '__main__':
    main()
