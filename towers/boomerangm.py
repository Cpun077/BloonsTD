import math
import pygame
from towers.tower import Tower


class BoomerangMonkey(Tower):

    img = pygame.image.load("images/tower_images/boomerangm.png")
    img = pygame.transform.smoothscale(img, (60, 60))

    def __init__(self, x, y):
        self.range = 300
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.price = None
        self.damage = None
        self.img.convert_alpha()
        self.img.set_alpha(255)
        self.reload_tick = [0, 20]  # number of frames to wait before shooting again
        self.is_reloading = False
        self.width = self.img.get_width()
        self.height = self.img.get_height()
