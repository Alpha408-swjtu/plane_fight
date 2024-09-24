#  飞机大战

基于pygame的飞机大战游戏

## 文件结构

```shell
|...
|
|--main.py
|
|--images
|
|--planes
|       |--enemy.py
|       |--player.py
|
|--bullets
|       |--bullet.py
|       |--enemy_bullets.py
|
|--sound
|       |--music.py
```

### main.py

```python
def main():
    sound = GameSound()
    sound.PlayMusic()
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
        enemy_plane.auto_move()
        enemy_plane.auto_fire()

        #显示窗口
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(60) #降低移动速率
```



### images

游戏所需要的图片和音乐

### planes

存储玩家和敌方飞机类

####     player.py

​         本方飞机

####     enemy.py

​          敌机

### bullets

子弹类

####     bullet.py

​           玩家子弹   

####     enemy_bullet.py

​           敌机子弹

