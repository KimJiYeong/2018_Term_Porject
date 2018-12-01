import game_framework
import title_state
from pico2d import *

from ui_Score import  UI_score

name = "TitleState"
image = None
note_image = None
exit_bt = None
restart_bt = None

score = None
font = None
restart_bt_ms_move_sel = 0
exit_bt_ms_move_sel = 0

restart_bt_x , restart_bt_y =500 , 150
exit_bt_x , exit_bt_y = 800, 150

ms_x , ms_y = 0,0

title_bgm = None
#이미지가 그려져서 옆으로 넘어오는 씬
draw_time = 0
print_final_score =0

def enter():
    global image
    global note_image
    global exit_bt, restart_bt
    global score
    global title_bgm
    global print_final_score
    global draw_time
    global font
    image = load_image('resource\\result_bg.png')
    note_image = load_image('resource\\result_note.png')

    exit_bt = load_image('resource\\exit_bt.png')
    restart_bt = load_image('resource\\restart_bt.png')

    title_bgm = load_music('resource\\Septentrion.mp3')
    title_bgm.set_volume(40)
    title_bgm.repeat_play()

    draw_time =0

    score = UI_score()
    print_final_score = score.score

    font = load_font('ENCR10B.TTF', 100)  # 폰트 업로드

    pass


def exit():
    global image
    global exit_bt , restart_bt , note_image
    del(image)
    del(exit_bt)
    del(restart_bt)
    del(note_image)
    pass


def handle_events():
    global restart_bt_ms_move_sel
    global exit_bt_ms_move_sel
    global restart_bt_x, restart_bt_y
    global exit_bt_x , exit_bt_y
    global ms_x, ms_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif ((restart_bt_x - 100) < ms_x) and (ms_x < (restart_bt_x + 100)) and ((restart_bt_y - 50) < ms_y) and (
                        ms_y < (restart_bt_y + 50)):
                game_framework.change_state(title_state)
            elif ((exit_bt_x - 100) < ms_x) and (ms_x < (exit_bt_x + 100)) and ((exit_bt_y - 50) < ms_y) and (
                    ms_y < (exit_bt_y + 50)):
                game_framework.quit()

    pass

def draw():
    global restart_bt_ms_move_sel
    global exit_bt_ms_move_sel
    global image
    global note_image
    global draw_time
    global exit_bt_x , exit_bt_y
    global restart_bt_x , restart_bt_y
    global font
    global print_final_score
    clear_canvas()

    image.draw(1200 // 2, 1000 // 2)
    note_image.draw(1200 - draw_time, 1000 //2)

    if draw_time > 1200 // 2:
        exit_bt.clip_draw(0, 60 * exit_bt_ms_move_sel, 109, 118//2, exit_bt_x, exit_bt_y, 109, 118//2)
        restart_bt.clip_draw(0, 60 * restart_bt_ms_move_sel, 168, 114//2, restart_bt_x, restart_bt_y, 168, 114//2)
        font.draw(1200 // 2, 600, '%d' % print_final_score, (93,91,160))

    update_canvas()
    pass

def update():
    global restart_bt_ms_move_sel
    global exit_bt_ms_move_sel
    global ms_x, ms_y
    global draw_time

    global exit_bt_x , exit_bt_y
    global restart_bt_x , restart_bt_y

    draw_time = clamp(0,draw_time, 1200 // 2)
    draw_time += 1


    if ((restart_bt_x - 100) < ms_x ) and (ms_x < (restart_bt_x + 100)) and ((restart_bt_y - 50) < ms_y )and (ms_y < (restart_bt_y + 50)):
        restart_bt_ms_move_sel = 0
    else:
        restart_bt_ms_move_sel = 1

    if ((exit_bt_x - 100) < ms_x) and (ms_x < (exit_bt_x + 100)) and ((exit_bt_y - 50) < ms_y) and (ms_y < (exit_bt_y + 50)):
        exit_bt_ms_move_sel = 0
    else:
        exit_bt_ms_move_sel = 1

    pass


def pause():
    pass


def resume():
    pass






