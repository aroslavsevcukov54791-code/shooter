#Создай собственный Шутер!
from pygame import *
from random import randint
window=display.set_mode((700,500))
galaxy=transform.scale(image.load('galaxy.jpg'),(700,500))
FPS=60
clock=time.Clock()
game=True
finish=False
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire=mixer.Sound('fire.ogg')
font.init()
font=font.SysFont('Arial',40)
play_win=font.render('ТЫ ВЫИГРАЛ!',True,'green')
play_lose=font.render('ТЫ ПРОИГРАЛ!',True,'red')
score_tablet=0
passed_tablet=0
win_width=700
win_height=500
lost=0
win=0
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_width=100,player_hight=100):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(player_width,player_hight))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def fire_bullet(self):
        bullet=Bullets('bullet.png',self.rect.x,self.rect.top,5,50,50)
        bullets.add(bullet)
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x-=5
        if keys[K_RIGHT] and self.rect.x<625:
            self.rect.x+=5
player=Player('rocket.png',300,400,5)
class Enemy(GameSprite):
    

    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y>win_height:
            self.rect.x=randint(80,win_width-80)
            self.rect.y=0
            lost+=1
class Bullets(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y<0:
            self.kill


object=[]
    

bullets=sprite.Group()

monsters=sprite.Group()
for i in range(1,6):
    monster=Enemy('ufo.png',randint(80,win_width-80),0,randint(1,5))
    monsters.add(monster)


while game:
    if finish==False:
            
        window.blit(galaxy,(0,0))
        player.reset()
        player.update()
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()
        score=font.render('Cчет: '+str(score_tablet+win),True,(255,255,255))
        passed=font.render('Пропущено: '+str(passed_tablet+lost),True,(255,255,255))
        window.blit(score,(0,50))
        window.blit(passed,(0,90))
        if win==40:
            finish=True
            window.blit(play_win,(200,200))
        if lost==13 or sprite.spritecollide(player,monsters,False):
            finish=True
            window.blit(play_lose,(200,200))
            
        collides=sprite.groupcollide(bullets,monsters,True,True)
        for c in collides:
            win+=1
            monster=Enemy('ufo.png',randint(80,win_width-80),0,randint(1,5))
            monsters.add(monster)
    for e in event.get():
        if e.type==QUIT:
            game=False
        if e.type==KEYDOWN:
            if e.key==K_SPACE:
                fire.play()
                player.fire_bullet()
    display.update()
    clock.tick(FPS)





