from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption("Shoting")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
game = True

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")

font.init()
font2 = font.SysFont("Arial", 36)
font1 = font.SysFont("Arial", 80)

clock = time.Clock()
x1 = 100
y1 = 300
x2 = 300
y2 = 300
speed = 10
win_width = 700
win_height = 500
lost = 0
score = 0
max_lost = 7
max_win = 5
life = 3
life_color = (0, 150, 0)
num_fire = 0
rel_time = False



img_hero = "rocket.png"
img_enemy = "ufo.png"
img_bullet = "bullet.png"
img_ast = "asteroid.png"

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

bullets = sprite.Group()

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


asteoroids = sprite.Group()
for i in range(1, 3):
    asteroid = Enemy(img_ast, randint(30, win_width - 30), -40, 80, 50, randint(1,7))
    asteoroids.add(asteroid)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)


finish = False
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if num_fire < 5 and rel_time == False:
                    num_fire = num_fire + 1
                    fire_sound.play()
                    ship.fire()
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True

    if finish != True:
        window.blit(background, (0, 0))
        ship.update()
        monsters.update()
        bullets.update()
        asteroid.update()
        
        text = font2.render("Score: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lost = font2.render("Lost: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lost, (10, 50))
        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))
        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3: #before 3 seconds are over, display reload message
                reload = font2.render('Wait, reload...', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0   #set the bullets counter to zero               
                rel_time = False #reset the reload flag
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteoroids.draw(window)

        collide = sprite.groupcollide(monsters, bullets, True, True)
        for c in collide:
            score += 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        if score == max_win:
            finish = True
            window.blit(win, (275, 250))

        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteoroids, False):
            sprite.spritecollide(ship, monsters, True)
            sprite.spritecollide(ship, asteoroids, True)
            life = life - 1
        if life == 0 or lost >= max_lost:
            finish = True
            window.blit(lose, (275, 250))


    display.update()    
    clock.tick(60)
    


