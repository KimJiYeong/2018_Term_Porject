import game_framework
from pico2d import *
from shoot import Shoot

import math
import random

import game_world

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
#애니메이션 프레임수
FRAMES_PER_ACTION = 6

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, DOWN_DOWN, UP_UP, DOWN_UP, LE_UP_DOWN , LE_UP_UP,SPACE = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN ,UP_DOWN, LEFT_DOWN) : LE_UP_DOWN,
    (SDL_KEYUP ,SDLK_UP, SDLK_DOWN) : LE_UP_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE

}

current_time = 0
save_time = 0

# Boy States
class IdleState:
    global current_time
    global save_time

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity_x += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity_x -= RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity_x -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity_x += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocity_y -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocity_y += RUN_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocity_y += RUN_SPEED_PPS
        elif event == UP_UP:
            boy.velocity_y -= RUN_SPEED_PPS


        boy.timer = 0
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        boy.timer += 1

        if boy.timer % 100 == 0 :
            boy.change_frame = True

        else:
            boy.change_frame = False

        if boy.change_frame == True:
            boy.frame_num = int((boy.frame_num + 1 ) % 3);

        if boy.change_hit == True:
            if int(boy.frame) < 5:
                boy.frame_num = 3
            else:
                boy.change_hit = False
                boy.frame_num = 0

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 124, 420 - boy.frame_num * 140, 124, 140, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 124, 420 - boy.frame_num * 140, 124, 140, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        # fill here
        if event == RIGHT_DOWN:
            boy.velocity_x += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity_x -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity_x -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity_x += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocity_y -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocity_y += RUN_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocity_y += RUN_SPEED_PPS
        elif event == UP_UP:
            boy.velocity_y -= RUN_SPEED_PPS

        boy.dir = clamp(-1, boy.velocity_x, 1)
        boy.dir_y = clamp(-1, boy.velocity_y, 1)
        pass

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()


    @staticmethod
    def do(boy):
        if boy.dir == 1:
            boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3 + 3
        else :
            boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        # fill here
        boy.x += boy.velocity_x * game_framework.frame_time
        boy.y += boy.velocity_y * game_framework.frame_time

        boy.x = clamp(250, boy.x, 1200 - 250)
        boy.y = clamp(100, boy.y, 1000 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 124, 420 - boy.frame_num * 140, 124, 140, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 124, 420 - boy.frame_num * 140, 124, 140, boy.x, boy.y)




next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_UP: RunState, DOWN_DOWN: RunState, UP_DOWN: RunState, DOWN_UP: RunState,
                LE_UP_DOWN : RunState , LE_UP_UP : RunState,
                SPACE: IdleState },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               UP_UP: IdleState, DOWN_DOWN: IdleState, UP_DOWN: IdleState, DOWN_UP: IdleState,
                LE_UP_DOWN : IdleState , LE_UP_UP : IdleState,
               SPACE: RunState },
}
class Boy:

    def __init__(self):
        # 초기 시작 1200/ 2 // 100
        self.x, self.y = 1200 // 2, 100
        # Boy is only once created, so instance image loading is fine
        #이미지 수정
        self.image = load_image('resource\\ch_move.png')
        # fill here
        self.font = load_font('ENCR10B.TTF' , 16) #폰트 업로드

        self.dir = 1
        self.dir_y = 1

        # 캐릭터 이동
        self.velocity_y = 0
        self.velocity_x = 0

        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        #프레임용
        self.change_frame = False
        self.frame_num = 0
        self.change_hit = False
        self.time = 0
        self.timer = 0

        self.hp = 100

        self.shoot_count = 0



    def fire_ball(self):
        print('Fire Shoot')
        shoot_ball = Shoot(self.x, self.y, 1 * 3)
        game_world.add_object(shoot_ball, 2)
        self.shoot_count += 1
        pass

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
        # 폰트 렌더링
        self.font.draw(self.x - 60, self.y + 50, '(HP : %3.2f)' % self.hp, (255, 0, 0))

        #충돌체크
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    #충돌체크 용 함수
    def get_bb(self):
        return self.x - 30, self.y - 50 , self.x + 25 , self.y + 50

