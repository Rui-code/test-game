import os
import sys
import pygame
import random
from asteroid import Asteroid
from pink_ship import PinkShip
from projectile import Projectile

dir_path = os.getcwd()
sys.path.append(dir_path)

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

pygame.init()

SCREEN_RES = [840, 480]

display = pygame.display.set_mode(SCREEN_RES)
pygame.display.set_caption('Ninja 2D - Aula 02')

# Background
bg_group = pygame.sprite.Group()

bg_image = pygame.sprite.Sprite(bg_group)
bg_image.image = pygame.image.load('data2/desert.png')
bg_image.image = pygame.transform.scale(bg_image.image, SCREEN_RES)
bg_image.rect = bg_image.image.get_rect()

# Asteroids
asteroid_group = pygame.sprite.Group()

# Player
player_group = pygame.sprite.Group()
player = PinkShip(player_group)

# Shots
shots_group = pygame.sprite.Group()

# Musics
pygame.mixer.music.load('data2/intro_music.wav')
pygame.mixer.music.play(-1)

# Sounds
shot_sound = pygame.mixer.Sound('data2/shot_sound.ogg')

clock = pygame.time.Clock()
tick_timer = 0
game_over = False
game_loop = True

while game_loop:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shot_sound.play()
            new_shot = Projectile(shots_group)
            new_shot.rect.center = player.rect.center

    # Logic
    if not game_over:
        tick_timer += 1
        if tick_timer > 30:
            tick_timer = 0
            if random.random() < 0.4:
                new_asteroid = Asteroid(asteroid_group)
                x, y = SCREEN_RES[0], random.randint(0, SCREEN_RES[1] - 100)
                new_asteroid.rect.move_ip(x, y)

        bg_group.update()
        asteroid_group.update()
        player_group.update()
        shots_group.update()

        collisions = pygame.sprite.spritecollide(player, asteroid_group, False)

        if collisions:
            print("Game Over!")
            game_over = True

        hits = pygame.sprite.groupcollide(shots_group, asteroid_group, True, True)

    # Draw
    display.fill([25, 25, 25])

    bg_group.draw(display)

    shots_group.draw(display)
    player_group.draw(display)
    asteroid_group.draw(display)

    pygame.display.update()
