import random, math, pygame.math
from settings import *


class Obj:
    def __init__(self, pos):
        self.size = 10
        self.pos = pos
        self.speed = 0.1
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self, target_pos, dt):
        dists = target_pos - self.pos
        if dists[0] < 0:
            dists[0] *= -1
        if dists[1] < 0:
            dists[1] *= -1
        dist = math.sqrt(dists[0]**2 + dists[1]**2)

        if dist < 60:
            try:
                self.pos -= pygame.math.Vector2.normalize((target_pos - self.pos)) * self.speed * dt
            except:
                pass
        if self.pos.x > screensize[0]:
            self.pos.x = screensize[0]
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > screensize[1]:
            self.pos.y = screensize[1]
        if self.pos.y < 0:
            self.pos.y = 0
