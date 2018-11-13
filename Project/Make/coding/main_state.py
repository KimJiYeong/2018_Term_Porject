import random
import json
import os

from pico2d import *
import game_framework
import game_world

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
def enter():
    global boy
    global gauge, ball, monster, balls, score, heart
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
    global boy, grass
    del boy
    del grass
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    global time, monster, balls, ball, score, heart
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)
    for game_object in game_world.check_object(3):
        if game_world.collide(game_object ,boy) == True:
            game_world.remove_object(game_object)
            boy.hp -= 1
            if(boy.hp % 10 == 0): #10 번 맞으면 하트가 한번 깍인다.
                heart.attack_count -= 1
            if boy.change_hit == False:
                boy.change_hit = True

    for game_object in game_world.check_object(2):
        if game_world.collide(game_object, monster) == True:
            game_world.remove_object(game_object)
            #시연 용 조정
            monster.hp -= 10
            score.score += 10
            #몬스터가 없어도 점수가 올라가는 버그 발생
            pass



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()









