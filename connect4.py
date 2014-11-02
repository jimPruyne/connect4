__author__ = 'pruyne'
import sys
import random


class Board:
    def __init__(self):
        self.columns = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
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
            self.columns[0][0], self.columns[1][0], self.columns[2][0], self.columns[3][0],
            self.columns[4][0],
            self.columns[5][0], self.columns[6][0],
            self.columns[0][1], self.columns[1][1], self.columns[2][1], self.columns[3][1],
            self.columns[4][1],
            self.columns[5][1], self.columns[6][1],
            self.columns[0][2], self.columns[1][2], self.columns[2][2], self.columns[3][2],
            self.columns[4][2],
            self.columns[5][2], self.columns[6][2],
            self.columns[0][3], self.columns[1][3], self.columns[2][3], self.columns[3][3],
            self.columns[4][3],
            self.columns[5][3], self.columns[6][3],
            self.columns[0][4], self.columns[1][4], self.columns[2][4], self.columns[3][4],
            self.columns[4][4],
            self.columns[5][4], self.columns[6][4],
            self.columns[0][5], self.columns[1][5], self.columns[2][5], self.columns[3][5],
            self.columns[4][5],
            self.columns[5][5], self.columns[6][5])
        return full_board

    def possible_moves(self):
        possible_moves = []
        item_number = 0
        for item in self.columns:
            if item[0] == 0:
                possible_moves.append(item_number)
            item_number = item_number + 1
        return possible_moves

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

    def remove_piece(self, column):
        row = 0
        for piece in self.columns[column]:
            if piece == 0:
                row = row + 1
            else:
                break
        if row < 6:
            self.columns[column][row] = 0


    def check_win(self):
        win = False
        # horizontal win
        for column in range(0, 4):
            for row in range(0, 6):
                if self.columns[column][row] != 0:
                    if self.columns[column][row] == self.columns[column + 1][row] == \
                            self.columns[column + 2][row] == \
                            self.columns[column + 3][row]:
                        win = True
                        return win
        # vertical win
        for column in range(0, 7):
            for row in range(0, 3):
                if self.columns[column][row] != 0:
                    if self.columns[column][row] == self.columns[column][row + 1] == \
                            self.columns[column][row + 2] == \
                            self.columns[column][row + 3]:
                        win = True
                        return win
        # diagonal down left win
        for column in range(3, 7):
            for row in range(0, 3):
                if self.columns[column][row] != 0:
                    if self.columns[column][row] == self.columns[column - 1][row + 1] == \
                            self.columns[column - 2][
                                        row + 2] == self.columns[column - 3][row + 3]:
                        win = True
                        return win
        # diagonal down right win
        for column in range(0, 4):
            for row in range(0, 3):
                if self.columns[column][row] != 0:
                    if self.columns[column][row] == self.columns[column + 1][row + 1] == \
                            self.columns[column + 2][
                                        row + 2] == self.columns[column + 3][row + 3]:
                        win = True
                        return win
        win = False
        return win

    def check_three(self, color):
        threes = [0, 0, 0]  # closed, 1 end open, 2 ends open
        for column in range(0, 5):
            for row in range(0, 6):
                if self.columns[column][row] == color:
                    if self.columns[column][row] == self.columns[column + 1][row] == \
                            self.columns[column + 2][row]:
                        ends_open = 0
                        if column + 3 < 7 and self.columns[column + 3][row] == 0:
                            ends_open = ends_open + 1
                        if column - 1 > -1 and self.columns[column - 1][row] == 0:
                            ends_open = ends_open + 1
                        threes[ends_open] = threes[ends_open] + 1
        for column in range(0, 7):
            for row in range(0, 4):
                if self.columns[column][row] == color:
                    if self.columns[column][row] == self.columns[column][row + 1] == \
                            self.columns[column][row + 2]:
                        ends_open = 0
                        if row + 3 < 6 and self.columns[column][row + 3] == 0:
                            ends_open = ends_open + 1
                        if row - 1 > -1 and self.columns[column][row - 1] == 0:
                            ends_open = ends_open + 1
                        threes[ends_open] = threes[ends_open] + 1
        for column in range(2, 7):
            for row in range(0, 4):
                if self.columns[column][row] == color:
                    if self.columns[column][row] == self.columns[column - 1][row + 1] == \
                            self.columns[column - 2][
                                        row + 2]:
                        ends_open = 0
                        if column - 3 > -1 and row + 3 < 6 and self.columns[column - 3][
                                    row + 3] == 0:
                            ends_open = ends_open + 1
                        if column + 1 < 7 and row - 1 > -1 and self.columns[column + 1][
                                    row - 1] == 0:
                            ends_open = ends_open + 1
                        threes[ends_open] = threes[ends_open] + 1
        for column in range(0, 5):
            for row in range(0, 4):
                if self.columns[column][row] == color:
                    if self.columns[column][row] == self.columns[column + 1][row + 1] == \
                            self.columns[column + 2][
                                        row + 2]:
                        ends_open = 0
                        if column + 3 < 7 and row + 3 < 6 and self.columns[column + 3][
                                    row + 3] == 0:
                            ends_open = ends_open + 1
                        if column - 1 > -1 and row - 1 > -1 and self.columns[column - 1][
                                    row - 1] == 0:
                            ends_open = ends_open + 1
                        threes[ends_open] = threes[ends_open] + 1
        return threes

    def check_two(self, color):
        twos = [0, 0, 0]  # closed, 1 end open, 2 ends open
        for column in range(0, 6):
            for row in range(0, 6):
                if self.columns[column][row] == color:
                    if self.columns[column][row] == self.columns[column + 1][row]:
                        ends_open = 0
                        if column + 2 < 7 and self.columns[column + 2][row] == 0:
                            ends_open = ends_open + 1
                        if column - 1 > -1 and self.columns[column - 1][row] == 0:
                            ends_open = ends_open + 1
                        twos[ends_open] = twos[ends_open] + 1
        for column in range(0, 7):
            for row in range(0, 5):
                if self.columns[column][row] == color:
                    if self.columns[column][row] == self.columns[column][row + 1]:
                        ends_open = 0
                        if row + 2 < 6 and self.columns[column][row + 2] == 0:
                            ends_open = ends_open + 1
                        if row - 1 > -1 and self.columns[column][row - 1] == 0:
                            ends_open = ends_open + 1
                        twos[ends_open] = twos[ends_open] + 1
        for column in range(1, 7):
            for row in range(0, 5):
                if self.columns[column][row] == color:
                    if self.columns[column][row] == self.columns[column - 1][row + 1]:
                        ends_open = 0
                        if column - 2 > -1 and row + 2 < 6 and self.columns[column - 2][
                                    row + 2] == 0:
                            ends_open = ends_open + 1
                        if column + 1 < 7 and row - 1 > -1 and self.columns[column + 1][
                                    row - 1] == 0:
                            ends_open = ends_open + 1
                        twos[ends_open] = twos[ends_open] + 1
        for column in range(0, 6):
            for row in range(0, 5):
                if self.columns[column][row] == color:
                    if self.columns[column][row] == self.columns[column + 1][row + 1]:
                        ends_open = 0
                        if column + 2 < 7 and row + 2 < 6 and self.columns[column + 2][
                                    row + 2] == 0:
                            ends_open = ends_open + 1
                        if column - 1 > -1 and row - 1 > -1 and self.columns[column - 1][
                                    row - 1] == 0:
                            ends_open = ends_open + 1
                        twos[ends_open] = twos[ends_open] + 1
        return twos


class AI:
    def __init__(self, lookahead, strategy, color):
        self.strategy = strategy
        self.lookahead = int(lookahead)
        self.color = color

    def choose_move(self, board):
        possible_moves = board.possible_moves()
        best_column = []
        best_score = -sys.maxint - 1  # equivalent of negative infinity
        for move_column in possible_moves:
            board.add_piece(move_column, self.color)
            current_column = self.minimax(board, self.lookahead - 1, True)
            if current_column > best_score:
                best_score = current_column
                best_column = []
                best_column.append(move_column)
            elif current_column == best_score:
                best_column.append(move_column)
            board.remove_piece(move_column)
        if len(best_column) > 0:
            chosen_column = random.choice(best_column)
        else:
            chosen_column = -1
        print "%s choosing column %s with value %s" % (self.color, chosen_column, best_score)
        return chosen_column

    def score_board(self, board):
        board_score = 0
        opp_color = 0
        if self.color == "R":
            opp_color = "B"
        else:
            opp_color = "R"
        self_threes = board.check_three(self.color)
        self_twos = board.check_two(self.color)
        opp_threes = board.check_three(opp_color)
        opp_twos = board.check_two(opp_color)
        board_score = board_score + self_threes[0] * self.strategy[0][0]
        board_score = board_score + self_threes[1] * self.strategy[0][1]
        board_score = board_score + self_threes[2] * self.strategy[0][2]
        board_score = board_score + self_twos[0] * self.strategy[1][0]
        board_score = board_score + self_twos[1] * self.strategy[1][1]
        board_score = board_score + self_twos[2] * self.strategy[1][2]
        board_score = board_score + opp_threes[0] * self.strategy[2][0]
        board_score = board_score + opp_threes[1] * self.strategy[2][1]
        board_score = board_score + opp_threes[2] * self.strategy[2][2]
        board_score = board_score + opp_twos[0] * self.strategy[3][0]
        board_score = board_score + opp_twos[1] * self.strategy[3][1]
        board_score = board_score + opp_twos[2] * self.strategy[3][2]
        return board_score

    def minimax(self, board, depth, maximizing_player):
        if depth == 0:
            return self.score_board(board)  # return node heuristic
        if board.check_win() == True:
            if maximizing_player == True:
                return sys.maxint
            else:
                return -sys.maxint - 1
        maximizing_player = not maximizing_player
        moves_to_check = board.possible_moves()
        if maximizing_player:
            best_value = -sys.maxint - 1
            for move in moves_to_check:
                board.add_piece(move, self.color)
                value = self.minimax(board, depth - 1, True)
                if value > best_value:
                    best_value = value
                board.remove_piece(move)
            return best_value
        else:
            best_value = sys.maxint
            opp_color = 0
            if self.color == "R":
                opp_color = "B"
            else:
                opp_color = "R"
            for move in moves_to_check:
                board.add_piece(move, opp_color)
                value = self.minimax(board, depth - 1, False)
                if value < best_value:
                    best_value = value
                board.remove_piece(move)
            return best_value


# main game

offense = [[1, 3, 4], [0, 1, 2], [1, 0, -1], [0, 0, 0]]
defense = [[0, 1, 3], [0, 0, 1], [3, -1, -4], [1, 0, -2]]
red_data = raw_input("Enter red AI:")
black_data = raw_input("Enter black AI:")
total_games = raw_input("Number of games:")
red_parts = red_data.split("_")
red_parts[1] = red_parts[1].replace("lookahead", "")
if red_parts[0] == "offense":
    red_parts[0] = offense
else:
    red_parts[0] = defense
red_ai = AI(red_parts[1], red_parts[0], "R")
black_parts = black_data.split("_")
black_parts[1] = black_parts[1].replace("lookahead", "")
if black_parts[0] == "offense":
    black_parts[0] = offense
else:
    black_parts[0] = defense
black_ai = AI(black_parts[1], black_parts[0], "B")

win = False
red_wins = 0
black_wins = 0
tie_redfirst = 0
tie_blackfirst = 0
game_number = 1
for i in range(1, int(total_games) + 1):
    my_board = Board()
    win = False
    print
    print
    if game_number % 2 == 0:
        while not win:
            print my_board
            play_column = red_ai.choose_move(my_board)
            if play_column == -1:
                win = True
                winner = "Tie"
                tie_redfirst = tie_redfirst + 1
                break
            my_board.add_piece(play_column, 'R')
            print play_column
            if my_board.check_win() == True:
                win = True
                red_wins = red_wins + 1
                winner = "red"
            print my_board
            play_column = black_ai.choose_move(my_board)
            my_board.add_piece(play_column, 'B')
            print play_column
            if my_board.check_win() == True:
                win = True
                black_wins = black_wins + 1
                winner = "black"
                break
    else:
        while not win:
            print my_board
            play_column = black_ai.choose_move(my_board)
            if play_column == -1:
                win = True
                winner = "Tie"
                tie_blackfirst = tie_blackfirst + 1
                break
            my_board.add_piece(play_column, 'B')
            print play_column
            if my_board.check_win() == True:
                win = True
                black_wins = black_wins + 1
                winner = "black"
                break
            print my_board
            play_column = red_ai.choose_move(my_board)
            my_board.add_piece(play_column, 'R')
            print play_column
            if my_board.check_win() == True:
                win = True
                red_wins = red_wins + 1
                winner = "red"

    print my_board
    print winner
print "Red won %s times" % (red_wins)
print "Black won %s times" % (black_wins)
print "There were %s ties with red going first" % (tie_redfirst)
print "There were %s ties with black going first" % (tie_blackfirst)