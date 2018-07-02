from jian import *
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
        enemy_hero.peng()
        enemy_hero.move()
        enemy_hero.display()
        jihui(hero,enemy_hero)
        djihui(hero,enemy_hero)
        if random.randint(1,52) == 5:
            enemy_hero.fire()

        key_control(hero, move_step)
        pygame.display.update()
        clock.tick(60) # 让游戏时钟，1/60秒运行一次


if __name__ == '__main__':
    main()
