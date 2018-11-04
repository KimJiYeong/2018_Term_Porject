import game_framework
from pico2d import *
from ball import Ball
import math
import game_world
import random

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3 ) #10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km/Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.8 / TIME_PER_ACTION
EMERGE_PER_TIME = 0.4 / TIME_PER_ACTION
#애니메이션 프레임수
FRAMES_PER_ACTION = 8

# Boy Event
EMERGE , MOVE = range(2)

current_time = 0
save_time = 0

# Boy States
class emergeState:
    global current_time
    global save_time

    @staticmethod
    def enter(monster, event):
        monster.y = 900
        monster.x = random.randint(400, 700)
        monster.velocity_y = 1
        monster.timer = 0
        monster.frame_num = 1

    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + FRAMES_PER_ACTION * EMERGE_PER_TIME * game_framework.frame_time) % 8
        monster.timer += 1
        if monster.timer == 50:
            #state 전환
            monster.cur_state = moveState

        monster.y -= 2

    @staticmethod
    def draw(monster):
        if monster.dir == 1:
            monster.image.clip_draw(int(monster.frame) * 150, 510 - 1 * 170, 150, 150, monster.x, monster.y)
        else:
            monster.image.clip_draw(int(monster.frame) * 150, 510 - 1 * 170, 150, 150, monster.x, monster.y)


class moveState:

    @staticmethod
    def enter(monster, event):
        monster.frame_num = 2
        monster.timer = 0
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        monster.timer += 1
        if monster.timer % 10 == 0:
            monster.velocity_x = random.randint(1, 10)

        if monster.velocity_x % 2 == 0:
            monster.x += 2
            print("t")
        else:
            monster.x -= 2
            print("r")

        monster.x = clamp(250 , monster.x , 1200 - 250)
        pass

    @staticmethod
    def draw(monster):
        monster.image.clip_draw(int(monster.frame) * 150, 510 - 2 * 170, 150, 150, monster.x, monster.y)
        pass


next_state_table = {
}

class Monster:

    def __init__(self):
        # 초기 시작 1200/ 2 // 100
        self.x, self.y = 1200 // 2, 1000

        #이미지 수정
        self.image = load_image('monster_A.png')
        # fill here
        self.font = load_font('ENCR10B.TTF' , 16) #폰트 업로드

        self.dir = 1
        self.dir_y = 1

        # 캐릭터 이동
        self.velocity_y = 0
        self.velocity_x = 0

        self.frame = 0
        self.event_que = []
        #c초기 상태
        self.cur_state = emergeState
        self.cur_state.enter(self, None)

        #프레임용
        self.change_frame = False
        self.frame_num = 1

        #Life
        self.hp = 100

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir_y*3)
        game_world.add_object(ball, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(HP : %3.2f)' % self.hp, (255, 0, 0))
