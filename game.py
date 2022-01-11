import pygame
import pygame_textinput
from random import randint

from words import Words


class Game:
    def __init__(self, resolution, title):
        # Pygame configuration
        self.resolution = resolution
        self.win = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(title)

        # Words handling
        self.wds = Words()
        self.wds.parse()
        self.wds.colorTotal()

        # Game elements
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.fnt = pygame.font.SysFont('Courier New', 20)
        testword = self.wds.words[randint(0, len(self.wds.words) - 1)]
        self.textsurface = self.fnt.render(str(testword), False, testword.color)

        # Misc. variables
        self.FPS = 30
        self.running = True

    def commands(self):
        """
        events handling (quit, keys, ...)
        """
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.running = False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_n: # Testing purposes
                    testword = self.wds.words[randint(0, len(self.wds.words) - 1)]
                    self.textsurface = self.fnt.render(str(testword), False, testword.color)

    def render(self):
        """
        assets/elements that needs to be rendered/updated every frames
        """
        self.win.fill((0, 0, 0))  # Make the main screen black every frame
        self.win.blit(self.textsurface, (self.resolution[0]/2, self.resolution[1]/2))

    def run(self):
        """
        The game loop where all the game logic is executed each frame
        """
        while self.running:
            pygame.time.Clock().tick(self.FPS)
            self.commands()
            self.render()
            pygame.display.update()
