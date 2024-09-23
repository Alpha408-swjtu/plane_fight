#子弹
import pygame


class Bullet(object):
    def __init__(self,screen,x,y):
        self.x = x+41
        self.y = y-20
        self.image = pygame.image.load("./images/bullet.png")
        self.screen = screen
        self.speed = 10

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def auto_move(self):
        self.y -= self.speed