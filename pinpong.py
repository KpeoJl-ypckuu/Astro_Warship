import pygame 
import random
import pygame.freetype
import sprite
pygame.init()
window = pygame.display.set_mode([1510,1080])
window.fill([1,2,50])
button3 = sprite.Button([570,610],'нажмите R что бы продолжить')
ball = pygame.rect.Rect([500,500],[100,100])
rectangle1 = pygame.rect.Rect([100,900],[175,25])
rectangle2 = pygame.rect.Rect([900,100],[175,25])
speedX = 3
speedY = 5
a = 1
red_player = 0
green_player = 0
pm = pygame.time.Clock()
red = 255
green = 0
blue = 40
on_off_menu = 0

while a == 1:
    if on_off_menu == 0:
        # движение объектов
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True and rectangle1.left > 0:
            rectangle1.x = rectangle1.x - 20
        elif keys[pygame.K_RIGHT] == True and rectangle1.right < 1510:
            rectangle1.x = rectangle1.x + 30
        if rectangle1.colliderect(ball):
            speedY = random.randint(-10,-1)
            red = 255
            green = 0
            blue = 40

        # ракетка противника
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] == True:
            rectangle2.x = rectangle2.x - 20
        elif keys[pygame.K_d] == True:
            rectangle2.x = rectangle2.x + 30
        if rectangle2.colliderect(ball):
            speedY = random.randint(1,10)
            red = 0
            green = 150
            blue = 40

        

        # координата Х
        ball.x = ball.x + speedX
        if ball.right >= 1510:
            speedX = random.randint(-10,-1)
        elif ball.left <= 0:
            speedX = random.randint(1,10)
            

        # координата У и очки игры
        
        ball.y = ball.y + speedY
        if ball.bottom >= 1080:
            green_player = green_player + 1
            if green_player == 5:
                print('Зелёный победил ! Игра окончена ! ')
                on_off_menu = 1
            ball = pygame.rect.Rect([700,500],[100,100])
            speedY = random.randint(-10,-1)
        elif ball.top <= 0:
            red_player = red_player + 1
            if red_player == 5:
                print('Красный победил ! Игра окончена ! ')
                on_off_menu = 1
            ball = pygame.rect.Rect([700,500],[100,100])
            speedY = random.randint(1,10)
   

    # отрисовка 
    
    FPS = pm.get_fps() 
    pygame.display.set_caption(str(FPS))  
    if on_off_menu == 0:
        window.fill([1,2,50])
        pygame.draw.rect(window,[255,0,40],rectangle1)
        pygame.draw.rect(window,[0,150,40],rectangle2)
        pygame.draw.ellipse(window,[red,green,blue],ball)
        spawn_text_pic = pygame.freetype.Font('Res/шрифт.ttf',50)
        pic_rect = spawn_text_pic.render(str(green_player),[255,255,255])
        text_pic = pic_rect[0]
        text_rect = pic_rect[1]
        text_rect.center = [590,100]
        window.blit(text_pic,text_rect)
        spawn_text_pic = pygame.freetype.Font('Res/шрифт.ttf',50)
        pic_rect = spawn_text_pic.render(str(red_player),[255,255,255])
        text_pic = pic_rect[0]
        text_rect = pic_rect[1]
        text_rect.center = [590,900]
        window.blit(text_pic,text_rect)
    elif on_off_menu == 1:
        window.fill([25,25,25])
        pic_rect = spawn_text_pic.render('нажмите R чтобы продолжить',[255,255,255])
        text_pic = pic_rect[0]
        text_rect = pic_rect[1]
        text_rect.center = [755,540]
        window.blit(text_pic,text_rect)
    pygame.display.update() 
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            a = a + 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and on_off_menu == 1:
                on_off_menu = 0
                red_player = 0
                green_player = 0
                rectangle1 = pygame.rect.Rect([100,900],[175,25])
                rectangle2 = pygame.rect.Rect([900,100],[175,25])
    pm.tick(100)
