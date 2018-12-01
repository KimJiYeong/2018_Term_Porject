import random
import json
import os
import json

from pico2d import *
import game_framework
import game_world
import game_over_state

from player import Boy
from monster import Monster
from grass import Grass
from ui_layer import UI_wings
from ui_gague import UI_gague
from ui_heart import  UI_heart
from shoot import Shoot
from ui_Score import  UI_score
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

def enter():
    global boy
    global gauge, ball, monster, balls, score, heart, grass
    boy = Boy()
    monster = Monster()
    grass = Grass()
    ui = UI_wings()
    score = UI_score()
    gauge = UI_gague()
    heart = UI_heart()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(monster, 1)
    game_world.add_object(ui, 4)
    game_world.add_object(score , 4)
    game_world.add_object(gauge, 5)
    game_world.add_object(heart, 5)

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

    game_world.remove_object(heart)
    game_world.remove_object(boy)
    game_world.remove_object(gauge)
    game_world.remove_object(balls)
    game_world.remove_object(ball)
    game_world.remove_object(monster)
    game_world.remove_object(grass)


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
    global time, monster, balls, ball, score, heart, gauge
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)
    for game_object in game_world.check_object(3):
        if game_world.collide(game_object ,boy) == True:
            game_world.remove_object(game_object)
            boy.hp -= 1
            if(boy.hp % 5 == 0): #5 번 맞으면 하트가 한번 깍인다.
                heart.attack_count = clamp(0 , heart.attack_count - 1 , 4)

            if boy.change_hit == False:
                boy.change_hit = True

    for game_object in game_world.check_object(2):
        if game_world.collide(game_object, monster) == True:
            game_world.remove_object(game_object)
            #시연 용 조정
            monster.hp -= 10

            if monster.hp > 0:
                score.score += 10
            pass
    if heart.attack_count == 1 or gauge.button_y > 657:
        game_framework.change_state(game_over_state)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()









