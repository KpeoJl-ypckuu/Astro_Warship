import pygame 
import settings
import sprite
import random 
pygame.init()
pygame.mixer.init(channels=4)
window = pygame.display.set_mode([settings.DLINA,settings.VISOTA])
fon = pygame.image.load('Res/фон.jpg')
fon = pygame.transform.scale(fon,[settings.DLINA,settings.VISOTA])
fon_menu = pygame.image.load('Res/меню_фон.jpg')
fon_menu = pygame.transform.scale(fon_menu,[settings.DLINA,settings.VISOTA])
fon_settings = pygame.image.load('Res/фон_настройки.jpg')
fon_settings = pygame.transform.scale(fon_settings,[settings.DLINA,settings.VISOTA])
start = 1
pm = pygame.time.Clock()
warship = sprite.Galaxy_War_Ship()
bonusR = sprite.Repair()
damage = sprite.Damage()
some_repair = []
some_meteorit = []
some_laser = []
some_damage = []
time = 0
time_fire = 0
time_damage = 0
on_off_menu = 3
rate_of_fire = 500
button1 = sprite.Button([570,200],'Заново')
button2 = sprite.Button([570,410],'Создатели')
button3 = sprite.Button([570,610],'Выйти из игры')
button5 = sprite.Button([570,200],'Играть')
spawn_meteorit = pygame.USEREVENT
spawn_repeir = pygame.USEREVENT + 1
spawn_damage = pygame.USEREVENT + 2
pygame.time.set_timer(spawn_meteorit,500)
pygame.time.set_timer(spawn_repeir,random.randint(10000,30000))
pygame.time.set_timer(spawn_damage,random.randint(10000,30000))
fire = pygame.mixer.Sound('sounds/выстрел.mp3')
fon_music = pygame.mixer.Sound('sounds/саундтрек.mp3')
fon_music.set_volume(0.05)
fon_music.play(-1)
boom = pygame.mixer.Sound('sounds/взрыв.mp3')
boom.set_volume(0.1)
while start == 1:

     
    if on_off_menu == 0:
        # геймплей
        warship.controller()
        for save in some_meteorit:
            save.controller()
        for save in some_laser:
            save.controller()
        for save in some_repair:
            save.controller()
        for save in some_damage:
            save.controller()
        mouse = pygame.mouse.get_pressed()
        if mouse[0] == True and time - time_fire > rate_of_fire:
            laser = sprite.Laser([warship.rect.centerx, warship.rect.y])
            some_laser.append(laser)
            fire.play()
            time_fire = pygame.time.get_ticks()
        for save in some_damage:
            if save.rect.colliderect(warship.rect):
                rate_of_fire = 100
                some_damage.remove(save)
                time_damage = pygame.time.get_ticks()
        if time - time_damage > 10000:
            rate_of_fire = 500
        for save in some_meteorit:
            if save.rect.colliderect(warship.rect):
                warship.XP = warship.XP - 20
                boom.play()
                some_meteorit.remove(save)
        for save in some_repair:
            if save.rect.colliderect(warship.rect):
                warship.XP = warship.XP + 10 * save.repairXP
                some_repair.remove(save)
        if warship.XP <= 0:
            on_off_menu = 1
        for saveL in some_laser:
            for saveM in some_meteorit:
                if saveL.rect.colliderect(saveM.rect):
                    some_meteorit.remove(saveM)
                    some_laser.remove(saveL)
                    boom.play()
                    
       
        time = pygame.time.get_ticks()
    
    

    # отрисовка 
    
    FPS = pm.get_fps() 
    pygame.display.set_caption(str(FPS))  
    if on_off_menu == 0:
        window.blit(fon,[0,0])
        warship.paint(window)
        for save in some_meteorit:
            save.paint(window)
        for save in some_laser:
            save.paint(window)
        for save in some_repair:
            save.paint(window)
        for save in some_damage:
            save.paint(window)
        xp = sprite.XP(str(warship.XP) + 'XP')
        xp.paint(window)
    elif on_off_menu == 1:
        window.blit(fon_menu,[0,0])
        button1.paint(window) 
        button2.paint(window) 
        button3.paint(window) 
    elif on_off_menu == 3:
        window.blit(fon_menu,[0,0])
        button5.paint(window) 
        button2.paint(window) 
        button3.paint(window) 
    elif on_off_menu == 4:
        window.blit(fon_settings,[0,0])
        
    pygame.display.update()
    

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            start = start + 1
        elif event.type == spawn_meteorit:
            meteorit = sprite.Meteor()
            some_meteorit.append(meteorit)
        elif event.type == spawn_repeir:
            bonusR = sprite.Repair()
            some_repair.append(bonusR)
            pygame.time.set_timer(spawn_repeir,random.randint(10000,30000))
        elif event.type == spawn_damage:
            damage = sprite.Damage()
            some_damage.append(damage)
            pygame.time.set_timer(spawn_damage,random.randint(10000,30000))
        elif event.type == pygame.MOUSEBUTTONDOWN and on_off_menu == 1:
            if button3.rect.collidepoint(event.pos):
                start = start + 1
            if button1.rect.collidepoint(event.pos):
                on_off_menu = 0
                warship.XP = 100
                warship.rect.center = [700,200]
                some_meteorit = []
                some_damage = []
                some_repair = []
                some_laser = []
            if button2.rect.collidepoint(event.pos):
                on_off_menu = 4
            if button3.rect.collidepoint(event.pos):
                start = start + 1
        elif event.type == pygame.MOUSEBUTTONDOWN and on_off_menu == 3:
            if button5.rect.collidepoint(event.pos):
                on_off_menu = 0
                warship.XP = 100
                warship.rect.center = [700,410]
                some_meteorit = []
                some_damage = []
                some_repair = []
                some_laser = []
            if button2.rect.collidepoint(event.pos):
                on_off_menu = 4
            if button3.rect.collidepoint(event.pos):
                start = start + 1
        



        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] == True and on_off_menu == 4:
            on_off_menu = 3

            
        
            
    pm.tick(100)
