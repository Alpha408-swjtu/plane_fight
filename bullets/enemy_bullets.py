import pygame


class EnemyBullet(object):
    def __init__(self,screen,x,y):
        self.x = x+21
        self.y = y=39
        self.image = pygame.image.load("./images/bullet1.png")
        self.screen = screen
        self.speed = 10

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def auto_move(self):
        self.y += self.speed