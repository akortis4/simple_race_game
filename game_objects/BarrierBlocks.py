#import modules
from pygame import Rect

#import user modules
from options.MainOptions import B_WIDTH, B_HEIGHT

class BarrierBlocks():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.white_rect = Rect(self.x_pos, self.y_pos, B_WIDTH, B_HEIGHT)
        self.red_rect = Rect(self.x_pos, self.y_pos+B_HEIGHT, B_WIDTH, B_HEIGHT)

    def get_white_rect(self):
        return self.white_rect

    def get_red_rect(self):
        return self.red_rect

    def update_red(self, y_pos):
        pass

    def upate_white(self, y_pos):
        pass