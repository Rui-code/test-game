import pygame
import random


class Projectile(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load('data2/projectile.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [20, 20])
        self.rect = self.image.get_rect()

        self.speed = 4

    def update(self):
        self.rect[0] += self.speed

        if self.rect[0] > 840:
            self.kill()
