import numpy as np
class Objects:
    def __init__(self,pos_x,pos_y):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._dim_x = 0
        self._dim_y = 0
    def show_pos_x(self):
        return self._pos_x
    def show_pos_y(self):
        return self._pos_y
    def show_dim_x(self):
        return self._dim_x
    def show_dim_y(self):
        return self._dim_y
class Coins(Objects):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self._dim_x = 2
        self._dim_y = 2
        self._val = "$"
        self._matrix = np.empty((2,2), dtype='str')
        self._matrix[0][0] = "$"
        self._matrix[0][1] = "$"
        self._matrix[1][0] = "$"
        self._matrix[1][1] = "$"
    def show_val(self):
        return self._val
    def show_matrix(self,i,j):
        return self._matrix[i][j]
# class Hor_beams(Objects):
#     def __init__(self,pos_x,pos_y):
#         super().__init__(pos_x,pos_y)
#         self._dim_x = 1
#         self._dim_y = 7
#         matrix = np.empty((1,7), dtype='str')
#         matrix[0][0] = "@"
#         matrix[0][1] = "@"
#         matrix[0][2] = "@"
#         matrix[0][3] = "@"
#         matrix[0][4] = "@"
#         matrix[0][5] = "@"
#         matrix[0][6] = "@"
#         self._matrix = matrix
#         self._touch = 0
#     def show_matrix(self,i,j):
#         return self._matrix[i][j]
#     def touched(self):
#         if(self._touch == 0):
#             self._touch = 1
#             return 0
#         else:
#             return 1
#     def end_pts(self):
#         return {self._pos_x,self._pos_y,self._pos_x,self._pos_y+6}

# class Ver_beams(Objects):
#     def __init__(self,pos_x,pos_y):
#         super().__init__(pos_x,pos_y)
#         self._dim_x = 7
#         self._dim_y = 1
#         matrix = np.empty((7,1),dtype='str')
#         matrix[0][0] = "@"
#         matrix[1][0] = "@"
#         matrix[2][0] = "@"
#         matrix[3][0] = "@"
#         matrix[4][0] = "@"
#         matrix[5][0] = "@"
#         matrix[6][0] = "@"
#         self._matrix = matrix
#     def show_matrix(self,i,j):
#         return self._matrix[i][j]

# class Cross_beams(Objects):
#     def __init__(self,pos_x,pos_y):
#         super().__init__(pos_x,pos_y)

class Magnets(Objects):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self._matrix = []
        with open("./design/magnet.txt") as design:
            for line in design:
                self._matrix.append(line.strip('\n'))
        self._dim_x = 3
        self._dim_y = 6
    def show_matrix(self,i,j):
        return self._matrix[i][j]

class Ice_balls(Objects):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self._val = "@"
    def show_val(self):
        return self._val

class Bullets(Objects):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        # self._matrix = []
        # self._matrix[0] = "~"
        # self._matrix[1] = ">"
        # self._matrix[0] = "~"
        # self._matrix[1] = ">"
    def show_matrix(self,i):
        if(i==0):
            return "~"
        elif(i==1):
            return ">"
        # return self._matrix[i]