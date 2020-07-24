import numpy as np
import time as t
from man import Man as m
from man import Boss as boss
from objects import Coins,Magnets,Bullets,Ice_balls
from beams import Beams,Hor_beams,Ver_beams,Cross_beams
from random import randint as r
from colorama import Fore, Back, Style 

class Board:
    def __init__(self, length, breadth,frame_width):
        self._length = length
        self._breadth = breadth
        self._frame_width = frame_width
        obj = np.empty((self._length, self._breadth), dtype='str')
        obj[:] = " "
        map = np.empty((self._length, self._breadth), dtype='str')
        map[:] = " "
        self._obj = obj
        self._map = map
        self._coins_pos = np.empty((int(self._breadth/20),2), dtype='int') 
        self._hor_beams_pos = np.empty((int(self._breadth/40),2), dtype='int') 
        self._ver_beams_pos = np.empty((int(self._breadth/40),2), dtype='int') 
        self._cross_beams_pos = np.empty((int(self._breadth/40),2), dtype='int') 
        self._magnets_pos = np.empty((int(self._breadth/100),2), dtype='int') 
        self._bullets_pos = []
        self._ice_balls_pos = []
        self._bullets = Bullets(0,0)
        self._coins = Coins(0,0)
        self._magnets = Magnets(0,0)
        self._ice_balls = Ice_balls(0,0)
        self._beams = Beams(0,0)
    def show_len(self):
        return self._length

    def show_brd(self):
        return self._breadth
    
    def show_frm_width(self):
        return self._frame_width

    def show(self, man,boss,l,ii):
        print('\033[0;0H', end="")
        for i in range(self._length):
            for j in range(self._frame_width):
                if(j+l < self._breadth):
                    x = self._obj[i][j+l]
                    print(self.show_colour(str(x)), end="")
                    print(Style.RESET_ALL,end="")
            print()
        for i in range(1):
            for j in range(self._frame_width):
                print(Back.GREEN + " ", end="")
        print(Style.RESET_ALL,end="")
        print()
        print("score : ",man.show_score()," lives : ",man.show_lives(),"     mode : ",man.show_mode() ,"    boss's lives : ",boss.show_lives(), "  time : ",ii,"        ")
        
            
    def update_object(self, obj):
        for i in range(obj.show_dim_x()):
            for j in range(obj.show_dim_y()):
                self._map[obj.show_pos_x()+i][obj.show_pos_y()+j] = obj.show_matrix(i,j)

    def update_beams(self,l):
        for t in self._hor_beams_pos:
            k = 0
            for j in range(7):
                if(self._obj[t[0]][t[1] + j] == self._bullets.show_matrix(1) or self._obj[t[0]][t[1] + j] == self._bullets.show_matrix(0)):
                    self.remove_bullet(t[0],t[1]+j,l)
                    k = 1
            if(k==1):
                for j in range(7):
                    self._map[t[0]][t[1] + j] = " "
                t[0] = 0
                t[1] = 0
        for t in self._ver_beams_pos:
            k = 0
            for i in range(7):
                if(self._obj[t[0] + i][t[1]] == self._bullets.show_matrix(1) or self._obj[t[0] + i][t[1]] == self._bullets.show_matrix(0)):
                    self.remove_bullet(t[0]+i,t[1],l)
                    k = 1
            if(k==1):
                for i in range(7):
                    self._map[t[0] + i][t[1]] = " "
                t[0] = 0
                t[1] = 0
        for t in self._cross_beams_pos:
            k = 0
            for i in range(7):
                if(self._obj[t[0]+i][t[1]-i] == self._bullets.show_matrix(1) or self._obj[t[0]+i][t[1]-i] == self._bullets.show_matrix(0)):
                    self.remove_bullet(t[0]+i,t[1]-i,l)
                    k = 1
            if(k==1):
                for i in range(7):
                    self._map[t[0]+i][t[1]-i] = " "
                t[0] = 0
                t[1] = 0

    def update(self):
        for i in range(self._length):
            for j in range(self._breadth):
                self._obj[i][j] = self._map[i][j]
    def update_man(self, man, l):
        for i in range(3):
            for j in range(3):
                self._obj[man.show_pos_x()+i][l+man.show_pos_y()+j] = man.show_matrix(i,j)
        if(man.show_mode() == 1 and man.show_shield_countdown() > 550):
            self._obj[man.show_pos_x()][l+man.show_pos_y()-1] = '\57'
            self._obj[man.show_pos_x()+1][l+man.show_pos_y()-1] = '\174'
            self._obj[man.show_pos_x()+2][l+man.show_pos_y()-1] = '\134'
            self._obj[man.show_pos_x()][l+man.show_pos_y()+3] = '\134'
            self._obj[man.show_pos_x()+1][l+man.show_pos_y()+3] = '\174'
            self._obj[man.show_pos_x()+2][l+man.show_pos_y()+3] = '\57'
        man.decrement_count()
        if(man.show_mode() == 1 and man.show_shield_countdown() < 500):
            man.shield_down()
    
    def magnet_effect(self,man,l):
        for i in self._magnets_pos:
            left = 0
            right = 0
            up = 0
            down = 0
            if(man.show_pos_x() < i[0] and man.show_pos_x() + 10 > i[0]):
                down = 1
            if(man.show_pos_x() > i[0] and man.show_pos_x() - 10 < i[0]):
                up = 1
            if(l + man.show_pos_y() < i[1] and l + man.show_pos_y() + 10 > i[1]):
                right = 1
            if(l + man.show_pos_y() > i[1] and l + man.show_pos_y() - 10 < i[1]):
                left = 1
            if(left+right+up+down == 2):
                if(left == 1):
                    man.move_left(1)
                if(right == 1):
                    man.move_right(1)
                if(up == 1):
                    man.move_up(1)
                if(down == 1):
                    man.move_down(1,30)
    def update_boss(self,boss,man,l):
        if(l + self._frame_width >= self._breadth):
            for i in range(15):
                for j in range(38):
                    if(man.show_pos_x()+16 >= self._length):
                        if(self._obj[self._length - 16+i][self._breadth-boss.show_dim_y()+j-1] == self._bullets.show_matrix(1)):
                            boss.die()
                            man.add_score()
                            self.remove_bullet(self._length - 16+i,self._breadth-boss.show_dim_y()+j-1,l)
                        self._obj[self._length - 16+i][self._breadth-boss.show_dim_y()+j-1] = boss.show_matrix(i,j)
                    else:
                        if(self._obj[man.show_pos_x()+i][self._breadth-boss.show_dim_y()+j-1] == self._bullets.show_matrix(1)):
                            boss.die()
                            man.add_score()
                            self.remove_bullet(man.show_pos_x()+i,self._breadth-boss.show_dim_y()+j-1,l)
                        self._obj[man.show_pos_x()+i][self._breadth-boss.show_dim_y()+j-1] = boss.show_matrix(i,j)

    
    def update_bullets(self,man,l):
        for i in self._bullets_pos:
            if(i[1] < self._frame_width-1 and l + i[1] < self._breadth-1):
                self._obj[i[0]][l + i[1]] = self._bullets.show_matrix(0)
                self._obj[i[0]][l + i[1]+1] = self._bullets.show_matrix(1)
                i[1] = i[1] + 1
            
    def remove_bullet(self,x,y,l):
        for i in self._bullets_pos:
            if(i[0] == x and i[1] + l == y):
                self._bullets_pos.remove(i)
            if(i[0] == x and i[1] - 1 + l == y):
                self._bullets_pos.remove(i)
            
    def update_ice_balls(self,l):
        for i in self._ice_balls_pos:
            if(i[1] > 2):
                if(self._obj[i[0]][i[1]] == self._bullets.show_matrix(1) or self._obj[i[0]][i[1]] == self._bullets.show_matrix(0)):
                    i[0] = 0
                    i[1] = 0
                else:
                    self._obj[i[0]][i[1]] = self._beams.show_val()       ##  check here
                    i[1] = i[1] - 1
            
    def fill_coins(self):
        for i in range(int(self._breadth/20)):
            pos_x = r(0,self._length-2)
            pos_y = r(2,self._breadth-100)
            c = Coins(pos_x,pos_y)
            self._coins_pos[i][0] = pos_x
            self._coins_pos[i][1] = pos_y
            self.update_object(c)
    
    def fill_hor_beams(self):
        for i in range(int(self._breadth/40)):
            pos_x = r(3,self._length-1)
            pos_y = r(50,self._breadth-100)
            self._hor_beams_pos[i][0] = pos_x
            self._hor_beams_pos[i][1] = pos_y
            v = Hor_beams(pos_x,pos_y)
            self.update_object(v) 
    
    def fill_ver_beams(self):
        for i in range(int(self._breadth/40)):
            pos_x = r(5,self._length-7)
            pos_y = r(50,self._breadth-100)
            self._ver_beams_pos[i][0] = pos_x
            self._ver_beams_pos[i][1] = pos_y
            h = Ver_beams(pos_x,pos_y)
            self.update_object(h)
    
    def fill_cross_beams(self):
        for i in range(int(self._breadth/40)):
            pos_x = r(3,self._length-7)
            pos_y = r(50,self._breadth-100)
            # print(pos_x,"   ",pos_y)
            self._cross_beams_pos[i][0] = pos_x
            self._cross_beams_pos[i][1] = pos_y
            self._map[pos_x][pos_y] = self._beams.show_val()
            self._map[pos_x+1][pos_y-1] = self._beams.show_val()
            self._map[pos_x+2][pos_y-2] = self._beams.show_val()
            self._map[pos_x+3][pos_y-3] = self._beams.show_val()
            self._map[pos_x+4][pos_y-4] = self._beams.show_val()
            self._map[pos_x+5][pos_y-5] = self._beams.show_val()
    
    def fill_magnets(self):
        for i in range(int(self._breadth/100)):
            pos_x = r(3,self._length-7)
            pos_y = r(10,self._breadth-100)
            self._magnets_pos[i][0] = pos_x
            self._magnets_pos[i][1] = pos_y
            m = Magnets(pos_x,pos_y)
            self.update_object(m)
            
    def collision_check(self,man,a,l):
        temp = 0
        for i in range(3):
            for j in range(3):
                if(self._map[man.show_pos_x()+i][l+man.show_pos_y()+j]==self._beams.show_val()):
                    temp = 1
                if(self._map[man.show_pos_x()+i][l+man.show_pos_y()+j]==self._coins.show_val()):
                    man.add_score()
                    self._map[man.show_pos_x()+i][l+man.show_pos_y()+j]=" "
                if(self._obj[man.show_pos_x()+i][l+man.show_pos_y()+j]==self._beams.show_val()):
                    temp = 1
        if(temp==1):
            man.die()
        
        
    def shoot(self,man,l):
        self._bullets_pos.append([man.show_pos_x()+1,man.show_pos_y()])
        self.update_bullets(man,l)
        
    def throw(self,boss,man,l):
        if(l + self._frame_width >= self._breadth):
            self._ice_balls_pos.append([man.show_pos_x()+1,self._breadth-boss.show_dim_y()])
            self.update_ice_balls(l)
    
    def show_colour(self,x):
        if(x == "~"):
            return Fore.CYAN + "~"
        elif(x == ">"):
            return Fore.CYAN + ">"
        elif(x == self._beams.show_val()):                                                                                 ##check here
            return Fore.RED + self._beams.show_val()
        elif(x == self._coins.show_val()):
            return Fore.YELLOW + self._coins.show_val()
        elif(x == ":"):
            return Fore.WHITE + ":"
        elif(x == ";"):
            return Fore.WHITE + ";"
        elif(x == "."):
            return Fore.WHITE + "."
        elif(x == "'"):
            return Fore.WHITE + "'"
        else:
            return Fore.BLUE + x
        
        
        
        
