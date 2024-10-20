import time

from pygame import font, display, key, transform, image
from pygame import sprite
from pygame import event
from pygame.constants import QUIT, K_UP, K_DOWN, K_w, K_s


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):

    def move_right(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed

    def move_left(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed


win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
# фон сцены
back = 'azure3'
window.fill(back)
racket1 = Player('racket.png', 30, 200, 4, 70, 150)
racket2 = Player('racket.png', 30, 200, 4, 70, 150)
ball = Player('tenis_ball.png', 200, 200, 4, 50, 50)
game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 35)

lose1 = font.render('ИГРОК 1 ПРОИГРАЛ!', True, 'red')
lose2 = font.render('ИГРОК 2 ПРОИГРАЛ!', True, 'red')

speed_x = 3
speed_y = 3

while game:
    # событие "закрыть игру"
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:

        window.fill(back)

        racket1.move_left()
        racket2.move_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_height:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
