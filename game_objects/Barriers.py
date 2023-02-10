#import modules
from math import ceil

#import user modules
from options.MainOptions import B_HEIGHT, B_WIDTH, S_HEIGHT, B_Y_START, B_L_START, B_INIT_WIDTH
from game_objects.BarrierBlocks import BarrierBlocks

#class to hold info for all barriers
class Barriers():
    def __init__(self):
        self.barriers = [[], []]
        self.create_barriers()

    def create_barriers(self):
        num_r_w_blocks = ceil((S_HEIGHT + abs(B_Y_START)) / (2*B_HEIGHT))
        shift = 0
        for i in range(num_r_w_blocks):
            self.barriers[0].append(BarrierBlocks((B_L_START - int(B_WIDTH/2)), B_Y_START+shift))
            self.barriers[1].append(BarrierBlocks(((B_L_START + B_INIT_WIDTH) - int(B_WIDTH/2)), B_Y_START+shift))
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