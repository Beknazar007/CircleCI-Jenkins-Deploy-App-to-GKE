import pygame

pygame.init()


win = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong')



white = (255, 255, 255)
black = (0, 0, 0)
col1 =(0,20,255)
col2 = (200,255,0)



class Paddle1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(col2)
        self.rect = self.image.get_rect()
        self.points = 0

class Paddle2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(col1)
        self.rect = self.image.get_rect()
        self.points = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 15
        self.dx = 1
        self.dy = 1
class Paddle3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 100])
        self.image.fill(col1)
        self.rect = self.image.get_rect()
        self.speed = 10

        self.dy = 1
class Paddle4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 100])
        self.image.fill(col2)
        self.rect = self.image.get_rect()

        self.dy = 1


paddle1 = Paddle1()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle2()
paddle2.rect.x = 720
paddle2.rect.y = 225

paddle3 = Paddle3()
paddle3.rect.x = 300
paddle3.rect.y = 30

paddle4 = Paddle4()
paddle4.rect.x = 450
paddle4.rect.y = 30



paddle_speed = 25

paddle_speed2 = 20

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250



all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong,paddle3, paddle4)



def redraw():

    win.fill(black)


    font = pygame.font.SysFont('Comic Sans MS', 20)
    text = font.render('PONG', False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    win.blit(text, textRect)

    
    p1_score = font.render(str(paddle1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)

    
    p2_score = font.render(str(paddle2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)

    
    all_sprites.draw(win)

    
    pygame.display.update()

run = True


while run:

    pygame.time.delay(100)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y += -paddle_speed
    if key[pygame.K_s]:
        paddle1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y += -paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle_speed


    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy


    if pong.rect.y > 490:
        pong.dy = -1

    if pong.rect.y < 1:
        pong.dy = 1

    if pong.rect.x > 750:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        paddle1.points += 1

    if pong.rect.x < 1:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = 1
        paddle2.points += 1

    paddle3.rect.y+=paddle_speed2 * paddle3.dy

    if paddle3.rect.y > 400:
        paddle3.dy = -1

    if paddle3.rect.y < 10:
        paddle3.dy = 1

    paddle4.rect.y += paddle_speed2 * paddle4.dy

    if paddle4.rect.y > 400:
        paddle4.dy = -1

    if paddle4.rect.y < 10:
        paddle4.dy = 1

    if paddle1.rect.colliderect(pong.rect):
        pong.dx = 1

    if paddle2.rect.colliderect(pong.rect):
        pong.dx = -1

    if paddle3.rect.colliderect(pong.rect):

        pong.dx =-1

    if paddle4.rect.colliderect(pong.rect):

        pong.dx = 1



    redraw()

pygame.quit()
