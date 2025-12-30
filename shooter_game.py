from pygame import *

background = transform.scale(image.load("galaxy.jpg"), (600, 500))

window = display.set_mode((600, 500))
display.set_caption("Shoting")
game = True

back = (200, 244, 255)
window.fill(back)
font.init()
font = font.SysFont("Arial", 36)

speed_x = 3
speed_y = 3
clock = time.Clock()
speed = 10
win_width = 600
win_height = 500
lost = 0
score = 0
max_lost = 7
max_win = 5
life = 3
life_color = (0, 150, 0)
num_fire = 0
rel_time = False
lose1 = font.render('PLAYER1 Lose', True, (180, 0, 0))
lose2 = font.render('PLAYER2 Lose', True, (180, 0, 0))


img_racket = "racket.png"
img_ball = "tenis_ball.png"

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (width, height))
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

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1 
        speed_y *= 1

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        game_over = True

    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (200, 200))
        gome_over = True

    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()    
    clock.tick(60)
    


