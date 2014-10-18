__author__ = 'pruyne'
import random

class Board:
    def __init__(self):
        self.columns = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.changing = True
        self.valid_move = False

    def __str__(self):
        full_board = """+-------------+
|%s|%s|%s|%s|%s|%s|%s|
+-------------+
|%s|%s|%s|%s|%s|%s|%s|
+-------------+
|%s|%s|%s|%s|%s|%s|%s|
+-------------+
|%s|%s|%s|%s|%s|%s|%s|
+-------------+
|%s|%s|%s|%s|%s|%s|%s|
+-------------+
|%s|%s|%s|%s|%s|%s|%s|
+-------------+""" % (
            self.columns[0][0], self.columns[1][0], self.columns[2][0], self.columns[3][0], self.columns[4][0],
            self.columns[5][0], self.columns[6][0],
            self.columns[0][1], self.columns[1][1], self.columns[2][1], self.columns[3][1], self.columns[4][1],
            self.columns[5][1], self.columns[6][1],
            self.columns[0][2], self.columns[1][2], self.columns[2][2], self.columns[3][2], self.columns[4][2],
            self.columns[5][2], self.columns[6][2],
            self.columns[0][3], self.columns[1][3], self.columns[2][3], self.columns[3][3], self.columns[4][3],
            self.columns[5][3], self.columns[6][3],
            self.columns[0][4], self.columns[1][4], self.columns[2][4], self.columns[3][4], self.columns[4][4],
            self.columns[5][4], self.columns[6][4],
            self.columns[0][5], self.columns[1][5], self.columns[2][5], self.columns[3][5], self.columns[4][5],
            self.columns[5][5], self.columns[6][5])
        return full_board

    def add_piece(self, column, player):
        self.valid_move = False
        row = 0
        for piece in self.columns[column]:
            if piece == 0:
                row = row + 1
            else:
                break
        row = row - 1
        if not row == -1:
            self.valid_move = True
            self.columns[column][row] = player

    def check_win(self):
        win = False
        #horizontal win
        for column in range(0,4):
            for row in range(0,6):
                if self.columns[column][row] != 0:
                    if self.columns[column][row] == self.columns[column + 1][row] == self.columns[column + 2][row] == self.columns[column + 3][row]:
                        win = True
                        return win
        #vertical win
        for column in range(0,7):
            for row in range(0,3):
                if self.columns[column][row]!= 0:
                    if self.columns[column][row] == self.columns[column][row + 1] == self.columns[column][row + 2]  == self.columns[column][row + 3]:
                        win = True
                        return win
        #diagonal down left win
        for column in range(3,7):
            for row in range(0,3):
                if self.columns[column][row] != 0:
                    if self.columns[column][row] == self.columns[column - 1][row + 1] == self.columns[column - 2][row + 2] == self.columns[column - 3][row + 3]:
                        win = True
                        return win
        #diagonal down right win
        for column in range(0,4):
            for row in range(0,3):
                if self.columns[column][row] != 0:
                    if self.columns[column][row] == self.columns[column + 1][row + 1] == self.columns[column + 2][row + 2] == self.columns[column + 3][row + 3]:
                        win = True
                        return win
        win = False
        return win







my_board = Board()
win = False
while not win:
    print my_board
    play_column = input("Red piece: ")
    my_board.add_piece(play_column, 'R')
    if my_board.check_win()== True:
        win = True
        winner = "red"
        break
    print my_board
    play_column = input("Black piece:")
    my_board.add_piece(play_column, 'B')
    if my_board.check_win()== True:
        win = True
        winner = "black"
        break
print my_board
print play_column