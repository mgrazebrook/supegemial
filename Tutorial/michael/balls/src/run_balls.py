# Other peoples' modules
import sys
import os
import pygame
import random

# A folder intended to contain the data for levels but not code
import scenario.icons



class Thing(pygame.sprite.Sprite):
    def __init__(self, group, icon_file, pos, speed):
        pygame.sprite.Sprite.__init__(self, group)
        self.icon_file = icon_file
        self.speed = speed
        self.image = pygame.image.load(icon_file)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos)
        self.friction = 0.01


    def update(self, display):
        self.rect = self.rect.move(self.speed)
        speed = self.speed
        rect = self.rect
        if rect.left < 0 or rect.right > display.width:
            speed[0] = -speed[0]
        if rect.top < 0 or rect.bottom > display.height:
            speed[1] = -speed[1]

        self.speed = speed


class Balls:
    size = width, height = 1000,500
    colour = 120, 30, 90

    def __init__(self, ):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.things = pygame.sprite.Group()
        for icon_file, pos, speed in scenario.icons.icons:
            icon_path = os.path.join('img', icon_file)
            Thing(self.things, icon_path, pos, speed)


    def run(self):
        """
        The event loop

        Detects mouse movements and key presses. Decides what to do.
        """
        while 1:
            for event in pygame.event.get():
                print(event) # debugging ...
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for thing in self.things:
                        if (thing.rect.left <= event.pos[0] and 
                            thing.rect.right >= event.pos[0] and
                            thing.rect.top <= event.pos[1] and
                            thing.rect.right >= event.pos[1]):
                            Balls.colour = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)

            for thing in self.things:
                thing.update(Balls)


            self.screen.fill(self.colour)
            self.things.draw(self.screen)

            pygame.display.flip()
            pygame.time.delay(10)


balls = Balls()
balls.run()


	

