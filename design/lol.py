# class Boss():
#     def __init__(self):
#         self.matrix = []
#         with open("./yoda.ansi.txt") as design:
#             for line in design:
#                 self.matrix.append(line.strip('\n'))
#     def show(self):
#         # print(self.matrix)
#         # for i in self.matrix:
#         #     self.matrix.remove(i)
#         for i in self.matrix:
#             print(i)
#             # for i in range(15):
#         #     for j in range(38):
#         #         print(self.matrix[i][j],end="")
#         #     print()
#             # print(len(self.matrix[i]))
# a = Boss()

# # a.matrix.remove(a.matrix[2])
# a.show()
# # a = 5.7
# # print(int(a))
 
from colorama import Fore, Back, Style 
print(Fore.RED + 'some red text') 
print(Back.GREEN + 'and with a green background') 
print(Style.DIM + 'and in dim text') 
print(Style.RESET_ALL) 
print('back to normal now') 