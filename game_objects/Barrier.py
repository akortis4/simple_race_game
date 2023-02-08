#import modules
from pygame import Rect

#import user modules
from options.MainOptions import WHITE, B_WIDTH, B_HEIGHT

class Barriers():
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.white_rect = None
        self.red_rect = None

    def get_white_rect(self):
        return self.white_rect

    def get_red_rect(self):
        return self.red_rect