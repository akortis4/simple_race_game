#Simple Race Game
#Adam Kortis
#2023

#import modules
import pygame

#import user modules
import options.MainOptions as mo

#main game class
class SimpleRace():
    def __init__(self):
        self.game = pygame.init()
        self.run_game = True
        self.display = pygame.display.set_mode((mo.S_WIDTH, mo.S_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while self.run_game:
            self.clock.tick(mo.S_REFRESH)
            self.display.fill(mo.S_BACKGROUND)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_game = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run_game = False
            pygame.display.flip()

if __name__ == '__main__':
    SimpleRace().run()