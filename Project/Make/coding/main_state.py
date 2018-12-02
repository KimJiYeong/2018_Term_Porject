import random
import json
import os
import json

from pico2d import *
import game_framework
import game_world
import game_over_state

from player import Boy
from monster_A import Monster
from background import Background
from ui_layer import UI_wings
from ui_gague import UI_gague
from ui_heart import  UI_heart
from shoot import Shoot
from ui_Score import  UI_score
from create_monster import create_Monseter
from monster_B import Monster2
name = "MainState"

boy = None
gauge = None
ball = None
monster = None
time = 0
balls = None
score = None
heart = None

#점수 저장 파일 입출력
returnScore = []
monster2 = []

temp_time = 0

global return_x
regen_time =0

def enter():
    global boy
    global gauge, ball, monster, balls, score, heart, grass, temp_time, regen_time
    boy = Boy()
    monster = Monster()
    grass = Background()
    ui = UI_wings()
    score = UI_score()
    gauge = UI_gague()
    heart = UI_heart()
    temp_time = 0
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)

    game_world.add_object(ui, 6)
    game_world.add_object(score , 7)
    game_world.add_object(gauge, 7)
    game_world.add_object(heart, 7)

    regen_time = 0

def exit():
    global boy
    global gauge, ball, monster, balls,  heart, grass, score
    global returnScore

    with open('score_save_Dict\\current_score.json', 'w') as f:
        json.dump(score.score, f)

    #점수 저장을 위해 먼저 점수를 불러오기
    with open('score_save_Dict\\score.json', 'r') as f:
        returnScore = json.load(f)

    returnScore.append(score.score)
    #점수 병합 후 합치기0
    with open('score_save_Dict\\score.json', 'w') as f:
        json.dump(returnScore, f)

    game_over_state.game_over_or_clear = gauge.button_y
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global heart, gauge
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)



def update():
    global time, monster, balls, ball, score, heart, gauge, monster2, temp_time, boy, return_x
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)
    for game_object in game_world.check_object(3):
        if game_world.collide(game_object ,boy) == True:
            game_world.remove_object(game_object)
            boy.hp -= 1
            boy.volume2.play()
            if(boy.hp % 5 == 0): #5 번 맞으면 하트가 한번 깍인다.
                heart.attack_count = clamp(0 , heart.attack_count - 1 , 4)

            if boy.change_hit == False:
                boy.frame = 0
                boy.change_hit = True
    for game_object in game_world.check_object(5):
        if game_world.collide(game_object, boy) == True:
            game_world.remove_object(game_object)
            boy.hp -= 1
            boy.volume2.play()
            if (boy.hp % 5 == 0):  # 5 번 맞으면 하트가 한번 깍인다.
                heart.attack_count = clamp(0, heart.attack_count - 1, 4)

            if boy.change_hit == False:
                boy.frame = 0
                boy.change_hit = True


    for game_object2 in game_world.check_object(5):
        for game_object in game_world.check_object(2):
            if game_world.collide(game_object2, game_object) == True:
                game_world.remove_object(game_object)
                #시연 용 조정
                game_object2.hp -= 5
                gauge.button_y += 1
                boy.volume.play()
                if game_object2.hp > 0:
                    score.score += 10

    #스페셜 공격시 몬스터 맞을때
    for game_object2 in game_world.check_object(5):
        for game_object in game_world.check_object(4):
            if game_world.collide(game_object2, game_object) == True:
                game_world.remove_object(game_object)
                # 시연 용 조정
                game_object2.hp -= 50
                gauge.button_y += 1.5
                boy.volume.play()
                if game_object2.hp > 0:
                    score.score += 15
                pass
    if heart.attack_count == 1 or gauge.button_y > 657:
        game_framework.change_state(game_over_state)

    global regen_time
    regen_time = clamp(0, regen_time + 1 , 400)
    if temp_time % (1000 - regen_time) == 0:
        tmp = Monster()
        game_world.add_object(tmp, 5)
        tmp = None

    if temp_time % (1200 - regen_time) == 0:
        tmp = Monster2()
        game_world.add_object(tmp, 5)
        tmp = None

    temp_time += 1

    return_x = boy.return_x()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()









