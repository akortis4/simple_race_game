#Simple Race Game
#Adam Kortis
#2023

#import modules
import pygame

#import user modules
import options.MainOptions as mo
from game_objects.Car import Car
from game_objects.Barriers import Barriers

#main game class
class SimpleRace():
    def __init__(self):
        self.game = pygame.init()
        self.run_game = True
        self.display = pygame.display.set_mode((mo.S_WIDTH, mo.S_HEIGHT))
        self.clock = pygame.time.Clock()
        self.car = Car()
        self.barriers = Barriers()

    def run(self):
        while self.run_game:
            self.clock.tick(mo.S_REFRESH)
            self.display.fill(mo.GRAY)
            self.draw_objects()
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_game = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run_game = False
            if key[pygame.K_LEFT]:
                self.car.update_pos(0)
            if key[pygame.K_RIGHT]:
                self.car.update_pos(1)
            pygame.display.flip()

    def draw_objects(self):
        pygame.draw.rect(self.display, mo.GREEN, self.car.get_rect())
        barriers = self.barriers.get_barriers()
        for i in range(self.barriers.get_barrier_length()):
            pygame.draw.rect(self.display, mo.WHITE, barriers[0][i].get_white_rect())
            pygame.draw.rect(self.display, mo.RED, barriers[0][i].get_red_rect())
            pygame.draw.rect(self.display, mo.WHITE, barriers[1][i].get_white_rect())
            pygame.draw.rect(self.display, mo.RED, barriers[1][i].get_red_rect())

if __name__ == '__main__':
    SimpleRace().run()