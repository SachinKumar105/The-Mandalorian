import time as t
from man import Man as m
from man import Boss as boss
from getch import input_to, Get
from board import Board as b
from beams import Beams,Hor_beams,Ver_beams,Cross_beams


a = b(30, 300,150)
game_time = 150
a.fill_coins()
a.fill_hor_beams()
a.fill_ver_beams()
a.fill_cross_beams()
a.fill_magnets()
man = m(5, 5)
boss = boss(0,0)
ii = 100
l = 0
gravity_count = 0
boost_count = 0
start_time = t.time()
while(t.time() - start_time < game_time):
    getch = Get()
    input = input_to(getch)
    if(input == "q"):
        exit()
    if(input == "b"):
        a.shoot(man,l)
    if(input == "h"):
        if(boost_count < 0):
            man.speed_boost()
            boost_count = 60
    if(input == " "):
        man.shield()
    if(input == "d"):
        if(boss.show_lives() == 0 and man.show_pos_y() > a.show_frm_width() - 10):
            boss.win(man)
        if(man.show_pos_y()+man.show_dim_y() < a.show_frm_width()):
            man.move_right(2)
    if(input == "a"):
        if(man.show_pos_y() > 1):
            man.move_left(2)
    if(input == "w"):
        if(man.show_pos_x() > 2):
            man.move_up(2)
        gravity_count = 0
    else:
        if(man.show_pos_x()+man.show_dim_x()+gravity_count < a.show_len()):
            man.move_down(gravity_count+1,30)
        else:
            # man.move_down(a.show_len() - man.show_dim_x() - man.show_pos_x(),30)
            man.set_pos_x(a.show_len() - man.show_dim_x())
        if(l%2==1):
            gravity_count = gravity_count + 1
        if(l + a.show_frm_width() +2 > a.show_len()):
            man.move_left(1)
    a.update_ice_balls(l)
    a.collision_check(man,100,l)
    a.update()
    a.magnet_effect(man,l)
    a.update_man(man, l)
    a.update_bullets(man,l)
    if(boss.show_lives() > 0):
        a.update_boss(boss,man,l)
        a.throw(boss,man,l)
    a.update_beams(l)
    a.show(man,boss,l,game_time - int(t.time() - start_time))
    if(l + a.show_frm_width() < a.show_brd()):
        l = l+1
    if(boost_count > 0):
        t.sleep(0.1)
    boost_count = boost_count - 1
    ii = ii + 1
    
man.lose()