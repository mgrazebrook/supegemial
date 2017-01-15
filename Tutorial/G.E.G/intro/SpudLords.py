import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
pink = 100, 0, 100
blue = 40, 10, 100
purple = 100, 20, 180
colourList = [purple, blue, pink]
currentColour = 1;
screen = pygame.display.set_mode(size)

ball = pygame.image.load("spud.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(event, ballrect)
            if (ballrect.left < event.pos[0] < ballrect.right and
                ballrect.top < event.pos[1] < ballrect.bottom):
                currentColour = (currentColour+1) % len(colourList)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(colourList[currentColour])

    screen.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.delay(10)