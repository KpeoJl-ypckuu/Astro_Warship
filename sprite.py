import pygame
import random
import pygame.freetype
pic_meteor = pygame.image.load('Res/метеорит1.webp')
pic_meteor = pygame.transform.scale(pic_meteor,[100,100])
pic_laser = pygame.image.load('Res/лазер.webp')
pic_laser = pygame.transform.scale(pic_laser,[10,50])
pic_repair = pygame.image.load('Res/ремонт.webp')
pic_repair = pygame.transform.scale(pic_repair,[100,100])
pic_damage = pygame.image.load('Res/усиление_урона.webp')
pic_damage = pygame.transform.scale(pic_damage,[100,100])
pic_XP = pygame.image.load('Res/хп.webp')
pic_XP = pygame.transform.scale(pic_XP,[200,100])
pic_RP = pygame.image.load('Res/RP.webp')
pic_RP = pygame.transform.scale(pic_RP,[50,100])
dlina = pic_meteor.get_width()
shirina = pic_meteor.get_height()
class Galaxy_War_Ship: 
    def __init__(self):
        self.pic = pygame.image.load('Res/истребитель1.webp')
        self.pic = pygame.transform.scale(self.pic,[100,100])
        self.dlina = self.pic.get_width()
        self.shirina = self.pic.get_height()
        self.rect = pygame.rect.Rect([700,200],[self.dlina,self.shirina])
        self.speed = 5
        self.XP = 100
    def paint(self,window):
        window.blit(self.pic, self.rect)
    def controller(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] == True and self.rect.left > 0:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_d] == True and self.rect.right < 1510:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_w] == True and self.rect.bottom >= 0:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_s] == True and self.rect.top <= 1080:
            self.rect.y = self.rect.y + self.speed

        
class Meteor:
    def __init__(self):
        self.rect = pygame.rect.Rect([random.randint(0,1510),0],[dlina,shirina])
        self.speedY = 3
    def paint(self,window):
        window.blit(pic_meteor,self.rect)
    def controller(self):
        self.rect.y = self.rect.y + self.speedY
class Laser:
    def __init__(self,gun_lokation):
        self.rect = pygame.rect.Rect(gun_lokation,[dlina,shirina])
        self.speedY = -10
    def paint(self,window):
        window.blit(pic_laser,self.rect)
    def controller(self):
        self.rect.y = self.rect.y + self.speedY
class Button:
    def __init__(self,lokation,text):
        self.pic = pygame.image.load('Res/кнопка.png')
        self.pic = pygame.transform.scale(self.pic,[500,150])
        self.shirina = self.pic.get_height()
        self.dlina = self.pic.get_width()
        self.rect = pygame.rect.Rect(lokation,[self.dlina,self.shirina])
        self.spawn_text_pic = pygame.freetype.Font('Res/шрифт.ttf',20)
        self.pic_rect = self.spawn_text_pic.render(text)
        self.text_pic = self.pic_rect[0]
        self.text_rect = self.pic_rect[1]
        self.text_rect.center = self.rect.center
    def paint(self,window):
        window.blit(self.pic,self.rect)
        window.blit(self.text_pic,self.text_rect)
class Repair:
    def __init__(self):
        self.rect = pygame.rect.Rect([random.randint(0,1510),0],[dlina,shirina])
        self.speedY = 3
        self.repairXP = random.randint(2,4)
    def paint(self,window):
        window.blit(pic_repair,self.rect)
    def controller(self):
        self.rect.y = self.rect.y + self.speedY
class Damage:
    def __init__(self):
        self.rect = pygame.rect.Rect([random.randint(0,1510),0],[dlina,shirina])
        self.speedY = 3
    def paint(self,window):
        window.blit(pic_damage,self.rect)  
    def controller(self):
        self.rect.y = self.rect.y + self.speedY 
class XP:
    def __init__(self,text):
        self.rect = pygame.rect.Rect([1290,980],[dlina,shirina])
        self.pic_XP = pygame.image.load('Res/хп.webp')
        self.pic_XP = pygame.transform.scale(pic_XP,[200,100])
        self.shirina = self.pic_XP.get_height()
        self.dlina = self.pic_XP.get_width()
        self.spawn_text_pic = pygame.freetype.Font('Res/шрифт.ttf',20)
        self.pic_rect = self.spawn_text_pic.render(str(text),[255,255,255])
        self.text_pic = self.pic_rect[0]
        self.text_rect = self.pic_rect[1]
        self.text_rect.centerx = self.rect.centerx + 50
        self.text_rect.centery = self.rect.centery
    def paint(self,window):
        window.blit(pic_XP,self.rect)
        window.blit(self.text_pic,self.text_rect)
    
    
    
