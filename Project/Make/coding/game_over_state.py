import game_framework
import title_state
from pico2d import *

name = "GameOverState"
image = None
note_image = None
exit_bt = None
restart_bt = None

score = None
font , best_score= None, None
restart_bt_ms_move_sel = 0
exit_bt_ms_move_sel = 0

restart_bt_x , restart_bt_y =500 , 150
exit_bt_x , exit_bt_y = 800, 150

ms_x , ms_y = 0,0

title_bgm = None
#이미지가 그려져서 옆으로 넘어오는 씬
draw_time = 0
print_final_score =0

#game over 인지 판단하는 함수
game_over_or_clear = 0
font_color = [0, 0, 0]

def enter():
    global image
    global note_image
    global exit_bt, restart_bt
    global restart_bt_x , restart_bt_y
    global exit_bt_x, exit_bt_y
    global score, print_final_score

    global title_bgm
    global draw_time
    global font , best_score
    image = load_image('resource\\ui\\result_bg.png')
    note_image = load_image('resource\\ui\\result_note.png')

    exit_bt = load_image('resource\\ui\\exit_bt.png')
    restart_bt = load_image('resource\\ui\\restart_bt.png')

    restart_bt_x, restart_bt_y = 500, 150
    exit_bt_x, exit_bt_y = 800, 150

    title_bgm = load_music('resource\\mp3\\Septentrion.mp3')
    title_bgm.set_volume(40)
    title_bgm.repeat_play()

    draw_time = 0

    font = load_font('ENCR10B.TTF', 100)  # 폰트 업로드
    best_score = load_font('ENCR10B.TTF', 50)
    with open('score_save_Dict\\current_score.json', 'r') as f:
        print_final_score = json.load(f)

    with open('score_save_Dict\\score.json', 'r') as f:
        score = json.load(f)
    score.sort(reverse = True)

    pass


def exit():
    global image
    global exit_bt , restart_bt , note_image, score, font , best_score
    global ms_x , ms_y
    global title_bgm
    ms_x , ms_y = 0,0

    del(image)
    del(exit_bt)
    del(restart_bt)
    del(note_image)
    del score
    del font
    del best_score
    del title_bgm
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
        elif event.type == SDL_MOUSEMOTION:
            ms_x , ms_y = event.x , 1000 - 1 - event.y
            update()
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
    global font , best_score
    global print_final_score , score
    global game_over_or_clear
    global font_color
    clear_canvas()

    image.draw(1200 // 2, 1000 // 2)
    note_image.draw(1200 - draw_time, 1000 //2)

    if draw_time > 1200 // 2:
        exit_bt.clip_draw(0, 60 * exit_bt_ms_move_sel, 109, 118//2, exit_bt_x, exit_bt_y, 109, 118//2)
        restart_bt.clip_draw(0, 60 * restart_bt_ms_move_sel, 168, 114//2, restart_bt_x, restart_bt_y, 168, 114//2)
        if game_over_or_clear > 650:
            best_score.draw(1200 // 2 - 100, 690, 'GAME CLEAR', (font_color[0], font_color[1], font_color[2]))
            font.draw(1200 // 2, 500, '%d' %print_final_score, (200,51,51))
            best_score.draw(450, 600, 'BEST SCORE %d' %score[0], (93,91,160))
        else:
            font.draw(1200 // 2 - 200, 550, 'GAME OVER', (0, 0, 0))

    update_canvas()
    pass

def update():
    global restart_bt_ms_move_sel
    global exit_bt_ms_move_sel
    global ms_x, ms_y
    global draw_time
    global exit_bt_x , exit_bt_y
    global restart_bt_x , restart_bt_y
    global font_color

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

    font_color[0] += 1
    font_color[1] += 5
    font_color[2] += 6

    pass


def pause():
    pass


def resume():
    pass






