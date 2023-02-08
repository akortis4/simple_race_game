#import modules
from pygame import Rect

#import user modules
from options.MainOptions import S_WIDTH, C_HEIGHT, C_WIDTH, C_Y_START

class Car():
    def __init__(self):
        self.x_pos = (S_WIDTH/2 - (C_WIDTH/2))
        self.x_min = 0
        self.x_max = S_WIDTH - C_WIDTH
        self.rect = Rect(self.x_pos, C_Y_START, C_WIDTH, C_HEIGHT)

    def get_rect(self):
        return self.rect

    def update_pos(self, direction:int):
        if direction == 0:
            if self.x_pos <= self.x_min:
                self.x_pos = self.x_min
            else:
                self.x_pos -= 10
        else:
            if self.x_pos >= self.x_max:
                self.x_pos = self.x_max
            else:
                self.x_pos += 10
        self.rect = Rect(self.x_pos, C_Y_START, C_WIDTH, C_HEIGHT)