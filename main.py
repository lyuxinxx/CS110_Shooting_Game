import pygame
import time
import sys
from GameMenu import *
from src import player
from src import bullets
from src import enemies
from src import rocks
from src import scoreData
from HelpMenu import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400


class Controller:
    def __init__(self):
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.bg_image = pygame.image.load("assets\\bg.png").convert()
        pygame.display.set_caption("Space Shooter 2")

        # Font
        self.font = pygame.font.SysFont("font",20)

        # Music
        self.bgm = pygame.mixer.music.load("assets\monkeys.wav")
        pygame.mixer.music.play(1)
        self.bullet_sound = pygame.mixer.Sound("assets\laser5.ogg")
        
        # Sprite lists
        self.enemy_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.rock_list = pygame.sprite.Group()
        
        # Create the player
        self.player = player.Player()

        # initiate the time
        self.start_time = time.time()
        self.pass_time = 0
        self.last_time = 0
        
        #initiate the score:
        self.hit_score = 0
        self.total_score = 0
        self.score_data = scoreData.ScoreData()

        self.clock = pygame.time.Clock()
        
        done = False

        # main loop
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    
                elif event.type == pygame.KEYDOWN:
                    
                    # shoot
                    if event.key == pygame.K_SPACE:
                        bullet_x = self.player.rect.x + self.player.image.get_width()
                        bullet_y = self.player.rect.y + 8
                        self.bullet_list.add(bullets.Bullet(bullet_x, bullet_y))
                        self.bullet_sound.play()
                    # move the plane
                    if event.key == pygame.K_LEFT:
                        self.player.x_speed = -5
                    if event.key == pygame.K_RIGHT:
                        self.player.x_speed = 5
                    if event.key == pygame.K_UP:
                        self.player.y_speed = -5
                    if event.key == pygame.K_DOWN:
                       self.player.y_speed = 5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player.x_speed = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.player.y_speed = 0
                        
            # set the difficulty
            self.pass_time = time.time() - self.start_time
            self.enemy_speed = self.pass_time ** 0.6 + 3
            self.rock_speed = self.pass_time ** 0.6 + 6

            # create rocks and enemies
            if self.pass_time < 30:
                if time.time() - self.last_time > 0.75:
                    self.enemy_list.add(enemies.Enemy(self.enemy_speed)) 
                    self.rock_list.add(rocks.Rock(self.rock_speed))
                    self.last_time = time.time()
            elif self.pass_time < 50:
                if time.time() - self.last_time > 0.5:
                    self.enemy_list.add(enemies.Enemy(self.enemy_speed)) 
                    self.rock_list.add(rocks.Rock(self.rock_speed))
                    self.last_time = time.time()
            elif self.pass_time < 75:
                if time.time() - self.last_time > 0.25:
                    self.enemy_list.add(enemies.Enemy(self.enemy_speed)) 
                    self.rock_list.add(rocks.Rock(self.rock_speed))
                    self.last_time = time.time()

            #--- Game Logic

                
            collide_list1 = pygame.sprite.spritecollideany(self.player, self.enemy_list) 
            collide_list2 = pygame.sprite.spritecollideany(self.player, self.rock_list)
            if collide_list1 or collide_list2:
                self.screen = pygame.display.set_mode((screen_width,screen_height))
                self.bg_image = pygame.image.load("assets\\bg.png").convert()
                pygame.display.set_caption("GAME OVER")
                self.font = pygame.font.SysFont("font",30)
                self.game_over = self.font.render("Game Over", True, WHITE)
                self.your_score = self.font.render("Your Score: " + str(self.total_score), True, WHITE)
                self.highest_score = self.font.render("Highest Score: " + str(self.score_data.best), True, WHITE)
                self.text_rect = self.game_over.get_rect()
                self.text_x = self.screen.get_width() / 2 - self.text_rect.width / 2
                self.text_y = self.screen.get_height() / 2 - self.text_rect.height / 2
                self.screen.blit(self.bg_image,(0,0))
                self.screen.blit(self.game_over, [self.text_x, self.text_y-20])
                self.screen.blit(self.your_score, [self.text_x, self.text_y+20])
                self.screen.blit(self.highest_score, [self.text_x, self.text_y+50])

                
                pygame.display.flip()
                time.sleep(3)
                done = True
                
    
            # update classes
            self.all_sprites_list= pygame.sprite.Group((self.player,)+tuple(self.enemy_list)+tuple(self.rock_list)+tuple(self.bullet_list))
            self.all_sprites_list.update()
            
            for bullet in self.bullet_list:
                hit_enemy_list = pygame.sprite.spritecollide(bullet, self.enemy_list, True)
                for enemy in hit_enemy_list:
                    self.hit_score += 2
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                hit_rock_list = pygame.sprite.spritecollide(bullet, self.rock_list, False)
                for rock in hit_rock_list:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                if bullet.rect.x > screen_width:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                
            # score
            self.total_score = int(self.hit_score + self.pass_time)
            if self.total_score > self.score_data.best:
                self.score_data.best = self.total_score
                self.score_data.update()
            self.score = self.font.render("Score: "+ str(self.total_score), True, WHITE)
            self.best_score = self.font.render("Best: "+ str(self.score_data.best), True, WHITE)

            
            # redraw the screen
            self.screen.blit(self.bg_image,(0,0))
            self.screen.blit(self.score, (screen_width - 100, 5))
            self.screen.blit(self.best_score, (screen_width - 100, 20))
            self.all_sprites_list.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.init()

    


def QuitGame():
    pygame.quit()
    sys.exit()



# ---driver---
def main():

    if __name__ == "__main__":

        pygame.init()

        screen = pygame.display.set_mode((700, 400), 0, 32)

        menu_items = ('Start', 'Quit')
        funcs = {'Start': Controller,
                 'Help':HelpMenu,
              'Quit': QuitGame}

        pygame.display.set_caption('Game Menu')
        gm = GameMenu(screen, funcs.keys(), funcs)
        gm.run()
        pygame.quit()
   
main()
