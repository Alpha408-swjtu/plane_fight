#敌方飞机
import pygame


class EnemyPlane(object):
    def __init__(self,screen):
        # 创建玩家飞机
        self.player = pygame.image.load("./images/enemy0.png")
        # 将图贴在窗口
        self.x = 0
        self.y = 0
        self.speed = 10
        self.screen = screen
        self.bullets = []


    def display(self):
        self.screen.blit(self.player, (self.x, self.y))
        # for bullet in self.bullets:
        #     bullet.auto_move()
        #     bullet.display()