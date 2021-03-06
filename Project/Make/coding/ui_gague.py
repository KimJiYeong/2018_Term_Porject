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
FRAMES_PER_ACTION = 4
monster = None
class UI_gague:
    def __init__(self):
        global monster
        #size = 87 658
        self.image_gauge = load_image('resource\\ui\\Dream_gauge.png')
        self.image_button = load_image('resource\\ui\\Dream_Button.png')

        self.volume = load_music('resource\\mp3\\dream come true.mp3')
        self.volume.set_volume(60)
        self.volume.repeat_play()

        self.button_y = 100
        self.monster_append = 0

    def update(self):
        self.button_y = (self.button_y + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        self.button_y = clamp(100  , self.button_y , 658)
        pass

    def draw(self):
        self.image_gauge.draw(87 + 950, 1000 - 658 + 100)
        self.image_button.draw(87 + 950, self.button_y)

    def exit(self):
        del self.volume
