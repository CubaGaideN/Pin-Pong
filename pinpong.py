from pygame import *

# Классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<500-70:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<500-70:
            self.rect.y += self.speed 
   
# Основа
window = display.set_mode((700, 500))
display.set_caption("Пин-Понг")
clock = time.Clock()
speed_x = 3
speed_y = 3
FPS = 60

# Спрайты и фон
background = transform.scale(
    image.load("bacground.png"),
    (700,500)
)

finish = False
game = True
rocket1 = Player("rocetka.png", 0, 250, 5)
rocket2 = Player2('rocetka.png', 635, 250, 5)
ball = GameSprite('ball.png', 0, 0, 2)

# Игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(background,(0, 0))
        ball.reset()
        ball.update()
        rocket1.reset()
        rocket1.update()
        rocket2.reset()
        rocket2.update()
    if ball.rect.y > 500-70 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
        speed_x *= -1
    display.update()
    clock.tick(FPS)

# Изменил модели ракеток, запрограммировал их движение
# Добавил модельку мячика и подкрутил физику
# Добавил столкновение