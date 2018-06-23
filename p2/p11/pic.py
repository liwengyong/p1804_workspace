
import pygame

class tu(object):
    def __init__(self,img_path,screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.width = 500
        self.height = 300
        self.img_path = img_path
        print(img_path)
        self.tu_pian = pygame.image.load(self.img_path)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

    def display(self):
        self.screen.blit(self.tu_pian,self.rect)

def main():
    screen = pygame.display.set_mode((500,300),0,32)
    #background = pygame.image.load('./images/bg.png')
    #screen.blit(background,(0,0))

    clock = pygame.time.Clock()



    a = 1
    c = 1
    while c < 25:
        b = './tu/tu%d.jpg' % a
        a +=1
        aa = tu(b,screen)
        if a > 3:
            a =1
        c +=1
        aa.display()
        clock.tick(25)
        pygame.display.update()
main()
