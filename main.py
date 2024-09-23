import pygame
from pygame import QUIT

from planes.enemy import EnemyPlane
from planes.player import HeroPlane


def main():
    # 1.创建窗口
    screen = pygame.display.set_mode((480,852),0,32)
    # 创建背景图
    background = pygame.image.load("./images/background.png")

    player = HeroPlane(screen)
    enemy_plane = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))

        #获取事件
        for event in pygame.event.get():
            #关闭操作
            if event.type == QUIT:
                pygame.quit()
                exit()

        player.key_control()
        player.display()
        enemy_plane.display()

        #显示窗口
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(60) #降低移动速率

if __name__ == '__main__':
    main()