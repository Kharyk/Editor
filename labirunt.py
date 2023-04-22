from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(45,45))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    
    def update(self):
        
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 720:
            self.rect.y += self.speed
            
        if keys_pressed[K_LEFT] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.y < 520:
            self.rect.x += self.speed
            
            
class Enemy(GameSprite):
    
    direction = "left"
    
    def update(self):
        
        if self.rect.x <= 490:
            self.direction =  "right"
        if self.rect.x >= 615:
            self.direction = "left"
            
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
            
class Enemy_2(GameSprite):
    
    direction = "left"
    
    def update(self):
        
        if self.rect.x <= 130:
            self.direction =  "right"
        if self.rect.x >= 420:
            self.direction = "left"
            
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
class Enemy_3(GameSprite):
    
    direction = "left"
    
    def update(self):
        
        if self.rect.x <= 330:
            self.direction =  "right"
        if self.rect.x >= 415:
            self.direction = "left"
            
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
            
class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.widht = wall_width
        self.height = wall_height
        self.image = Surface((self.widht, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        
win_width = 900
win_height = 800
back = (0,250,154)
display.set_caption("PIN-PONG")
window = display.set_mode((win_width, win_height))
window.fill(back)

#player = Player('hero.png',50,420,4)
#monster = Enemy("cyborg.png", 480, 280,2)
#monster_2 = Enemy_2("cyborg.png", 130, 50, 1)
#monster_3 = Enemy_3("cyborg.png", 320, 363, 1)
#finale = GameSprite("treasure.png", 530, 390, 0)


w1 = Wall(15,205,70,110,90,40,320)
w2 = Wall(15,205,70,110,460,40,330)
w3 = Wall(15,205,70,150,750,680,40)
w4 = Wall(15,205,70,800,460,40,330)
w5 = Wall(15,205,70,800,90,40,320)

w6 = Wall(15,205,70,150,90,680,40)
w7 = Wall(15,205,70,190,170,40,80)
w8 = Wall(15,205,70,230,170,80,40)
w9 = Wall(15,205,70,270,210,80,40)
w10 = Wall(15,205,70,350,130,40,400)

w11 = Wall(15,205,70,430,170,40,440)
w13 = Wall(15,205,70,600,250,80,40)
w14 = Wall(15,205,70,640,130,40,120)
w15 = Wall(15,205,70,720,170,40,240)
w90 = Wall(15,205,70,560,170,40,540)


w16 = Wall(15,205,70,190,290,120,40)
w17 = Wall(15,205,70,270,330,40,40)
w18 = Wall(15,205,70,640,330,40,240)
w19 = Wall(15,205,70,680,330,40,40)
w20 = Wall(15,205,70,190,370,40,120)

w21 = Wall(15,205,70,230,410,40,40)
w22 = Wall(15,205,70,270,410,40,200)
w23 = Wall(15,205,70,720,460,80,40)
w24 = Wall(15,205,70,720,490,40,80)
w25 = Wall(15,205,70,190,530,40,180)

w26 = Wall(15,205,70,230,670,40,80)
w27 = Wall(15,205,70,310,570,40,180)
w28 = Wall(15,205,70,390,570,40,140)
w29 = Wall(15,205,70,430,670,40,40)
w30 = Wall(15,205,70,600,630,80,40)

w31 = Wall(15,205,70,640,670,40,40)
w32 = Wall(15,205,70,720,630,40,80)







#mixer.init()
#mixer.music.load("jungles.ogg") 
#mixer.music.play()
#money = mixer.Sound("ḿoney.ogg")
#kick = mixer.Sound("kick.ogg")

game = True
clock = time.Clock()
FPS = 70

finish = False

#window.blit(background,(0,0))
#player.reset()
#monster.reset()
#monster_2.reset()
#monster_3.reset()

    
font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN!", True,(255,215,0))
lose = font.render("YOU LOSE!", True,(180,0,0))
    
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    

    if finish != True:
        #window.blit(background, (0,0))
        #player.update()
        #monster.update()
        #monster_2.update()
        #monster_3.update()
        
        
        #player.reset()
        #monster.reset()
        #monster_2.reset()
        #monster_3.reset()
        
        #finale.reset()
        
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        
        w11.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w90.draw_wall()
        
        
        w16.draw_wall()
        w17.draw_wall()
        w18.draw_wall()
        w19.draw_wall()
        w20.draw_wall()
        
        w21.draw_wall()
        w22.draw_wall()
        w23.draw_wall()
        w24.draw_wall()
        w25.draw_wall()
        
        w26.draw_wall()
        w27.draw_wall()
        w28.draw_wall()
        w29.draw_wall()
        w30.draw_wall()
        
        w31.draw_wall()
        w32.draw_wall()
        
        
        
        
        
        
        #if sprite.collide_rect(player,monster) or sprite.collide_rect(player,monster_2) or sprite.collide_rect(player,monster_3) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7) or sprite.collide_rect(player,w8) or sprite.collide_rect(player,w9) or sprite.collide_rect(player,w10) or sprite.collide_rect(player,w11) or sprite.collide_rect(player,w12) or sprite.collide_rect(player,w13) or sprite.collide_rect(player,w14) or sprite.collide_rect(player,w15) or sprite.collide_rect(player,w90) or sprite.collide_rect(player,w17) or sprite.collide_rect(player,w18) or sprite.collide_rect(player,w19) or sprite.collide_rect(player,w21) or sprite.collide_rect(player,w22)or sprite.collide_rect(player,w23)or sprite.collide_rect(player,w24)or sprite.collide_rect(player,w25)or sprite.collide_rect(player,w26)or sprite.collide_rect(player,w27)or sprite.collide_rect(player,w28)or sprite.collide_rect(player,w29)or sprite.collide_rect(player,w20)or sprite.collide_rect(player,w30)or sprite.collide_rect(player,w31) or sprite.collide_rect(player,w32):
            #finish = True
            #window.blit(lose,(200,200))
            #kick.play()
        #if sprite.collide_rect(player,finale):
            #finish = True
            #window.blit(win,(200,200))
            #money.play()        

    display.update()
    clock.tick(FPS)