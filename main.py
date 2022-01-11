from game import Game
import pygame

pygame.init()

g = Game((600,600), "TypingSpeed !")
g.run()

pygame.quit()