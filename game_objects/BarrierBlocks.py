#import modules
from pygame import Rect

#import user modules
from options.MainOptions import B_WIDTH, B_HEIGHT

#class to hold data for red and white blocks
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

    def get_left_x_pos(self):
        return self.x_pos + B_WIDTH - 3

    def get_right_x_pos(self):
        return self.x_pos + 3

    def get_white_y_pos(self):
        return self.y_pos

    def get_red_y_pos(self):
        return self.y_pos + (B_HEIGHT * 2)

    def update_y_pos(self, y_pos):
        self.y_pos += y_pos
        self.recreate_recs()

    def recreate_recs(self):
        self.white_rect = Rect(self.x_pos, self.y_pos, B_WIDTH, B_HEIGHT)
        self.red_rect = Rect(self.x_pos, self.y_pos+B_HEIGHT, B_WIDTH, B_HEIGHT)