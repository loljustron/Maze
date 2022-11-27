from time import *
from pygame import *

#fonts
white = (255, 255, 255)
yellow = (255, 255, 0)
font.init()
font = font.SysFont('Comic Sans MS', 50)
win = font.render('YOU WON!1!', True, yellow)
loose = font.render('YOU LOOOSER!1!))!', True, white)

'''classes'''
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, width, height, speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed, right):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.right = right
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.right = False
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 45:
            self.right = True
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 45:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('billliti.png', self.rect.right, self.rect.centery, 15, 20, 15, self.right)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.side = 'right'
        if self.rect.x >= win_width - 85:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Enemy2(GameSprite):
    side = 'up'
    def __init__(self, player_image, player_x, player_y, width, height, speed, health):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.hp = health
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update(self):
        if self.rect.y <= 5:
            self.side = 'up'
        if self.rect.y >= win_height - 300:
            self.side = 'down'
        if self.side == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.hp <= 0:
            self.kill()
class Enemy3(GameSprite):
    side = 'up'
    def update(self):
        if self.rect.y <= 115:
            self.side = 'up'
        if self.rect.y >= win_height - 110:
            self.side = 'down'
        if self.side == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
class Enemy4(GameSprite):
    side = 'left'
    def update(self):
        if self.rect.x <= 100:
            self.side = 'right'
        if self.rect.x >= win_width - 250:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, colour, wall_x, wall_y, width, height): #class constructor
        super().__init__() #inheriting properties from superclass
        #an image property for Picture
        self.colour = colour
        self.w = width
        self.h = height
        self.image = Surface((self.w, self.h))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed, right):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.right = right
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update(self):
        if self.right == True:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.rect.x > win_width + 10:
            self.kill()
        if self.rect.x < -10:
            self.kill()

#creating a window
win_width = 700
win_height = 500
window_size = (win_width, win_height)
display.set_caption('Random game') #window's name
window = display.set_mode(window_size) #setting a window
back = transform.scale(image.load('backdora.png'), window_size) #setting a background

#creating sprites (objects) using previously created classes
hero = Player('FINNTHEHUMAN.png', 30, 5, 44, 56, 10, True)
boss = Enemy2('swiperfox.png', win_width // 6 + 30, 60, 175, 130, 2, 5)
monster1 = Enemy3('swiperfox.png', win_width // 6 * 5 - 60, 280, 150, 120, 2)
final = GameSprite('coinmeh.png', win_width - 120, 10, 65, 65, 0)

#creating walls
w_colour = (125, 52, 12)
w1 = Wall(w_colour, win_width // 6, 0, 10, win_height - 100)
w2 = Wall(w_colour, win_width // 6 + 10, win_height - 175, win_width // 6 * 3, 10)
w3 = Wall(w_colour, win_width // 6 * 2, win_height - 65, 10, 65)
w4 = Wall(w_colour, win_width // 6 * 3, win_height - 165, 10, 85)
w5 = Wall(w_colour, win_width // 6 * 4, win_height - 65, 10, 65)
w6 = Wall(w_colour, win_width // 6 * 4, win_height - 240, 10, 65)
w7 = Wall(w_colour, win_width // 6 * 3, 100, win_width - win_width // 6 * 2 + win_width //12, 10)
w8 = Wall(w_colour, win_width // 6 * 3, 110, 10, 65)
w9 = Wall(w_colour, 200, 280, 10, 200)

#grouping
bullets = sprite.Group()
monsters = sprite.Group()
monsters.add(monster1)
walls = sprite.Group()
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)
walls.add(w7)
walls.add(w8)

#game itself
points = 0
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()

    if finish != True:
        window.blit(back, (0,0))
        walls.draw(window)
        monsters.update()
        monsters.draw(window)
        hero.reset()
        hero.update()
        final.reset()
        bullets.draw(window)
        bullets.update()
        if boss.hp > 0:
            boss.reset()
            boss.update()
            x = font.render(str(boss.hp), True, (255, 255, 255))
            window.blit(x, (win_width // 6 + 10, boss.rect.y + 30))
        sprite.groupcollide(bullets, walls, True, False)

        sprite.groupcollide(bullets, monsters, True, True)
        if sprite.spritecollide(boss, bullets, True):
            boss.hp -= 1
        if sprite.spritecollide(hero, monsters, False):
            finish = True
            window.blit(loose, (200, 200))
        if sprite.spritecollide(hero, walls, False):
            finish = True
            window.blit(loose, (200, 200))
        if sprite.collide_rect(hero, final):
            finish = True
            window.blit(win, (200, 200))


    display.update()
    clock.tick(FPS)