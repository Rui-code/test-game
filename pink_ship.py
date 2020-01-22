import pygame


class PinkShip(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load('data2/pink_ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [80, 65])
        self.rect = self.image.get_rect()

        self.rect[0] = 40
        self.rect[1] = 220

        self.speed = 0
        self.acceleration = 0.1

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed -= self.acceleration
        elif keys[pygame.K_s]:
            self.speed += self.acceleration
        else:
            self.speed *= 0.9

        self.rect[1] += self.speed

        if self.rect[1] < 0:
            self.rect[1] = 0
            self.speed = 0
        elif self.rect[1] > 415:
            self.rect[1] = 415
            self.speed = 0
