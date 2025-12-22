from pygame import *

background = transform.scale(image.load("galaxy.jpg"), (600, 500))

window = display.set_mode((600, 500))
display.set_caption("Shoting")
game = True

back = (200, 244, 255)
window.fill(back)
font.init()
font2 = font.SysFont("Arial", 36)
font1 = font.SysFont("Arial", 80)

speed_x = 3
speed_y = 3
clock = time.Clock()
speed = 10
win_width = 60
win_height = 500
lost = 0
score = 0
max_lost = 7
max_win = 5
life = 3
life_color = (0, 150, 0)
num_fire = 0
rel_time = False



img_racket = "racket.png"
img_ball = "tenis_ball.png"

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

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:   
            self.rect.y += self.speed

racket1 = Player(img_racket, 30, 200, 4, 50, 150)
racket2 = Player(img_racket, 520, 200, 4, 50, 150)
ball = GameSprite(img_ball, 200, 200, 4, 50, 50)


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

finish = False

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))


    display.update()    
    clock.tick(60)
    


