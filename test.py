import pygame
import random
from bullets import *
from enemies import *
from GameMenu import *
from MenuItem import *
from player import *
from rocks import *
from main import *

def main():
    #test bullets model
    print("####### testing bullets model######")
    pygame.display.init()
    test_bullet = Bullet(9,8)
    
    print("=====Standard Initialization Test=====")
    assert test_bullet.rect.x == 9
    assert test_bullet.rect.y == 8
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_bullet.update()
    assert True
    print("=====Pass=====")
    
    print("######## bullets test complete#######\n")

    pygame.quit()


    # test enemy model
    print("####### testing enemy model######")

    test_enemy = Enemy()

    print("=====Standard Initialization Test=====")
    assert test_enemy.rect.x == screen_width
    assert test_enemy.rect.y < screen_height
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_enemy.update()
    assert True
    print("=====Pass=====")
    
    print("######## enemy test complete#######\n")

    #test GameMenu model
    print("####### testing GameMenu model######")
    pygame.init()
    test_menu = GameMenu(pygame.display.set_mode((700, 400), 0, 32),('Start', 'Quit'),{'Start': print("start")})
    
    print("=====Standard Initialization Test=====")
    assert test_menu.mouse_is_visible == True
    assert test_menu.cur_item == None
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_menu.set_mouse_visibility()
    test_menu.set_keyboard_selection(pygame.K_UP)
    assert True
    print("=====Pass=====")
    
    print("######## GameMenu test complete#######\n")

    #test MenuItem model
    print("####### testing MenuItem model######")
    pygame.init()
    test_menuitem = MenuItem("\u6211", None, 30, WHITE)
    
    print("=====Standard Initialization Test=====")
    assert test_menuitem.text == "\u6211"
    assert test_menuitem.font_size == 30
    assert test_menuitem.font_color == WHITE
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_menuitem.is_mouse_selection((2,3))
    test_menuitem.set_position(0,0)
    test_menuitem.set_font_color((0,0,0))
    assert True
    print("=====Pass=====")
    
    print("######## MenuItem test complete#######\n")

    
    # test player model
    print("####### testing player model######")
    pygame.display.init()
    pygame.display.set_mode((700, 400), 0, 32)
    test_player = Player()
    
    print("=====Standard Initialization Test=====")
    assert test_player.rect.x == 0
    assert test_player.rect.y == 200
    assert test_player.x_speed == 0
    assert test_player.y_speed == 0
    print("=====Pass=====")

    print("=====Standard Function Test=====")
    test_player.update()
    assert True
    print("=====Pass=====")

    
    print("######## player test complete#######\n")

    #test rocks model
    print("####### testing player model######")
    test_rock = Rock()
    
    print("=====Standard Initialization Test=====")
    assert test_rock.rect.x == 700
    assert test_rock.rect.y < 400
    print("=====Pass=====")
    
    print("=====Standard Function Test=====")
    test_rock.update()
    assert True
    print("=====Pass=====")

    print("######## rocks test complete#######\n")

    pygame.quit()

main()
