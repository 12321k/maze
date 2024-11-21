from pygame import*

init()
font.init()
size =(500,500)
window=display.set_mode(size)
display.set_caption("Лабіринт")
clock=time.Clock()

class GameSprite:
    def __init__(self,img,x,y,width,height):
        self.image = transform.scale(image.load(img), (width, height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.direction=None
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y-=5
        if keys[K_s] and self.rect.y < 470:
            self.rect.y+=5
        if keys[K_a] and self.rect.x > 0:
            self.rect.x-=5
        if keys[K_d] and self.rect.x < 470:
            self.rect.x+=5


class Wall:
    def __init__(self,x,y,width,height,color):
        self.rect=Rect(x,y,width,height)
        self.color=color
    def reset(self):
        draw.rect(window,self.color,self.rect)
class Enemy(GameSprite):
    def update(self):
        if self.rect.x>450:
            self.direction=False
        if self.rect.x<0:
            self.direction=True
        if self.direction:
            self.rect.x+=10
        else:
            self.rect.x-=5
enemy=Enemy("cyborg.png",250,100,50,50)
player=Player("hero.png",10, 10, 30, 30)
finish=GameSprite("treasure.png",450,450,50,50)
font1=font.Font(None,30)

position_wall=[(0,50),(450,50),(100,250),(350,50),(400,50),(350,50),(300,50),(250,100),(50,100),(0,150),(200,150),(150,200),(50,200),(100,200),(0,250),(450,300),(400,250),(350,300),(300,250),(250,300),(200,250),(150,300),(100,250),(50,250),()]
size_walls=[(300,5),(5,200),(400,5),(5,200),(5,150),(50,5),(5,150),(5,150),(200,5),(200,5),(5,50),(55,5),(50,5),(5,50),(50,5),(5,200),(5,200),(5,200),(5,200),(5,200),(5,200),(5,200),(5,200),(5,200)]
walls=list()
for i in range(len(size_walls)):
    x=position_wall[i][0]
    y=position_wall[i][1]
    width=size_walls[i][0]
    height=size_walls[i][1]
    wall=Wall(x,y,width,height,(255,0,0))
    walls.append(wall)
game=True
hp=3
while game:
    for i in event.get():
        if i.type==QUIT:
            game=False
    window.fill((255,255,255))
    player.reset()
    player.update()
    finish.reset()

    for wall in walls:
        wall.reset()
        if wall.rect.colliderect(player):
            player.rect.x=10
            player.rect.y=10
            hp-=1
    enemy.reset()
    enemy.update()
    if enemy.rect.colliderect(player):
        player.rect.x=10
        player.rect.y=10
        hp-=1
    text_hp=font1.render(str(hp),True,(0,0,0))
    window.blit(text_hp,(20,20))
    if hp <=0:
        window.fill((255,0,0))
    if finish.rect.colliderect(player):
        window.fill((0,255,0))
    display.update()
    clock.tick(60)