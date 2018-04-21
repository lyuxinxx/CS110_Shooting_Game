import pygame
import time
from GameMenu import *
from HelpMenu import *
from src import player as pl
from src import bullets as bt
from src import enemies as em
from src import rocks as rk
from src import scoreData
from main_2 import *

def main():
    #test bullets model
    print("####### testing bullets model######")
    test_bullet = bt.Bullet(9,8)
    
    print("=====Standard Initialization Test=====")
    assert test_bullet.rect.x == 9
    assert test_bullet.rect.y == 8
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_bullet.update() 
    assert test_bullet.rect.x == 9 + 13
    assert test_bullet.rect.y == 8
    print("=====Pass=====")
    
    print("######## bullets test complete#######\n")



    # test enemy model
    print("####### testing enemy model######")

    test_enemy = em.Enemy()

    print("=====Standard Initialization Test=====")
    assert test_enemy.rect.x == screen_width
    assert test_enemy.rect.y < screen_height
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_enemy.update()
    assert test_enemy.rect.x == 700 - 2
    assert test_enemy.rect.y <= 400 + 3
    print("=====Pass=====")
    
    print("######## enemy test complete#######\n")

    #test GameMenu model
    print("####### testing GameMenu model######")
    test_menu = GameMenu(pygame.display.set_mode((700, 400), 0, 32),('Start', 'Quit'),{'Start': print("start")})
    
    print("=====Standard Initialization Test=====")
    assert test_menu.mouse_is_visible == True
    assert test_menu.cur_item == None
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_menu.set_mouse_visibility()
    assert pygame.mouse.set_visible(True)
    test_menu.set_keyboard_selection(pygame.K_UP)
    assert test_menu.cur_item == 0
    print("=====Pass=====")
    
    print("######## GameMenu test complete#######\n")

    #test MenuItem model
    print("####### testing MenuItem model######")
    test_menuitem = MenuItem("\u6211", None, 30, WHITE)
    
    print("=====Standard Initialization Test=====")
    assert test_menuitem.text == "\u6211"
    assert test_menuitem.font_size == 30
    assert test_menuitem.font_color == WHITE
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    assert test_menuitem.is_mouse_selection((2,3))
    test_menuitem.set_position(0,0)
    assert test_menuitem.pos_x == 0
    assert test_menuitem.pos_y == 0
    test_menuitem.set_font_color((0,0,0))
    assert test_menuitem.font_color == (0,0,0)
    print("=====Pass=====")
    
    print("######## MenuItem test complete#######\n")

    # test initialization of the help menu
    print("####### testing HelpMenu model######")
    print("=====Standard Initialization Test=====")
    test_menu = HelpMenu()
    print("=====Pass=====")

    print("######## HelpMenu test complete#######\n")
    
    # test player model
    print("####### testing player model######")
    test_player = pl.Player()
    
    print("=====Standard Initialization Test=====")
    assert test_player.rect.x == 0
    assert test_player.rect.y == 200
    assert test_player.x_speed == 0
    assert test_player.y_speed == 0
    print("=====Pass=====")

    print("=====Standard Function Test=====")
    test_player.update()
    assert test_player.rect.x == 0
    assert test_player.rect.y == 200
    print("=====Pass=====")

    
    print("######## player test complete#######\n")

    #test rocks model
    print("####### testing player model######")
    test_rock = rk.Rock()
    
    print("=====Standard Initialization Test=====")
    assert test_rock.rect.x == 700
    assert test_rock.rect.y < 400
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_rock.update()
    assert test_rock.rect.x == 700 - 6
    print("=====Pass=====")

    print("######## rocks test complete#######\n")

    

    pygame.quit()

main()
