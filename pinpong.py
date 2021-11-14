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

# Основа
window = display.set_mode((700, 500))
display.set_caption("Пин-Понг")
clock = time.Clock()
FPS = 60

# Спрайты и фон
background = transform.scale(
    image.load("background.jpg"),
    (700,500)
)

finish = False
game = True

# Игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))


    display.update()
    clock.tick(FPS)