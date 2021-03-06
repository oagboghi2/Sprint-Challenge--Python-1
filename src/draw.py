import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(1*random.random() - 6, 1*random.random() - 6),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    #position, width, height, color
    block1 = KineticBlock(Vector2(40,50), 75, 50, [0, 0, 255])
    object_list.append(block1)
    block2 = KineticBlock(Vector2(120,50), 75, 50, [255, 0, 0])
    object_list.append(block2)
    block3 = KineticBlock(Vector2(200,50), 75, 50, [80, 25, 175])
    object_list.append(block3)
    block4 = KineticBlock(Vector2(280,50), 75, 50, [43, 255, 1])
    object_list.append(block4)
    block5 = KineticBlock(Vector2(360,50), 75, 50, [100, 35, 0])
    object_list.append(block5)
    # block6 = KineticBlock(Vector2(490,50), 75, 50, [34, 90, 200])
    # object_list.append(block6)

    paddle = Paddle(Vector2(200,680), 75, 25, [0, 0, 0])
    object_list.append(paddle)

    print(object_list)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            object.update()
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
