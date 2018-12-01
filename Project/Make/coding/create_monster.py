from pico2d import *
import game_framework
import game_world
from monster_A import Monster
PIXEL_PER_METER = (10.0 / 0.3 ) #10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km/Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1 / TIME_PER_ACTION
#애니메이션 프레임수
FRAMES_PER_ACTION = 5
monster = None
class create_Monseter:
    def __init__(self):
        global monster
        #size = 87 658
        self.monster_append = 0
        monster = Monster()

    def update(self):

        pass

    def draw(self):
        pass
    def exit(self):
        pass

    def create(self):

        pass
    def clear(self):
         game_world.remove_object(self)
