import game_framework
from pico2d import *
from monster_shoot import Shoot
import math
import main_state
import game_world
import random
from player import Boy

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
ATTACK_PER_TIME = 0.5 / TIME_PER_ACTION
EMERGE_PER_TIME = 0.4 / TIME_PER_ACTION
#애니메이션 프레임수
FRAMES_PER_ACTION = 8

# Boy Event
EMERGE , MOVE, ATTACK, DIE = range(4)

current_time = 0
save_time = 0

boy = None
# Boy States
class emergeState:
    global current_time
    global save_time

    @staticmethod
    def enter(monster, event):
        monster.y = 900
        monster.x = random.randint(300, 800)
        monster.velocity_y = 1
        monster.time = 0
        monster.frame_num = 1
        monster.hp = 100
    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + FRAMES_PER_ACTION * EMERGE_PER_TIME * game_framework.frame_time) % 8
        monster.time += 1
        if monster.time == monster.rand_y:
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
    global boy
    @staticmethod
    def enter(monster, event):
        monster.frame_num = 2
        monster.timer = 0
        monster.time = 1
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        monster.time += 1
        # hp가 0 이 되면 죽는다
        if monster.hp <= 0:
            monster.cur_state = dieState

        if monster.time % 5 == 0:
            monster.velocity_x = random.randint(1, 10)
            monster.dir_y = random.randint(1, 20)

        if monster.time > 200:
            monster.cur_state = attackState

        if monster.velocity_x % 2 == 0:
            monster.x += 2

        else:
            monster.x -= 2

        pass

    @staticmethod
    def draw(monster):
        monster.image.clip_draw(int(monster.frame) * 150, 510 - 2 * 170, 150, 150, monster.x, monster.y)
        pass

class attackState:
    global boy
    @staticmethod
    def enter(monster):
        monster.frame_num = 2
        monster.time = 0

        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + FRAMES_PER_ACTION * ATTACK_PER_TIME * game_framework.frame_time) % 8
        monster.time += 1
        # hp가 0 이 되면 죽는다
        if monster.y < 100:
            monster.cur_state = dieState

        # hp가 0 이 되면 죽는다
        if monster.hp == 0:
            game_world.remove_object(monster)

        if monster.x > monster.arrive_x:
            monster.x -= 1
        elif monster.x < monster.arrive_x:
            monster.x += 1


        monster.x = clamp(250 , monster.x , 1200 - 250)
        monster.y -= 1

    @staticmethod
    def draw(monster):
        monster.image.clip_draw(int(monster.frame) * 150, 510 - 3 * 170, 150, 150, monster.x, monster.y)
        pass

class dieState:

    @staticmethod
    def enter(monster, event):
        monster.time = 100
        monster.opacity = 1

    @staticmethod
    def exit(monster, event):
        monster.opacity = 1
        monster.timer = 0


    @staticmethod
    def do(monster):
        monster.time -= 1
        if monster.time > 10:
            if monster.y >= 0:
                monster.y -= 2
                monster.opacity -= 0.1

        if monster.y == 0:
            game_world.remove_object(monster)

        pass

    @staticmethod
    def draw(monster):
        monster.image.opacify(monster.opacity)
        monster.image.clip_draw(int(monster.frame) * 150, 510 - 4 * 170, 150, 150, monster.x, monster.y)

        pass

next_state_table = {
    emergeState : { EMERGE : emergeState , MOVE : moveState , ATTACK : emergeState ,DIE : emergeState },
    moveState: {EMERGE: moveState, MOVE: moveState, ATTACK: attackState, DIE: dieState},
    attackState: {EMERGE: attackState, MOVE: moveState, ATTACK: attackState, DIE: dieState},
    dieState: {EMERGE: emergeState, MOVE: moveState, ATTACK: attackState, DIE: dieState}

}

class Monster2:

    def __init__(self):
        global boy
        # 초기 시작 1200/ 2 // 100
        self.x, self.y = random.randint(300, 800), 1000

        #이미지 수정
        self.image = load_image('resource\\monster\\monster_B.png')
        # fill here
        self.font = load_font('ENCR10B.TTF' , 16) #폰트 업로드
        self.rand_y = random.randint(50 , 100)
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

        #불투명도
        self.opacity = 1

        self.time = 0
        boy = Boy()
        self.arrive_x =0
        self.arrive_y = 0

    def attack_player(self):
        attack_ball = Shoot(self.x, self.y, -1 * 3)
        game_world.add_object(attack_ball, 3)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        global boy
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        self.arrive_x = main_state.return_x

    def draw(self):

        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(HP : %3.2f)' % self.hp, (255, 0, 0))
        # 충돌체크
        #draw_rectangle(*self.get_bb())

    #충돌체크 용 함수
    def get_bb(self):
        return self.x - 50, self.y - 50 , self.x + 50 , self.y + 50