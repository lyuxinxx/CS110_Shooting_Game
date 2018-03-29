import pygame
import random
from Classes import *

def main():
    print("####### testing player model######")

    test_player = Player()
    #print(test_player.rect.center)


    print("=====Standard Input Test=====")

    test_player.move(pygame.K_UP)
    assert test_player.getCoordinates() == (0,-5)

    test_player = Player()
    #print(test_player.rect.center)
    print("=====Standard Input Test=====")

    test_player.move(pygame.K_DOWN)
    assert test_player.getCoordinates() == (0,5)

    test_player = Player()
    #print(test_player.rect.center)
    print("=====Standard Input Test=====")

    test_player.move(pygame.K_LEFT)
    assert test_player.getCoordinates() == (-5,0)

    test_player = Player()
    #print(test_player.rect.center)
    print("=====Standard Input Test=====")

    test_player.move(pygame.K_RIGHT)
    assert test_player.getCoordinates() == (5,0)

    print("######## player test complete#######")

    

main()
