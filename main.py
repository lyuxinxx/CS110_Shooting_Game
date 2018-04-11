import pygame
import MenuItem
from GameMenu import *
import player
import bullets
import enemy
import rocks
import time


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400


def setSpeed():
    t = pygame.time.get_ticks()
    return (8 + t**0.8/800, 4 + t**0.8/800)


class GUI:
    def __init__(self):
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.bg_image = pygame.image.load("image\\bg.png").convert()
        self.font = pygame.font.SysFont("font",18,False,False)
        
        # Sprite lists
        self.all_sprites_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.rock_list = pygame.sprite.Group()
        
        # Create the sprites
        self.player = player.Player()
        self.all_sprites_list.add(self.player)
        
        self.bgm = pygame.mixer.music.load("sound\monkeys.wav")
        pygame.mixer.music.play(1)
        self.bullet_sound = pygame.mixer.Sound("sound\laser5.ogg")

        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.last_time = 0
        done = False
        # main loop
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    
                # move the plane
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.x_speed = -5
                    if event.key == pygame.K_RIGHT:
                        self.player.x_speed = 5
                    if event.key == pygame.K_UP:
                        self.player.y_speed = -5
                    if event.key == pygame.K_DOWN:
                       self.player.y_speed = 5
                    if event.key == pygame.K_SPACE:
                        new_bullet = bullets.Bullet(self.player.rect.x + 35, self.player.rect.y+15)
                        self.all_sprites_list.add(new_bullet)
                        self.bullet_list.add(new_bullet)
                        self.bullet_sound.play()   
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player.x_speed = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.player.y_speed = 0
                        
            # set the difficulty
            self.pass_time = time.time() - self.start_time
            self.enemy_speed = self.pass_time**0.6 + 3
            self.rock_speed =self.pass_time**0.6 + 6

            if self.pass_time < 30:
                if time.time() - self.last_time > 0.75:
                    new_enemy = enemy.Enemy()
                    self.enemy_list.add(new_enemy)
                    self.all_sprites_list.add(new_enemy)
                    new_rock = rocks.Rock()
                    self.rock_list.add(new_rock)
                    self.all_sprites_list.add(new_rock)
                    self.last_time = time.time()
            elif self.pass_time < 50:
                if time.time() - self.last_time > 0.5:
                    new_enemy = enemy.Enemy()
                    self.enemy_list.add(new_enemy)
                    self.all_sprites_list.add(new_enemy)
                    new_rock = rocks.Rock()
                    self.rock_list.add(new_rock)
                    self.all_sprites_list.add(new_rock)
                    self.last_time = time.time()
            elif self.pass_time < 75:
                if time.time() - self.last_time > 0.25:
                    new_enemy = enemy.Enemy()
                    self.enemy_list.add(new_enemy)
                    self.all_sprites_list.add(new_enemy)
                    new_rock = rocks.Rock()
                    self.rock_list.add(new_rock)
                    self.all_sprites_list.add(new_rock)
                    self.last_time = time.time()
                        
            #--- Game Logic
            if pygame.sprite.spritecollideany(self.player, self.enemy_list):
                done = True       
            if pygame.sprite.spritecollideany(self.player, self.rock_list):
                done = True
    
            # update classes
            self.bullet_list.update()
            self.player.update()
            self.rock_list.update(self.rock_speed)
            self.enemy_list.update(self.enemy_speed)
            for bullet in self.bullet_list:
                hit_enemy_list = pygame.sprite.spritecollide(bullet, self.enemy_list, True)
                hit_rock_list = pygame.sprite.spritecollide(bullet, self.rock_list, False)
                for rock in hit_rock_list:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                if bullet.rect.x > screen_width:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                
            # score   
            self.score = self.font.render("Score: "+ str(self.pass_time), True, (0,0,0))
            
            # redraw the screen
            self.screen.blit(self.bg_image,(0,0))
            self.screen.blit(self.score, (0, 5))
            self.all_sprites_list.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()


# driver
def main():
    main_window = GUI()

main()

#if __name__ == "__main__":

 #   screen = pygame.display.set_mode((640, 480), 0, 32)

 #   menu_items = ('Start', 'Quit')
 #   funcs = {'Start': main,
 #            'Quit': pygame.quit}

 #   pygame.display.set_caption('Game Menu')
 #   gm = GameMenu(screen, funcs.keys(), funcs)
 #   gm.run()
