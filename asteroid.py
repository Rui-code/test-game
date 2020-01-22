import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load('data2/asteroid.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [70, 70])
        self.rect = self.image.get_rect()

        self.speed = 1 + random.random() * 2

    def update(self):
        self.rect[0] -= self.speed

        if self.rect[0] < -300:
            self.kill()
