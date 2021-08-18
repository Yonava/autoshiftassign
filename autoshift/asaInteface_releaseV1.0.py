from typing import TYPE_CHECKING
import pygame
import os
import sys
from collections import Counter
import random

pygame.init()

WIDTH, HEIGHT = 960, 540
window = (WIDTH, HEIGHT)


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (255, 100, 100)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (125, 125, 125)
DARK_RED = (200, 0, 0)
LIGHT_GRAY = (210, 210, 210)
YELLOW = (255, 223, 0)
DARK_BLUE = (0, 0, 150)
PINK = (255, 182, 193)
HOT_PINK = (255, 105, 180)
DARK_GREEN = (0, 200, 0)
GOLD = (212, 175, 55)

# name, boards, dining, cash, expo, baskets, bird, toast
employee_list = [['Yona',1,5,3,3,1,1,2],['Alex',1,2,1,1,5,5,4],['Isabella',0,3,4,5,0,0,0],['Fox',5,1,2,3,2,5,2],['Ari',5,1,1,2,3,3,2],['Sammy',2,1,2,3,4,5,5],['Arryan',1,4,3,1,1,1,2],['Caleb',0,3,0,1,4,5,3],['Eli',1,1,1,1,3,3,3],['Maya',0,3,4,3,0,0,0],['Jacob',3,2,5,3,4,1,3],['Emma',5,1,2,1,3,1,3]]

logo = pygame.image.load(os.path.join('caneslove', 'logo.png'))
logo = pygame.transform.scale(logo, (int((logo.get_width()/4)), int((logo.get_height()/4))))
pygame.image.load(os.path.join('caneslove', 'schedule.jpg'))

github_url = 'github.com/yonava'
FPS = 60
clock = pygame.time.Clock()
WIN = pygame.display.set_mode(window)
pygame.display.set_caption('Raising Canes Shift Assign (c714)')
pygame.display.set_icon(logo)
schedule = pygame.transform.scale(pygame.image.load(os.path.join('caneslove', 'schedule.jpg')), window)
base_font = pygame.font.SysFont('Gadugi Bold', 40)
big_font = pygame.font.SysFont('Gadugi Bold', 120)
ratings_font = pygame.font.SysFont('Gadugi Bold', 30)
fineprint_font = pygame.font.SysFont('Arial', 20)

crew_text = ''
crew_rating_int = ''
am_pm = ''

# main_menu buttons
build_schedule_button = base_font.render('Generate New Schedule', False, ORANGE)
add_crew_button = base_font.render('Add Crew', False, GREEN)
del_crew_button = base_font.render('Remove Crew', False, RED)
build_version = fineprint_font.render('asa release v1.0: by Yona V-A (yonava.com/github)', False, BLACK)

# build_sheet buttons
am_button = big_font.render('AM', False, YELLOW)
pm_button = big_font.render('PM', False, BLUE)
joyce_button = base_font.render('Joyce', False, BLACK)
aidee_button = base_font.render('Aidee', False, BLACK)
isiah_button = base_font.render('Isiah', False, BLACK)
ismael_button = base_font.render('Ismael', False, BLACK)
continue_button = base_font.render('Continue', False, (0,200,0))

# generate_schedule buttons
exit_button = base_font.render('Return To Main Menu', False, BLACK)

# add_crew buttons
# board buttons
bb0 = ratings_font.render('0', False, BLACK)
bb1 = ratings_font.render('1', False, BLACK)
bb2 = ratings_font.render('2', False, BLACK)
bb3 = ratings_font.render('3', False, BLACK)
bb4 = ratings_font.render('4', False, BLACK)
bb5 = ratings_font.render('5', False, BLACK)
bb_list = [bb0,bb1,bb2,bb3,bb4,bb5]
boards = ratings_font.render('Boards:', False, BLACK)

# dining buttons
db0 = ratings_font.render('0', False, BLACK)
db1 = ratings_font.render('1', False, BLACK)
db2 = ratings_font.render('2', False, BLACK)
db3 = ratings_font.render('3', False, BLACK)
db4 = ratings_font.render('4', False, BLACK)
db5 = ratings_font.render('5', False, BLACK)
db_list = [db0,db1,db2,db3,db4,db5]
dining = ratings_font.render('Dining Room:', False, BLACK)

# cashier buttons
cb0 = ratings_font.render('0', False, BLACK)
cb1 = ratings_font.render('1', False, BLACK)
cb2 = ratings_font.render('2', False, BLACK)
cb3 = ratings_font.render('3', False, BLACK)
cb4 = ratings_font.render('4', False, BLACK)
cb5 = ratings_font.render('5', False, BLACK)
cb_list = [cb0,cb1,cb2,cb3,cb4,cb5]
cashier = ratings_font.render('Cashier:', False, BLACK)

# expo buttons
eb0 = ratings_font.render('0', False, BLACK)
eb1 = ratings_font.render('1', False, BLACK)
eb2 = ratings_font.render('2', False, BLACK)
eb3 = ratings_font.render('3', False, BLACK)
eb4 = ratings_font.render('4', False, BLACK)
eb5 = ratings_font.render('5', False, BLACK)
eb_list = [eb0,eb1,eb2,eb3,eb4,eb5]
expo = ratings_font.render('Expo:', False, BLACK)

# basket buttons
bab0 = ratings_font.render('0', False, BLACK)
bab1 = ratings_font.render('1', False, BLACK)
bab2 = ratings_font.render('2', False, BLACK)
bab3 = ratings_font.render('3', False, BLACK)
bab4 = ratings_font.render('4', False, BLACK)
bab5 = ratings_font.render('5', False, BLACK)
bab_list = [bab0,bab1,bab2,bab3,bab4,bab5]
baskets = ratings_font.render('Baskets:', False, BLACK)

# bird buttons
bib0 = ratings_font.render('0', False, BLACK)
bib1 = ratings_font.render('1', False, BLACK)
bib2 = ratings_font.render('2', False, BLACK)
bib3 = ratings_font.render('3', False, BLACK)
bib4 = ratings_font.render('4', False, BLACK)
bib5 = ratings_font.render('5', False, BLACK)
bib_list = [bib0,bib1,bib2,bib3,bib4,bib5]
bird = ratings_font.render('Bird:', False, BLACK)

# toast buttons
tb0 = ratings_font.render('0', False, BLACK)
tb1 = ratings_font.render('1', False, BLACK)
tb2 = ratings_font.render('2', False, BLACK)
tb3 = ratings_font.render('3', False, BLACK)
tb4 = ratings_font.render('4', False, BLACK)
tb5 = ratings_font.render('5', False, BLACK)
tb_list = [tb0,tb1,tb2,tb3,tb4,tb5]
toast = ratings_font.render('Toast:', False, BLACK)

save_button = base_font.render('Save and Exit', False, BLACK)
name_button = ratings_font.render('Name:', False, BLACK)

# main_menu sprites
build_button_hitbox = pygame.Rect(((WIDTH/2)-(build_schedule_button.get_width()/2)), (HEIGHT/2-30), (build_schedule_button.get_width()), (build_schedule_button.get_height()))
add_crew_hitbox = pygame.Rect(((WIDTH/2)-(add_crew_button.get_width()/2)), (HEIGHT/2+30), (add_crew_button.get_width()), (add_crew_button.get_height()))
del_crew_hitbox = pygame.Rect(((WIDTH/2)-(del_crew_button.get_width()/2)), (HEIGHT/2+60), (del_crew_button.get_width()), (del_crew_button.get_height()))
version_hitbox = pygame.Rect(((WIDTH/2)-(build_version.get_width()/2)), (HEIGHT-30), (build_version.get_width()), (build_version.get_height()))

# build_sheet sprites
am_hitbox = pygame.Rect((0, 0, (WIDTH/2), HEIGHT))
pm_hitbox = pygame.Rect(((WIDTH/2), 0, (WIDTH/2), HEIGHT))
joyce_hitbox = pygame.Rect(((75)-(joyce_button.get_width()/2)), (HEIGHT/2), (joyce_button.get_width()), (joyce_button.get_height()))
aidee_hitbox = pygame.Rect(((WIDTH*.25+75)-(aidee_button.get_width()/2)), (HEIGHT/2), (aidee_button.get_width()), (aidee_button.get_height()))
isiah_hitbox = pygame.Rect(((WIDTH*.5+75)-(isiah_button.get_width()/2)), (HEIGHT/2), (isiah_button.get_width()), (isiah_button.get_height()))
ismael_hitbox = pygame.Rect(((WIDTH*.75+75)-(ismael_button.get_width()/2)), (HEIGHT/2), (ismael_button.get_width()), (ismael_button.get_height()))
continue_hitbox = pygame.Rect(((WIDTH/2)-(continue_button.get_width()/2)), (HEIGHT-50), (continue_button.get_width()), (continue_button.get_height()))

# generate_schedule sprites
exit_hitbox = pygame.Rect(((WIDTH/2)-(exit_button.get_width()/2)), (HEIGHT-30), (exit_button.get_width()), (exit_button.get_height()))
reshuffle_hitbox = pygame.Rect(0,0,50,50)

# for add_crew sprites go to add_crew()
save_hitbox = pygame.Rect(((WIDTH/2)-(save_button.get_width()/2)), (HEIGHT-50), (save_button.get_width()), (save_button.get_height()))

def add_crew():

    bha0, bha1, bha2, bha3, bha4, bha5 = 0, 0, 0, 0, 0, 0
    dha0, dha1, dha2, dha3, dha4, dha5 = 0, 0, 0, 0, 0, 0
    cha0, cha1, cha2, cha3, cha4, cha5 = 0, 0, 0, 0, 0, 0
    eha0, eha1, eha2, eha3, eha4, eha5 = 0, 0, 0, 0, 0, 0
    baha0, baha1, baha2, baha3, baha4, baha5 = 0, 0, 0, 0, 0, 0
    biha0, biha1, biha2, biha3, biha4, biha5 = 0, 0, 0, 0, 0, 0
    tha0, tha1, tha2, tha3, tha4, tha5 = 0, 0, 0, 0, 0, 0

    criteria_not_met = True
    while criteria_not_met:

        WIN.fill((200, 255, 200))

        width_dif = 35
        default_width = ((WIDTH/2)-(width_dif))
        width = default_width
        height = 135
        height_dif = 50
        sign_spacing = 350

        # boards hitbox
        bh0 = pygame.Rect(width+width_dif*1, height, bb0.get_width(), bb0.get_height())
        bh1 = pygame.Rect(width+width_dif*2, height, bb1.get_width(), bb1.get_height())
        bh2 = pygame.Rect(width+width_dif*3, height, bb2.get_width(), bb2.get_height())
        bh3 = pygame.Rect(width+width_dif*4, height, bb3.get_width(), bb3.get_height())
        bh4 = pygame.Rect(width+width_dif*5, height, bb4.get_width(), bb4.get_height())
        bh5 = pygame.Rect(width+width_dif*6, height, bb5.get_width(), bb5.get_height())
        
        # dining hitbox
        dh0 = pygame.Rect(width+width_dif*1, height+height_dif, db0.get_width(), db0.get_height())
        dh1 = pygame.Rect(width+width_dif*2, height+height_dif, db1.get_width(), db1.get_height())
        dh2 = pygame.Rect(width+width_dif*3, height+height_dif, db2.get_width(), db2.get_height())
        dh3 = pygame.Rect(width+width_dif*4, height+height_dif, db3.get_width(), db3.get_height())
        dh4 = pygame.Rect(width+width_dif*5, height+height_dif, db4.get_width(), db4.get_height())
        dh5 = pygame.Rect(width+width_dif*6, height+height_dif, db5.get_width(), db5.get_height())

        # cashier hitbox
        ch0 = pygame.Rect(width+width_dif*1, height+height_dif*2, cb0.get_width(), cb0.get_height())
        ch1 = pygame.Rect(width+width_dif*2, height+height_dif*2, cb1.get_width(), cb1.get_height())
        ch2 = pygame.Rect(width+width_dif*3, height+height_dif*2, cb2.get_width(), cb2.get_height())
        ch3 = pygame.Rect(width+width_dif*4, height+height_dif*2, cb3.get_width(), cb3.get_height())
        ch4 = pygame.Rect(width+width_dif*5, height+height_dif*2, cb4.get_width(), cb4.get_height())
        ch5 = pygame.Rect(width+width_dif*6, height+height_dif*2, cb5.get_width(), cb5.get_height())

        # expo hitbox
        eh0 = pygame.Rect(width+width_dif*1, height+height_dif*3, eb0.get_width(), eb0.get_height())
        eh1 = pygame.Rect(width+width_dif*2, height+height_dif*3, eb1.get_width(), eb1.get_height())
        eh2 = pygame.Rect(width+width_dif*3, height+height_dif*3, eb2.get_width(), eb2.get_height())
        eh3 = pygame.Rect(width+width_dif*4, height+height_dif*3, eb3.get_width(), eb3.get_height())
        eh4 = pygame.Rect(width+width_dif*5, height+height_dif*3, eb4.get_width(), eb4.get_height())
        eh5 = pygame.Rect(width+width_dif*6, height+height_dif*3, eb5.get_width(), eb5.get_height())

        # baskets hitbox
        bah0 = pygame.Rect(width+width_dif*1, height+height_dif*4, bab0.get_width(), bab0.get_height())
        bah1 = pygame.Rect(width+width_dif*2, height+height_dif*4, bab1.get_width(), bab1.get_height())
        bah2 = pygame.Rect(width+width_dif*3, height+height_dif*4, bab2.get_width(), bab2.get_height())
        bah3 = pygame.Rect(width+width_dif*4, height+height_dif*4, bab3.get_width(), bab3.get_height())
        bah4 = pygame.Rect(width+width_dif*5, height+height_dif*4, bab4.get_width(), bab4.get_height())
        bah5 = pygame.Rect(width+width_dif*6, height+height_dif*4, bab5.get_width(), bab5.get_height())

        # bird hitbox
        bih0 = pygame.Rect(width+width_dif*1, height+height_dif*5, bib0.get_width(), bib0.get_height())
        bih1 = pygame.Rect(width+width_dif*2, height+height_dif*5, bib1.get_width(), bib1.get_height())
        bih2 = pygame.Rect(width+width_dif*3, height+height_dif*5, bib2.get_width(), bib2.get_height())
        bih3 = pygame.Rect(width+width_dif*4, height+height_dif*5, bib3.get_width(), bib3.get_height())
        bih4 = pygame.Rect(width+width_dif*5, height+height_dif*5, bib4.get_width(), bib4.get_height())
        bih5 = pygame.Rect(width+width_dif*6, height+height_dif*5, bib5.get_width(), bib5.get_height())

        # toast hitbox
        th0 = pygame.Rect(width+width_dif*1, height+height_dif*6, tb0.get_width(), tb0.get_height())
        th1 = pygame.Rect(width+width_dif*2, height+height_dif*6, tb1.get_width(), tb1.get_height())
        th2 = pygame.Rect(width+width_dif*3, height+height_dif*6, tb2.get_width(), tb2.get_height())
        th3 = pygame.Rect(width+width_dif*4, height+height_dif*6, tb3.get_width(), tb3.get_height())
        th4 = pygame.Rect(width+width_dif*5, height+height_dif*6, tb4.get_width(), tb4.get_height())
        th5 = pygame.Rect(width+width_dif*6, height+height_dif*6, tb5.get_width(), tb5.get_height())

    
        if bh0.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bh0)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                bha0 += 1
                bha1,bha2,bha3,bha4,bha5 = 0,0,0,0,0
        if bh1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bh1)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                bha1 += 1
                bha0,bha2,bha3,bha4,bha5 = 0,0,0,0,0
        if bh2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bh2)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                bha2 += 1
                bha0,bha1,bha3,bha4,bha5 = 0,0,0,0,0
        if bh3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bh3)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                bha3 += 1
                bha0,bha1,bha2,bha4,bha5 = 0,0,0,0,0
        if bh4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bh4)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                bha4 += 1
                bha0,bha1,bha2,bha3,bha5 = 0,0,0,0,0
        if bh5.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bh5)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                bha5 += 1
                bha0,bha1,bha2,bha3,bha4 = 0,0,0,0,0
        if bha0 % 2:
            bht0 = True
            pygame.draw.rect(WIN, DARK_RED, bh0)
        else: bht0 = False
        if bha1 % 2:
            bht1 = True
            pygame.draw.rect(WIN, RED, bh1)
        else: bht1 = False
        if bha2 % 2:
            bht2 = True
            pygame.draw.rect(WIN, ORANGE, bh2)
        else: bht2 = False
        if bha3 % 2:
            bht3 = True
            pygame.draw.rect(WIN, YELLOW, bh3)
        else: bht3 = False
        if bha4 % 2:
            bht4 = True
            pygame.draw.rect(WIN, GREEN, bh4)
        else: bht4 = False
        if bha5 % 2:
            bht5 = True
            pygame.draw.rect(WIN, DARK_GREEN, bh5)
        else: bht5 = False

        
        if dh0.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, dh0)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                dha0 += 1
                dha1,dha2,dha3,dha4,dha5 = 0,0,0,0,0
        if dh1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, dh1)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                dha1 += 1
                dha0,dha2,dha3,dha4,dha5 = 0,0,0,0,0
        if dh2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, dh2)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                dha2 += 1
                dha0,dha1,dha3,dha4,dha5 = 0,0,0,0,0
        if dh3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, dh3)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                dha3 += 1
                dha0,dha1,dha2,dha4,dha5 = 0,0,0,0,0
        if dh4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, dh4)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                dha4 += 1
                dha0,dha1,dha2,dha3,dha5 = 0,0,0,0,0
        if dh5.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, dh5)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                dha5 += 1
                dha0,dha1,dha2,dha3,dha4 = 0,0,0,0,0
        if dha0 % 2:
            dht0 = True
            pygame.draw.rect(WIN, DARK_RED, dh0)
        else: dht0 = False
        if dha1 % 2:
            dht1 = True
            pygame.draw.rect(WIN, RED, dh1)
        else: dht1 = False
        if dha2 % 2:
            dht2 = True
            pygame.draw.rect(WIN, ORANGE, dh2)
        else: dht2 = False
        if dha3 % 2:
            dht3 = True
            pygame.draw.rect(WIN, YELLOW, dh3)
        else: dht3 = False
        if dha4 % 2:
            dht4 = True
            pygame.draw.rect(WIN, GREEN, dh4)
        else: dht4 = False
        if dha5 % 2:
            dht5 = True
            pygame.draw.rect(WIN, DARK_GREEN, dh5)
        else: dht5 = False


        if ch0.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, ch0)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                cha0 += 1
                cha1,cha2,cha3,cha4,cha5 = 0,0,0,0,0
        if ch1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, ch1)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                cha1 += 1
                cha0,cha2,cha3,cha4,cha5 = 0,0,0,0,0
        if ch2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, ch2)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                cha2 += 1
                cha0,cha1,cha3,cha4,cha5 = 0,0,0,0,0
        if ch3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, ch3)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                cha3 += 1
                cha0,cha1,cha2,cha4,cha5 = 0,0,0,0,0
        if ch4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, ch4)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                cha4 += 1
                cha0,cha1,cha2,cha3,cha5 = 0,0,0,0,0
        if ch5.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, ch5)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                cha5 += 1
                cha0,cha1,cha2,cha3,cha4 = 0,0,0,0,0
        if cha0 % 2:
            cht0 = True
            pygame.draw.rect(WIN, DARK_RED, ch0)
        else: cht0 = False
        if cha1 % 2:
            cht1 = True
            pygame.draw.rect(WIN, RED, ch1)
        else: cht1 = False
        if cha2 % 2:
            cht2 = True
            pygame.draw.rect(WIN, ORANGE, ch2)
        else: cht2 = False
        if cha3 % 2:
            cht3 = True
            pygame.draw.rect(WIN, YELLOW, ch3)
        else: cht3 = False
        if cha4 % 2:
            cht4 = True
            pygame.draw.rect(WIN, GREEN, ch4)
        else: cht4 = False
        if cha5 % 2:
            cht5 = True
            pygame.draw.rect(WIN, DARK_GREEN, ch5)
        else: cht5 = False


        if eh0.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, eh0)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                eha0 += 1
                eha1,eha2,eha3,eha4,eha5 = 0,0,0,0,0
        if eh1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, eh1)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                eha1 += 1
                eha0,eha2,eha3,eha4,eha5 = 0,0,0,0,0
        if eh2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, eh2)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                eha2 += 1
                eha0,eha1,eha3,eha4,eha5 = 0,0,0,0,0
        if eh3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, eh3)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                eha3 += 1
                eha0,eha1,eha2,eha4,eha5 = 0,0,0,0,0
        if eh4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, eh4)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                eha4 += 1
                eha0,eha1,eha2,eha3,eha5 = 0,0,0,0,0
        if eh5.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, eh5)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                eha5 += 1
                eha0,eha1,eha2,eha3,eha4 = 0,0,0,0,0
        if eha0 % 2:
            eht0 = True
            pygame.draw.rect(WIN, DARK_RED, eh0)
        else: eht0 = False
        if eha1 % 2:
            eht1 = True
            pygame.draw.rect(WIN, RED, eh1)
        else: eht1 = False
        if eha2 % 2:
            eht2 = True
            pygame.draw.rect(WIN, ORANGE, eh2)
        else: eht2 = False
        if eha3 % 2:
            eht3 = True
            pygame.draw.rect(WIN, YELLOW, eh3)
        else: eht3 = False
        if eha4 % 2:
            eht4 = True
            pygame.draw.rect(WIN, GREEN, eh4)
        else: eht4 = False
        if eha5 % 2:
            eht5 = True
            pygame.draw.rect(WIN, DARK_GREEN, eh5)
        else: eht5 = False


        if bah0.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bah0)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                baha0 += 1
                baha1,baha2,baha3,baha4,baha5 = 0,0,0,0,0
        if bah1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bah1)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                baha1 += 1
                baha0,baha2,baha3,baha4,baha5 = 0,0,0,0,0
        if bah2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bah2)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                baha2 += 1
                baha0,baha1,baha3,baha4,baha5 = 0,0,0,0,0
        if bah3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bah3)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                baha3 += 1
                baha0,baha1,baha2,baha4,baha5 = 0,0,0,0,0
        if bah4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bah4)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                baha4 += 1
                baha0,baha1,baha2,baha3,baha5 = 0,0,0,0,0
        if bah5.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bah5)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                baha5 += 1
                baha0,baha1,baha2,baha3,baha4 = 0,0,0,0,0
        if baha0 % 2:
            baht0 = True
            pygame.draw.rect(WIN, DARK_RED, bah0)
        else: baht0 = False
        if baha1 % 2:
            baht1 = True
            pygame.draw.rect(WIN, RED, bah1)
        else: baht1 = False
        if baha2 % 2:
            baht2 = True
            pygame.draw.rect(WIN, ORANGE, bah2)
        else: baht2 = False
        if baha3 % 2:
            baht3 = True
            pygame.draw.rect(WIN, YELLOW, bah3)
        else: baht3 = False
        if baha4 % 2:
            baht4 = True
            pygame.draw.rect(WIN, GREEN, bah4)
        else: baht4 = False
        if baha5 % 2:
            baht5 = True
            pygame.draw.rect(WIN, DARK_GREEN, bah5)
        else: baht5 = False


        if bih0.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bih0)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                biha0 += 1
                biha1,biha2,biha3,biha4,biha5 = 0,0,0,0,0
        if bih1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bih1)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                biha1 += 1
                biha0,biha2,biha3,biha4,biha5 = 0,0,0,0,0
        if bih2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bih2)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                biha2 += 1
                biha0,biha1,biha3,biha4,biha5 = 0,0,0,0,0
        if bih3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bih3)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                biha3 += 1
                biha0,biha1,biha2,biha4,biha5 = 0,0,0,0,0
        if bih4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bih4)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                biha4 += 1
                biha0,biha1,biha2,biha3,biha5 = 0,0,0,0,0
        if bih5.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, bih5)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                biha5 += 1
                biha0,biha1,biha2,biha3,biha4 = 0,0,0,0,0
        if biha0 % 2:
            biht0 = True
            pygame.draw.rect(WIN, DARK_RED, bih0)
        else: biht0 = False
        if biha1 % 2:
            biht1 = True
            pygame.draw.rect(WIN, RED, bih1)
        else: biht1 = False
        if biha2 % 2:
            biht2 = True
            pygame.draw.rect(WIN, ORANGE, bih2)
        else: biht2 = False
        if biha3 % 2:
            biht3 = True
            pygame.draw.rect(WIN, YELLOW, bih3)
        else: biht3 = False
        if biha4 % 2:
            biht4 = True
            pygame.draw.rect(WIN, GREEN, bih4)
        else: biht4 = False
        if biha5 % 2:
            biht5 = True
            pygame.draw.rect(WIN, DARK_GREEN, bih5)
        else: biht5 = False


        if th0.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, th0)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                tha0 += 1
                tha1,tha2,tha3,tha4,tha5 = 0,0,0,0,0
        if th1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, th1)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                tha1 += 1
                tha0,tha2,tha3,tha4,tha5 = 0,0,0,0,0
        if th2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, th2)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                tha2 += 1
                tha0,tha1,tha3,tha4,tha5 = 0,0,0,0,0
        if th3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, th3)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                tha3 += 1
                tha0,tha1,tha2,tha4,tha5 = 0,0,0,0,0
        if th4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, th4)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                tha4 += 1
                tha0,tha1,tha2,tha3,tha5 = 0,0,0,0,0
        if th5.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, th5)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                tha5 += 1
                tha0,tha1,tha2,tha3,tha4 = 0,0,0,0,0
        if tha0 % 2:
            tht0 = True
            pygame.draw.rect(WIN, DARK_RED, th0)
        else: tht0 = False
        if tha1 % 2:
            tht1 = True
            pygame.draw.rect(WIN, RED, th1)
        else: tht1 = False
        if tha2 % 2:
            tht2 = True
            pygame.draw.rect(WIN, ORANGE, th2)
        else: tht2 = False
        if tha3 % 2:
            tht3 = True
            pygame.draw.rect(WIN, YELLOW, th3)
        else: tht3 = False
        if tha4 % 2:
            tht4 = True
            pygame.draw.rect(WIN, GREEN, th4)
        else: tht4 = False
        if tha5 % 2:
            tht5 = True
            pygame.draw.rect(WIN, DARK_GREEN, th5)
        else: tht5 = False

        global user_text

        type_hitbox = pygame.Rect((sign_spacing+125), ((height)+(height_dif*-1)), (bb0.get_width()*20), (bb0.get_height()))
        pygame.draw.rect(WIN, GRAY, type_hitbox)
        WIN.blit(name_button, ((width-width_dif*4),(height-height_dif)))
        if type_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, LIGHT_GRAY, type_hitbox)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else: user_text += event.unicode
        user_input_button = ratings_font.render(user_text, True, BLACK)
        WIN.blit(user_input_button, ((sign_spacing+125), (height)+(height_dif*-1)))
        

        for x in bb_list:
            width += width_dif
            WIN.blit(x, (width, height))
        WIN.blit(boards, ((width-sign_spacing),(height)))

        width = default_width
        height += height_dif
        for x in db_list:
            width += width_dif
            WIN.blit(x, (width, height))
        WIN.blit(dining, ((width-sign_spacing),(height)))

        width = default_width
        height += height_dif
        for x in cb_list:
            width += width_dif
            WIN.blit(x, (width, height))
        WIN.blit(cashier, ((width-sign_spacing),(height)))

        width = default_width
        height += height_dif
        for x in eb_list:
            width += width_dif
            WIN.blit(x, (width, height))
        WIN.blit(expo, ((width-sign_spacing),(height)))

        width = default_width
        height += height_dif
        for x in bab_list:
            width += width_dif
            WIN.blit(x, (width, height))
        WIN.blit(baskets, ((width-sign_spacing),(height)))

        width = default_width
        height += height_dif
        for x in bib_list:
            width += width_dif
            WIN.blit(x, (width, height))
        WIN.blit(bird, ((width-sign_spacing),(height)))

        width = default_width
        height += height_dif
        for x in tb_list:
            width += width_dif
            WIN.blit(x, (width, height))
        WIN.blit(toast, ((width-sign_spacing),(height)))

        
        if save_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GREEN, save_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                bht_list = [bht0, bht1, bht2, bht3, bht4, bht5]
                dht_list = [dht0, dht1, dht2, dht3, dht4, dht5]
                cht_list = [cht0, cht1, cht2, cht3, cht4, cht5]
                eht_list = [eht0, eht1, eht2, eht3, eht4, eht5]
                baht_list = [baht0, baht1, baht2, baht3, baht4, baht5]
                biht_list = [biht0, biht1, biht2, biht3, biht4, biht5]
                tht_list = [tht0, tht1, tht2, tht3, tht4, tht5]
                
                
                valitity_score = 0
                
                for x in bht_list:
                    if x:
                        boards_Score = bht_list.index(x)
                        valitity_score += 1
                    else: valitity_score -=1
                for x in dht_list:
                    if x:
                        dining_Score = dht_list.index(x)
                        valitity_score +=1
                    else: valitity_score -= 1
                for x in cht_list:
                    if x:
                        cashier_Score = cht_list.index(x)
                        valitity_score += 1
                    else: valitity_score -= 1
                for x in eht_list:
                    if x:
                        expo_Score = eht_list.index(x)
                        valitity_score += 1
                    else: valitity_score -=1
                for x in baht_list:
                    if x:
                        baskets_Score = baht_list.index(x)
                        valitity_score += 1
                    else: valitity_score -= 1
                for x in biht_list:
                    if x:
                        bird_Score = biht_list.index(x)
                        valitity_score +=1
                    else: valitity_score -= 1
                for x in tht_list:
                    if x:
                        toast_Score = tht_list.index(x)
                        valitity_score += 1
                    else: valitity_score -= 1

                if valitity_score == -28 and len(user_text) > 0:
                    employee_list.append([user_text.capitalize(), boards_Score, dining_Score, cashier_Score, expo_Score, baskets_Score, bird_Score, toast_Score])
                    print(employee_list)
                    main_menu()
                else: print('[asa]: Missing Critical Information!')

                
        WIN.blit(save_button, (((WIDTH/2)-(save_button.get_width()/2)),(HEIGHT-50)))

        


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu()
            
        pygame.display.update()


def build_sheet():

    requirement_am_pm = True
    tick_delay = 0

    while requirement_am_pm:
        
        tick_delay += 1
        
        global am_pm
        clock.tick(FPS)
        WIN.fill(DARK_BLUE)
        pygame.draw.rect(WIN, YELLOW, ((WIDTH/2), 0, (WIDTH/2), HEIGHT))

        if am_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, BLACK, am_hitbox)
            if pygame.mouse.get_pressed()[0]:
                am_pm = 'AM'
                requirement_am_pm = False
        WIN.blit(am_button, (((WIDTH/4)-(am_button.get_width()/2)),((HEIGHT/2)-(am_button.get_height()/2))))
        
        if pm_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, BLACK, pm_hitbox)
            if pygame.mouse.get_pressed()[0]:
                am_pm = 'PM'
                requirement_am_pm = False
        WIN.blit(pm_button, (((WIDTH*.75)-(pm_button.get_width()/2)),((HEIGHT/2)-(pm_button.get_height()/2))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()
    
    build_sheet2()
    


def build_sheet2():
    
    requirement_mod = True
    tick_delay = 0
    tick_delay1 = -120
    
    joyce_score = 0
    aidee_score = 0
    isiah_score = 0
    ismael_score = 0

    while requirement_mod:
    
        tick_delay += 1
        tick_delay1 += 1
        WIN.fill(WHITE)
        clock.tick(FPS)

        pygame.draw.rect(WIN, BLACK, (((WIDTH/2)-(continue_button.get_width())), (HEIGHT-70), (continue_button.get_width()*2), HEIGHT))
        pygame.draw.rect(WIN, BLUE, (200, tick_delay-50, 100, tick_delay*2))
        pygame.draw.rect(WIN, (85, 200, 255), (tick_delay1, tick_delay1*.5, 300, 200))
        pygame.draw.rect(WIN, (100, 100, 255), (tick_delay, 150, 300, 200))
        if tick_delay > 1200:
            tick_delay = 0
            tick_delay1 = -120


        if joyce_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, joyce_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                joyce_score += 1
        WIN.blit(joyce_button, (((75)-(joyce_button.get_width()/2)),(HEIGHT/2)))

        if aidee_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, aidee_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                aidee_score += 1
        WIN.blit(aidee_button, (((WIDTH*.25+75)-(aidee_button.get_width()/2)),(HEIGHT/2)))

        if isiah_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, isiah_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                isiah_score += 1
        WIN.blit(isiah_button, (((WIDTH*.5+75)-(isiah_button.get_width()/2)),(HEIGHT/2)))

        if ismael_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, ismael_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                ismael_score += 1
        WIN.blit(ismael_button, (((WIDTH*.75+75)-(ismael_button.get_width()/2)),(HEIGHT/2)))

        if joyce_score % 2 == 1:
            pygame.draw.rect(WIN, ORANGE, joyce_hitbox)
            WIN.blit(joyce_button, (((75)-(joyce_button.get_width()/2)),(HEIGHT/2)))
            joyce_on_shift = 'Joyce'
        else: joyce_on_shift = ''

        if aidee_score % 2 == 1:
            pygame.draw.rect(WIN, RED, aidee_hitbox)
            WIN.blit(aidee_button, (((WIDTH*.25+75)-(aidee_button.get_width()/2)),(HEIGHT/2)))
            aidee_on_shift = 'Aidee'
        else: aidee_on_shift = ''

        if isiah_score % 2 == 1:
            pygame.draw.rect(WIN, GREEN, isiah_hitbox)
            WIN.blit(isiah_button, (((WIDTH*.5+75)-(isiah_button.get_width()/2)),(HEIGHT/2)))
            isiah_on_shift = 'Isiah'
        else: isiah_on_shift = ''

        if ismael_score % 2 == 1:
            pygame.draw.rect(WIN, HOT_PINK, ismael_hitbox)
            WIN.blit(ismael_button, (((WIDTH*.75+75)-(ismael_button.get_width()/2)),(HEIGHT/2)))
            ismael_on_shift = 'Ismael'
        else: ismael_on_shift = ''

        if continue_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, (150,250,150), continue_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                global mods
                mods = base_font.render(f"{joyce_on_shift} {aidee_on_shift} {isiah_on_shift} {ismael_on_shift}", False, BLACK)
                build_sheet3()
        WIN.blit(continue_button, (((WIDTH/2)-(continue_button.get_width()/2)),(HEIGHT-50)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        WIN.blit(big_font.render('Select MODs', False, BLACK),((75)-(joyce_button.get_width()/2),(HEIGHT/2-100)))
        pygame.display.update()

def build_sheet3():
    
    tick_delay = 0
    employees_on_shift = []
    num = len(employee_list)
    select_sign = big_font.render('Select Crew Members', False, BLACK)

    t = []
    for x in range(num):
        t.append(0)
    
    truth = True
    while truth:
        tick_delay += 1
        clock.tick(FPS)
        
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, (50,50,50), (((WIDTH/2)-(continue_button.get_width())), (HEIGHT-70), (continue_button.get_width()*2), HEIGHT))
        pygame.draw.rect(WIN, (0,210,0), (200, tick_delay-50, 100, tick_delay*2))
        pygame.draw.rect(WIN, (100, 255, 180), (tick_delay, 150, 300, 200))
        if tick_delay > 1200:
            tick_delay = 0
        
        WIN.blit(select_sign, (WIDTH/2-select_sign.get_width()/2, 130))

        width, height = (WIDTH/2-select_sign.get_width()/2), 200
        buttons_per_row = 4
        per_row = buttons_per_row
       
        
        for x in range(num):
            height += 20
            y = pygame.draw.rect(WIN, RED, (width, height, 200, 20))
            if y.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(WIN, GRAY, (width, height, 200, 20))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(WIN, GRAY, (width, height, 200, 20))
                    pygame.time.delay(250)
                    t[x] += 1 
                    if t[x] == 2: t[x] = 0
            if t[x] % 2:
                pygame.draw.rect(WIN, GREEN, (width, height, 200, 20))
            text = ratings_font.render(employee_list[x][0], True, BLACK)
            WIN.blit(text, ((width+2), (height)))
            if per_row == x+1:
                width += 200
                height = 200
                per_row += buttons_per_row
        

        if continue_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, LIGHT_GRAY, continue_hitbox)
            if pygame.mouse.get_pressed()[0]:
                for i in range(num):
                    if t[i] == 1: employees_on_shift.append(employee_list[i])
                truth = False
        WIN.blit(continue_button, (((WIDTH/2)-(continue_button.get_width()/2)),(HEIGHT-50)))
        
        pygame.display.update()
    
        for event in pygame.event.get():        
                if event.type == pygame.QUIT:
                    pygame.quit()

    
    print(f"[asa]: Employees On Shift: {employees_on_shift}")

    generate_schedule(employees_on_shift)

def remove_crew():
    tick_delay = 0
    num = len(employee_list)
    remove_sign = base_font.render('Select 1 Crew Member At A Time Please:', False, BLACK)


    t = []
    for x in range(num):
        t.append(0)
    
    truth = True
    while truth:
        
        tick_delay += 1
            


        WIN.fill(LIGHT_RED)
        WIN.blit(remove_sign, ((WIDTH/2-remove_sign.get_width()/2), 50))

        width, height = (WIDTH/2-100), 100
        buttons_per_row = 15
        per_row = buttons_per_row
       
        
        for x in range(num):
            height += 20
            y = pygame.draw.rect(WIN, RED, (width, height, 200, 20))
            if y.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(WIN, GRAY, (width, height, 200, 20))
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.rect(WIN, GRAY, (width, height, 200, 20))
                    pygame.time.delay(250)
                    t[x] += 1 
                    if t[x] == 2: t[x] = 0
            if t[x] % 2:
                pygame.draw.rect(WIN, GREEN, (width, height, 200, 20))
            text = ratings_font.render(employee_list[x][0], True, BLACK)
            WIN.blit(text, ((width+2), (height)))
            if per_row == x+1:
                width += 200
                height = 100
                per_row += buttons_per_row
        

        if save_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, LIGHT_GRAY, save_hitbox)
            if pygame.mouse.get_pressed()[0]:
                for i in range(num):
                    if t[i] == 1: 
                        print (f'[asa]: {employee_list[i]} successfully removed.')
                        employee_list.remove(employee_list[i])
                        num = len(employee_list)
                truth = False
        WIN.blit(save_button, (((WIDTH/2)-(save_button.get_width()/2)),(HEIGHT-50)))

        pygame.display.update()
    
        for event in pygame.event.get():        
                if event.type == pygame.QUIT:
                    pygame.quit()
    
    main_menu()

def generate_schedule(crew):
    
    tick_delay = 0
    sort_algorithm = True
    reshuffle = 0
    pos_verified = 0
    pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11 = [['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]],[['',5,5,5,5,5,5,5]]
    crew_len = len(crew)
    crew2 = crew.copy()
    generate = True
    while generate:
        
        WIN.blit(schedule, (0, 0))
        tick_delay += 1
        
        am_pm_render = base_font.render(am_pm, False, BLACK)
        WIN.blit(am_pm_render, (360, 63))
        WIN.blit(mods, (530, 65))
        
        if exit_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 50:
            pygame.draw.rect(WIN, GRAY, exit_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(100)
                generate = False
        WIN.blit(exit_button, (((WIDTH/2)-(exit_button.get_width()/2)),(HEIGHT-30)))

        while sort_algorithm:
            random.shuffle(crew)
            print(crew)
            if len(crew) > 0:
                for x in range(crew_len):
                    if crew[x][3] == 0: pos1.append(crew[x])
                for x in range(crew_len):
                    if crew[x][3] == 1: pos1.append(crew[x])
                for x in range(crew_len):
                    if crew[x][3] == 2: pos1.append(crew[x])
                for x in range(crew_len):
                    if crew[x][3] == 3: pos1.append(crew[x])
                for x in range(crew_len):
                    if crew[x][3] == 4: pos1.append(crew[x])
                for x in range(crew_len):
                    if crew[x][3] == 5: pos1.append(crew[x])
                crew.remove(pos1[-1])

            if len(crew) > 0:
                for x in range(crew_len-1):
                    if crew[x][6] == 0: pos2.append(crew[x])
                for x in range(crew_len-1):
                    if crew[x][6] == 1: pos2.append(crew[x])
                for x in range(crew_len-1):
                    if crew[x][6] == 2: pos2.append(crew[x])
                for x in range(crew_len-1):
                    if crew[x][6] == 3: pos2.append(crew[x])
                for x in range(crew_len-1):
                    if crew[x][6] == 4: pos2.append(crew[x])
                for x in range(crew_len-1):
                    if crew[x][6] == 5: pos2.append(crew[x])
                crew.remove(pos2[-1])

            if len(crew) > 0:
                for x in range(crew_len-2):
                    if crew[x][1] == 0: pos3.append(crew[x])
                for x in range(crew_len-2):
                    if crew[x][1] == 1: pos3.append(crew[x])
                for x in range(crew_len-2):
                    if crew[x][1] == 2: pos3.append(crew[x])
                for x in range(crew_len-2):
                    if crew[x][1] == 3: pos3.append(crew[x])
                for x in range(crew_len-2):
                    if crew[x][1] == 4: pos3.append(crew[x])
                for x in range(crew_len-2):
                    if crew[x][1] == 5: pos3.append(crew[x])
                crew.remove(pos3[-1])

            if len(crew) > 0:
                for x in range(crew_len-3):
                    if crew[x][3] == 0: pos4.append(crew[x])
                for x in range(crew_len-3):
                    if crew[x][3] == 1: pos4.append(crew[x])
                for x in range(crew_len-3):
                    if crew[x][3] == 2: pos4.append(crew[x])
                for x in range(crew_len-3):
                    if crew[x][3] == 3: pos4.append(crew[x])
                for x in range(crew_len-3):
                    if crew[x][3] == 4: pos4.append(crew[x])
                for x in range(crew_len-3):
                    if crew[x][3] == 5: pos4.append(crew[x])
                crew.remove(pos4[-1])

            if len(crew) > 0:
                for x in range(crew_len-4):
                    if crew[x][7] == 0: pos5.append(crew[x])
                for x in range(crew_len-4):
                    if crew[x][7] == 1: pos5.append(crew[x])
                for x in range(crew_len-4):
                    if crew[x][7] == 2: pos5.append(crew[x])
                for x in range(crew_len-4):
                    if crew[x][7] == 3: pos5.append(crew[x])
                for x in range(crew_len-4):
                    if crew[x][7] == 4: pos5.append(crew[x])
                for x in range(crew_len-4):
                    if crew[x][7] == 5: pos5.append(crew[x])
                crew.remove(pos5[-1])

            if len(crew) > 0:
                for x in range(crew_len-5):
                    if crew[x][2] == 0: pos6.append(crew[x])
                for x in range(crew_len-5):
                    if crew[x][2] == 1: pos6.append(crew[x])
                for x in range(crew_len-5):
                    if crew[x][2] == 2: pos6.append(crew[x])
                for x in range(crew_len-5):
                    if crew[x][2] == 3: pos6.append(crew[x])
                for x in range(crew_len-5):
                    if crew[x][2] == 4: pos6.append(crew[x])
                for x in range(crew_len-5):
                    if crew[x][2] == 5: pos6.append(crew[x])
                crew.remove(pos6[-1])

            if len(crew) > 0:
                for x in range(crew_len-6):
                    if crew[x][1] == 0: pos7.append(crew[x])
                for x in range(crew_len-6):
                    if crew[x][1] == 1: pos7.append(crew[x])
                for x in range(crew_len-6):
                    if crew[x][1] == 2: pos7.append(crew[x])
                for x in range(crew_len-6):
                    if crew[x][1] == 3: pos7.append(crew[x])
                for x in range(crew_len-6):
                    if crew[x][1] == 4: pos7.append(crew[x])
                for x in range(crew_len-6):
                    if crew[x][1] == 5: pos7.append(crew[x])
                crew.remove(pos7[-1])

            if len(crew) > 0:
                for x in range(crew_len-7):
                    if crew[x][4] == 0: pos8.append(crew[x])
                for x in range(crew_len-7):
                    if crew[x][4] == 1: pos8.append(crew[x])
                for x in range(crew_len-7):
                    if crew[x][4] == 2: pos8.append(crew[x])
                for x in range(crew_len-7):
                    if crew[x][4] == 3: pos8.append(crew[x])
                for x in range(crew_len-7):
                    if crew[x][4] == 4: pos8.append(crew[x])
                for x in range(crew_len-7):
                    if crew[x][4] == 5: pos8.append(crew[x])
                crew.remove(pos8[-1])

            if len(crew) > 0:
                for x in range(crew_len-8):
                    if crew[x][5] == 0: pos9.append(crew[x])
                for x in range(crew_len-8):
                    if crew[x][5] == 1: pos9.append(crew[x])
                for x in range(crew_len-8):
                    if crew[x][5] == 2: pos9.append(crew[x])
                for x in range(crew_len-8):
                    if crew[x][5] == 3: pos9.append(crew[x])
                for x in range(crew_len-8):
                    if crew[x][5] == 4: pos9.append(crew[x])
                for x in range(crew_len-8):
                    if crew[x][5] == 5: pos9.append(crew[x])
                crew.remove(pos9[-1])

            # pos10 = floater
            if len(crew) > 0:
                pos10.append(random.choice(crew))
                crew.remove(pos10[-1])

            if len(crew) > 0:
                for x in range(crew_len-10):
                    if crew[x][2] == 0: pos11.append(crew[x])
                for x in range(crew_len-10):
                    if crew[x][2] == 1: pos11.append(crew[x])
                for x in range(crew_len-10):
                    if crew[x][2] == 2: pos11.append(crew[x])
                for x in range(crew_len-10):
                    if crew[x][2] == 3: pos11.append(crew[x])
                for x in range(crew_len-10):
                    if crew[x][2] == 4: pos11.append(crew[x])
                for x in range(crew_len-10):
                    if crew[x][2] == 5: pos11.append(crew[x])
                crew.remove(pos11[-1])
            
            pos_list = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11]
            r = 0
            for x in range(10):
                if r < 6:
                    r += 1
                if pos_list[x][-1][r] in range (2,6):
                    pos_verified += 1
                if pos_list[x][-1][r] == 0 or pos_list[x][-1][r] == 1 and reshuffle < 200:
                   reshuffle += 1
                if pos_verified == crew_len: sort_algorithm = False
                if reshuffle == 200:
                    print('[asa]: no assignments found')
                    sort_algorithm = False



        if reshuffle_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, reshuffle_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(500)
                sort_algorithm = True
                reshuffle = 0
                pos_verified = 0
                crew = crew2.copy()

        
        pos1_name = base_font.render(pos_list[0][-1][0], False, BLACK)
        pos2_name = base_font.render(pos_list[1][-1][0], False, BLACK)
        pos3_name = base_font.render(pos_list[2][-1][0], False, BLACK)
        pos4_name = base_font.render(pos_list[3][-1][0], False, BLACK)
        pos5_name = base_font.render(pos_list[4][-1][0], False, BLACK)
        pos6_name = base_font.render(pos_list[5][-1][0], False, BLACK)
        pos7_name = base_font.render(pos_list[6][-1][0], False, BLACK)
        pos8_name = base_font.render(pos_list[7][-1][0], False, BLACK)
        pos9_name = base_font.render(pos_list[8][-1][0], False, BLACK)
        pos10_name = base_font.render(pos_list[9][-1][0], False, BLACK)
        pos11_name = base_font.render(pos_list[10][-1][0], False, BLACK)
        WIN.blit(pos1_name, (235, 190))
        WIN.blit(pos2_name, (710, 180))
        WIN.blit(pos3_name, (710, 235))
        WIN.blit(pos4_name, (235, 250))
        WIN.blit(pos5_name, (710, 280))
        WIN.blit(pos6_name, (235, 315))
        WIN.blit(pos7_name, (710, 335))
        WIN.blit(pos8_name, (240, 380))
        WIN.blit(pos9_name, (710, 380))
        WIN.blit(pos10_name, (710, 435))
        WIN.blit(pos11_name, (235, 435))



        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

   
        pygame.display.update()
    
    print(f"cash {pos1[-1][0]}")
    print(f"bird {pos2[-1][0]}")
    print(f"boards {pos3[-1][0]}")
    print(f"cash 2 {pos4[-1][0]}")
    print(f"toast {pos5[-1][0]}")
    print(f"dining {pos6[-1][0]}")
    print(f"boards setup {pos7[-1][0]}")
    print(f"expo {pos8[-1][0]}")
    print(f"baskets {pos9[-1][0]}")
    print(f"floater {pos10[-1][0]}")
    print(f"dining 2 {pos11[-1][0]}")
        
    
    main_menu()

def main_menu():
    
    tick_delay = 0
    tick_delay1 = 0
    running = True
    while running:
        
        # basic main_menu config
       
        tick_delay += 1
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, DARK_RED, (tick_delay, tick_delay, tick_delay/2, tick_delay))
        pygame.draw.rect(WIN, (60, 0, 0), (800 -tick_delay, 800 -tick_delay, 800 -tick_delay, 800-tick_delay))
        pygame.draw.rect(WIN, (140, 0, 0), (tick_delay, 0, tick_delay, 300))
        pygame.draw.rect(WIN, DARK_RED, (0, tick_delay1, tick_delay1/2, tick_delay1))
        pygame.draw.rect(WIN, (60, 0, 0), (800 -tick_delay1, 800 +tick_delay1, tick_delay1*2, tick_delay1))
        pygame.draw.rect(WIN, (140, 0, 0), (tick_delay1, 0, tick_delay1, 300))
        if tick_delay > 1000:
            tick_delay = 0
        if tick_delay1 > 1300:
            tick_delay1 = 0 
        if tick_delay > 300:
            tick_delay1 += 1

        pygame.draw.rect(WIN, LIGHT_GRAY, ((WIDTH/2-170), 30, 340, 400),15)
        clock.tick(FPS)
        WIN.blit(logo, (((WIDTH/2)-(logo.get_width()/2)),(50)))

        # mouse hover / click detection

        if build_button_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, build_button_hitbox)
            if pygame.mouse.get_pressed()[0]:
                build_sheet()
        WIN.blit(build_schedule_button, (((WIDTH/2)-(build_schedule_button.get_width()/2)),(HEIGHT/2-30)))
        
        if add_crew_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, add_crew_hitbox)
            if pygame.mouse.get_pressed()[0] and tick_delay > 10:  
                pygame.time.delay(250)
                global user_text
                user_text = ''
                add_crew()
        WIN.blit(add_crew_button, (((WIDTH/2)-(add_crew_button.get_width()/2)),(HEIGHT/2+30)))

        if del_crew_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, del_crew_hitbox)
            if pygame.mouse.get_pressed()[0] and tick_delay > 10:
                pygame.time.delay(250)
                remove_crew()
        WIN.blit(del_crew_button, (((WIDTH/2)-(del_crew_button.get_width()/2)),(HEIGHT/2+60)))

        if version_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, version_hitbox)
            if pygame.mouse.get_pressed()[0] and tick_delay > 10:
                pygame.time.delay(250)
                print(f"[asa]: {github_url}")
        WIN.blit(build_version, (((WIDTH/2)-(build_version.get_width()/2)),(HEIGHT-30)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()