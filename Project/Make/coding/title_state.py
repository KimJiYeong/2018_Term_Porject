import game_framework
import main_state
from pico2d import *
import game_world
from ui_Score import UI_score
import tutorial_state
name = "TitleState"
image = None

exit_bt = None
restart_bt = None

tutorial_bt_ms_move_sel = 0
start_bt_ms_move_sel = 0

tutorial_bt_x , tutorial_bt_y =0 , 0
start_bt_x , start_bt_y = 0, 0

ms_x , ms_y = 0,0

title_bgm = None
score = None

def enter():
    global image
    global start_bt
    global tutorial_bt
    global start_bt_x , start_bt_y
    global tutorial_bt_x , tutorial_bt_y

    global title_bgm

    global score

    tutorial_bt_x, tutorial_bt_y = 1000 - 50, 300
    start_bt_x, start_bt_y = 1000 - 50, 550

    image = load_image('resource\\ui\\title2.png')
    start_bt = load_image('resource\\ui\\start_bt.png')
    tutorial_bt = load_image('resource\\ui\\tutorial_bt.png')

    title_bgm = load_music('resource\\mp3\\Septentrion.mp3')
    title_bgm.set_volume(40)
    title_bgm.repeat_play()

    score = UI_score()
    pass


def exit():
    global image
    global ms_x, mx_y
    global score

    del(image)
    ms_x = 0
    ms_y = 0

    score = 0
    pass


def handle_events():
    global tutorial_bt_ms_move_sel
    global start_bt_ms_move_sel
    global tutorial_bt_x, tutorial_bt_y
    global ms_x, ms_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            ms_x , ms_y = event.x , 1000 - 1 - event.y
            update()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif ((start_bt_x - 100) < ms_x) and (ms_x < (start_bt_x + 100)) and ((start_bt_y - 50) < ms_y) and (ms_y < (start_bt_y + 50)):
                game_framework.change_state(main_state)
            elif ((tutorial_bt_x - 100) < ms_x) and (ms_x < (tutorial_bt_x + 100)) and ((tutorial_bt_y - 50) < ms_y) and (
                    ms_y < (tutorial_bt_y + 50)):
                game_framework.change_state(tutorial_state)
    pass

def draw():
    global tutorial_bt_ms_move_sel
    global start_bt_ms_move_sel
    global start_bt_x , start_bt_y
    global tutorial_bt_x , tutorial_bt_y
    global start_bt, tutorial_bt
    clear_canvas()

    image.draw(1200 // 2, 1000 // 2)

    start_bt.clip_draw(0, 60 * start_bt_ms_move_sel, 250, 60, start_bt_x, start_bt_y, 250, 60)
    tutorial_bt.clip_draw(0, 60 * tutorial_bt_ms_move_sel, 250, 60, tutorial_bt_x, tutorial_bt_y, 250, 60)

    update_canvas()
    pass

def update():
    global tutorial_bt_ms_move_sel
    global start_bt_ms_move_sel
    global ms_x, ms_y
    global start_bt_x , start_bt_y
    global tutorial_bt_x , tutorial_bt_y


    if ((tutorial_bt_x - 100) < ms_x ) and (ms_x < (tutorial_bt_x + 100)) and ((tutorial_bt_y - 50) < ms_y )and (ms_y < (tutorial_bt_y + 50)):
        tutorial_bt_ms_move_sel = 0
    else:
        tutorial_bt_ms_move_sel = 1

    if ((start_bt_x - 100) < ms_x) and (ms_x < (start_bt_x + 100)) and ((start_bt_y - 50) < ms_y) and (ms_y < (start_bt_y + 50)):
        start_bt_ms_move_sel = 0
    else:
        start_bt_ms_move_sel = 1
    pass


def pause():
    pass


def resume():
    pass






