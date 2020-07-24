import numpy as np
from objects import Objects

class Beams(Objects):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self._val = "@"
    def show_val(self):
        return "@"
class Hor_beams(Beams):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self._dim_x = 1
        self._dim_y = 7
        matrix = np.empty((1,7), dtype='str')
        matrix[0][0] = self._val
        matrix[0][1] = self._val
        matrix[0][2] = self._val
        matrix[0][3] = self._val
        matrix[0][4] = self._val
        matrix[0][5] = self._val
        matrix[0][6] = self._val
        self._matrix = matrix
        self._touch = 0
    def show_matrix(self,i,j):
        return self._matrix[i][j]
    def touched(self):
        if(self._touch == 0):
            self._touch = 1
            return 0
        else:
            return 1
    def end_pts(self):
        return {self._pos_x,self._pos_y,self._pos_x,self._pos_y+6}

class Ver_beams(Beams):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self._dim_x = 7
        self._dim_y = 1
        matrix = np.empty((7,1),dtype='str')
        matrix[0][0] = self._val
        matrix[1][0] = self._val
        matrix[2][0] = self._val
        matrix[3][0] = self._val
        matrix[4][0] = self._val
        matrix[5][0] = self._val
        matrix[6][0] = self._val
        self._matrix = matrix
    def show_matrix(self,i,j):
        return self._matrix[i][j]

class Cross_beams(Beams):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
