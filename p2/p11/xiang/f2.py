from jian import *
def main():
    # 创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)

    # 把本地文件夹的图片，获取到 代码中
    background = pygame.image.load('./images/background.png')

    # 初始化飞机
    hero = HeroPlane('./images/hero1.png', screen)
    #初始化敌机
    enemy_hero = EnemyPlane('./images/enemy1.png',screen)

    clock = pygame.time.Clock() #获得游戏时钟 控制器

    move_step = 10 # 移动的步长值

    while True:
        # 把图片 加载 到 游戏窗口上
        screen.blit(background, (0,0))
        hero.display()  #调用英雄显示
        hero.peng()  #调用英雄爆炸
        enemy_hero.display()  #调用敌机显示
        enemy_hero.move()  #调用敌机移动
        enemy_hero.peng()  #调用敌机爆炸
        jihui(hero,enemy_hero)  #调用碰撞检测方法
        djihui(hero,enemy_hero)
        if random.randint(1,80) == 5:  #判断发射子弹的频率，1/80的几率
            enemy_hero.fire()

        key_control(hero, move_step)  #调用游戏监听
        pygame.display.update()  #刷新游戏界面
        clock.tick(60) # 让游戏时钟，1/60秒运行一次

if __name__ == '__main__':
    main()
