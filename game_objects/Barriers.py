#import modules
from math import ceil

#import user modules
from options.MainOptions import B_HEIGHT, B_WIDTH, S_HEIGHT, B_Y_START, B_L_START, B_R_START
from game_objects.BarrierBlocks import BarrierBlocks

class Barriers():
    def __init__(self):
        self.barriers = [[], []]
        self.create_barriers()

    def create_barriers(self):
        num_r_w_blocks = ceil((S_HEIGHT + abs(B_Y_START)) / (2*B_HEIGHT))
        shift = 0
        for i in range(num_r_w_blocks):
            self.barriers[0].append(BarrierBlocks((B_L_START - int(B_WIDTH/2)), B_Y_START+shift))
            self.barriers[1].append(BarrierBlocks((B_R_START - int(B_WIDTH/2)), B_Y_START+shift))
            shift += (B_HEIGHT*2)

    def get_barriers(self):
        return self.barriers

    def get_barrier_length(self):
        return len(self.barriers[0])