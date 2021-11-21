from pygame import *
# классы
class GameSprite(sprite.Sprite):
    def __init__(self,x_player,y_player,image_player,player_speed,player_size_1,player_size_2):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(player_size_1,player_size_2))# 65,65
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = x_player
        self.rect.y = y_player
    def recet(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y <500:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
class Player_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y <500:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
#окно
window = display.set_mode((700, 500))
display.set_caption("Шутер")
background=transform.scale(image.load("bacground.png"),(700,500))
#создание объектов
game = True
player_1 = Player(10,100,"rocetka.png",1,65,65)
player_2 = Player_2(620,100,"rocetka.png",1,65,65)

while game:
    for i in event.get():
        if i.type ==QUIT:
            game = False
    window.blit(background,(0,0))
    player_1.update()
    player_2.update()
    player_2.recet()
    player_1.recet()
    display.update()
    
    
