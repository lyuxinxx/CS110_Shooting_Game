import sys
import pygame
import MenuItem
from GameMenu import *
import player
import bullets
import enemy
import rocks
import time

pygame.init()

bgm = pygame.mixer.music.load("monkeys.wav")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400

def setSpeed():
    t = time.clock()
    return (8 + t/5, 4 + t/5)

def RunGame():
    #pygame.init()

    pygame.mixer.music.play(1)

    # Create the window

    screen = pygame.display.set_mode((screen_width,screen_height))

    font = pygame.font.SysFont("font",18,False,False)
    
    # Sprite lists

    all_sprites_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    rock_list = pygame.sprite.Group()
    
    # Create the sprites
    
    my_player = player.Player()
    all_sprites_list.add(my_player)
    
    
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 200)

    ADDROCK = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDROCK, 550)

    bullet_sound = pygame.mixer.Sound("laser5.ogg")
    
    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == ADDENEMY:
                new_enemy = enemy.Enemy()
                enemy_list.add(new_enemy)
                all_sprites_list.add(new_enemy)
            if event.type == ADDROCK:
                new_rock = rocks.Rock()
                rock_list.add(new_rock)
                all_sprites_list.add(new_rock)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    my_player.x_speed = -3
                if event.key == pygame.K_RIGHT:
                    my_player.x_speed = 3
                if event.key == pygame.K_UP:
                    my_player.y_speed = -3
                if event.key == pygame.K_DOWN:
                    my_player.y_speed = 3
                    
                if event.key == pygame.K_SPACE:
                    new_bullet = bullets.Bullet(my_player.rect.x + 35, my_player.rect.y+15)
                    all_sprites_list.add(new_bullet)
                    bullet_list.add(new_bullet)
                    bullet_sound.play()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    my_player.x_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    my_player.y_speed = 0

        #--- Game Logic
        (rock_speed, enemy_speed) = setSpeed()
        bullet_list.update()
        my_player.update()
        rock_list.update(rock_speed)
        enemy_list.update(enemy_speed)

        for bullet in bullet_list:
            hit_enemy_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
            hit_rock_list = pygame.sprite.spritecollide(bullet, rock_list, False)
            for enermy in hit_enemy_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            for rock in hit_rock_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            if bullet.rect.x > screen_width:
                bullet_list.remove(bullet)
                all_sprites.list.remove(bullet)
                
        if pygame.sprite.spritecollideany(my_player, enemy_list):
            done = True       
        if pygame.sprite.spritecollideany(my_player, rock_list):
            done = True
            
        score = font.render("Score: "+ str(time.clock()), True, (0,0,0))
        
        screen.fill((255,255,255))
        all_sprites_list.draw(screen)
        screen.blit(score, (600,5))
        pygame.display.flip()
        clock.tick(60)
        
    pygame.init()

if __name__ == "__main__":

    screen = pygame.display.set_mode((640, 480), 0, 32)

    menu_items = ('Start', 'Quit')
    funcs = {'Start': RunGame,
             'Quit': pygame.quit}

    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()
