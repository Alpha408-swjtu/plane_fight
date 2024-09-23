import pygame
from pygame.locals import *

from bullets.bullet import Bullet


class HeroPlane(object):
    def __init__(self,screen):
        # 创建玩家飞机
        self.player = pygame.image.load("./images/hero1.png")
        # 将图贴在窗口
        self.x = 480 / 2 - 100 / 2
        self.y = 600
        self.speed = 10
        self.screen = screen
        self.bullets = []

    def key_control(self):
        # 监听键盘事件：
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            print("上")
            self.y -= self.speed
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            print("下")
            self.y += self.speed
        elif key_pressed[K_a] or key_pressed[K_LEFT]:
            print("左")
            self.x -= self.speed
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            print("右")
            self.x += self.speed
        elif key_pressed[K_SPACE]:
            #按空格发射子弹
            bullet = Bullet(self.screen,self.x,self.y)
            self.bullets.append(bullet)

    def display(self):
        self.screen.blit(self.player, (self.x, self.y))
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()