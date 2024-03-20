import pygame, sys, object, random
from settings import *

screen = pygame.display.set_mode(screensize)

objs = []
for i in range(150):
    objs.append(object.Obj(pygame.math.Vector2(random.randint(0, screensize[0]), random.randint(0, screensize[1]))))

clock = pygame.time.Clock()
while True:
    dt = clock.tick(60)
    screen.fill("black")

    for obj in objs:
        pygame.draw.rect(screen, obj.color, (obj.pos.x - obj.size/2, obj.pos.y - obj.size/2, obj.size, obj.size))
        for other_obj in objs:
            if obj != other_obj:
                obj.update(other_obj.pos, dt)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
