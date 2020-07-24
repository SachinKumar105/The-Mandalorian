import numpy as np
import time as t
from colorama import Fore, Back, Style 
def deployman(r,c,manfig):
    print('\033[{};{}H'.format(r,c),end="")
    for i in range(len(manfig)):
        for j in range(len(manfig[i])):
            print(manfig[i][j],end="")
        print('\033[1B',end="")
        print('\033[3D',end="")
    for i in range(r+4,21):
        print('\42',end="")
        print('\033[1B',end="")
        print('\033[1D',end="")
class Person():
    def __init__(self,pos_x,pos_y):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._dim_x = 0
        self._dim_y = 0
        self._lives = 0
    def show_pos_x(self):
        return self._pos_x
    def show_pos_y(self):
        return self._pos_y
    def show_dim_x(self):
        return self._dim_x
    def show_dim_y(self):
        return self._dim_y
    def die(self):
        self._lives = self._lives - 1
class Man(Person):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self._dim_x = 3
        self._dim_y = 3
        self._shield_mode = 0
        self._shield_countdown = 0
        self._score = 0
        self._lives = 3
        self._boost = 0
        matrix = []
        with open("./design/din.txt") as design:
            for line in design:
                matrix.append(line.strip('\n'))
        self._matrix = matrix
    def move_right(self,i):
        self._pos_y = self._pos_y + i
    def move_left(self,i):
        if(self._pos_y > 2):
            self._pos_y = self._pos_y - i
    def move_up(self,i):
        if(self._pos_x > 2):
            self._pos_x = self._pos_x - i
    def move_down(self,i,j):
        if(self._pos_x + self._dim_x  + i < j):
            self._pos_x = self._pos_x + i
    def set_pos_x(self,i):
        self._pos_x = i
    def set_pos_y(self,i):
        self._pos_y = i
    def show_score(self):
        return self._score
    def show_lives(self):
        return self._lives
    def show_matrix(self,i,j):
        return self._matrix[i][j]
    def show_boost(self):
        return self._boost
    def add_score(self):
        self._score = self._score + 1
    def shield(self):
        if(self._shield_countdown < 1):
            self._shield_countdown = 600
            self._shield_mode = 1
    def shield_down(self):
        self._shield_mode = 0
    def show_mode(self):
        return self._shield_mode
    def show_shield_countdown(self):
        return self._shield_countdown
    def decrement_count(self):
        self._shield_countdown = self._shield_countdown - 1
    def speed_boost(self):
        self._boost = 1
    def die(self):
        if(self._lives == 0):
            # exit()
            self.lose()
        if(self._shield_mode == 0):
            self._lives = self._lives - 1
    def lose(self):
        self._mat = []
        with open("./design/lost.txt") as design:
            for line in design:
                self._mat.append(line.strip('\n'))
            print('\033[2J', end="")
            print('\033[0;0H', end="")
            for i in self._mat:
                print(Fore.RED + i)
            print(Style.RESET_ALL,end="")
            print("score : ",self._score)
        exit()
    
class Boss(Person):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self._dim_x = 15
        self._dim_y = 38
        self._lives = 10
        self._matrix = []
        with open("./design/boss.txt") as design:
            for line in design:
                self._matrix.append(line.strip('\n'))
    def show_lives(self):
        return self._lives
    def die(self):
        if(self._lives == 0):
            # exit()
            # self.win()
            self._pos_y = 5
        else:
            self._lives = self._lives - 1
    def show_matrix(self,i,j):
        return self._matrix[i][j]
    def win(self,man):
        self._mat = []
        with open("./design/yoda.txt") as design:
            for line in design:
                self._mat.append(line.strip('\n'))
            print('\033[2J', end="")
            print('\033[0;0H', end="")
            for i in self._mat:
                print(Fore.GREEN + i)
            print(Style.RESET_ALL,end="")
            print("score : ",man.show_score())

            
        exit()