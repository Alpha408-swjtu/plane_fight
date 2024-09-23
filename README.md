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
|

```

### planes

存储玩家和敌方飞机类

#### player.py

```python
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
...
```

#### enemy.py

```python
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
...
```

### bullets

子弹类

#### bullet.py

```python
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
...
```

