import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
pink = 100, 0, 100
blue = 20, 20, 100
purple = 100, 20, 180
colourList = [pink, blue, purple]
currentColour = 1;
screen = pygame.display.set_mode(size)

ball = pygame.image.load("spud.png")
ballrect = ball.get_rect()
mouseDown = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(colourList[currentColour])

    screen.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.delay(10)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        print(event)
        if mouseDown == 0:
            currentColour = (currentColour+1) % len(colourList)
        mouseDown = 1
    else:
        mouseDown = 0
