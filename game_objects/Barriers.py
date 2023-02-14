#import modules
from math import ceil
from random import randint

#import user modules
from options.MainOptions import (B_HEIGHT, B_WIDTH, S_HEIGHT, B_Y_START, 
                                B_L_START, B_INIT_WIDTH, B_REMOVE, B_CREATE,
                                S_WIDTH)
from game_objects.BarrierBlocks import BarrierBlocks

#class to hold info for all barriers
class Barriers():
    def __init__(self):
        self.barriers = [[], []]
        self.width = B_INIT_WIDTH
        self.x_pos = B_L_START - int(B_WIDTH/2)
        self.create_barriers()

    def create_barriers(self):
        num_r_w_blocks = ceil((S_HEIGHT + abs(B_Y_START)) / (2*B_HEIGHT))
        shift = 0
        for i in range(num_r_w_blocks):
            self.barriers[0].append(BarrierBlocks((B_L_START - int(B_WIDTH/2)), B_Y_START+shift))
            self.barriers[1].append(BarrierBlocks(((B_L_START + self.width) - int(B_WIDTH/2)), B_Y_START+shift))
            shift += (B_HEIGHT*2)

    def get_barriers(self):
        return self.barriers

    def get_barrier_length(self):
        return len(self.barriers[0])

    def get_inner_y_positions(self, car_top, car_bottom):
        left_inner = []
        right_inner = []
        for i in range(self.get_barrier_length()):
            if self.barriers[0][i].get_red_y_pos() >= car_top and self.barriers[0][i].get_white_y_pos() <= car_bottom:
                left_pos = self.barriers[0][i].get_left_x_pos()
                right_pos = self.barriers[1][i].get_right_x_pos()
                if left_pos not in left_inner:
                    left_inner.append(left_pos)
                if right_pos not in right_inner:
                    right_inner.append(right_pos)
        return left_inner, right_inner

    def forward_barriers(self):
        for i in range(self.get_barrier_length()):
            self.barriers[0][i].update_y_pos(4)
            self.barriers[1][i].update_y_pos(4)

    def remove_barriers(self):
        if self.barriers[0][-1].get_white_y_pos() > B_REMOVE:
            self.barriers[0] = self.barriers[0][:-1]
            self.barriers[1] = self.barriers[1][:-1]
    
    def add_barriers(self):
        if self.barriers[0][0].get_white_y_pos() >= B_CREATE:
            self.x_pos_shift()
            self.barriers[0].insert(0, BarrierBlocks(self.x_pos, B_Y_START))
            self.barriers[1].insert(0, BarrierBlocks((self.x_pos + self.width), B_Y_START))

    def x_pos_shift(self):
        r_shift = randint(1, 9)
        if r_shift <= 3:
            self.x_pos -= B_WIDTH
            if self.x_pos <= 0:
                self.x_pos = 0
        elif 3 < r_shift <= 6:
            self.x_pos += B_WIDTH
            if (self.x_pos + self.width + B_WIDTH) >= S_WIDTH:
                self.x_pos = S_WIDTH - B_WIDTH - self.width
        else:
            self.x_pos = self.x_pos