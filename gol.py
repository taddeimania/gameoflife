import random
import copy

class LifeNode():

    def __init__(self):
        rand = random.random()
        if rand < 0.5:
            self.lifestate = 1
        else:
            self.lifestate = 0

    def __str__(self):
        states = {0:" ", 1:"X"}
        return states[self.lifestate]

class CreateBoard():

    def __init__(self, size):
        self.BOARD = []
        self.NEW_BOARD = []
        self.size = size

    def generate_board(self):
        row = []
        for x in range(self.size):
            for y in range(self.size):
               row.append(LifeNode())
            self.BOARD.append(row)
            row = []

    def draw_board(self, board):
        for row in board:
            for cell in row:
                print "", cell, "",
            print "\n"

    def iterate_board(self):
        tmp = self.copy_board(self.BOARD)
        for idx, row in enumerate(self.BOARD):
            for idxx, cell in enumerate(row):
                locale_tuple = (idx, idxx)
                self.check_neighbors(tmp, locale_tuple)
        self.BOARD = self.copy_board(tmp)
        self.draw_board(self.BOARD)

    def copy_board(self, board):
        return copy.deepcopy(board)

    def check_neighbors(self, tmp, locale_tuple):
        count = self.count_neighbors(locale_tuple)
        if count < 2:
            self.die_cell(tmp, locale_tuple)
        if count in [2,3] and tmp[locale_tuple[0]][locale_tuple[1]].lifestate == 1:
            self.live_cell(tmp, locale_tuple)
        if count == 3:
            self.live_cell(tmp, locale_tuple)
        if count > 3:
            self.die_cell(tmp, locale_tuple)

    def count_neighbors(self, loc):
        neighbor_count = 0
        high_bound = self.size - 1
        if loc[0] > 0:
            if loc[1] > 0:
                neighbor_count += self.BOARD[loc[0] - 1][loc[1] - 1].lifestate
            elif loc[1] == 0:
                neighbor_count += self.BOARD[loc[0] - 1][high_bound].lifestate

            neighbor_count += self.BOARD[loc[0] - 1][loc[1]].lifestate

            if loc[1] < high_bound:
                neighbor_count += self.BOARD[loc[0] - 1][loc[1] + 1].lifestate
            elif loc[1] == high_bound:
                neighbor_count += self.BOARD[loc[0] - 1][0].lifestate

        if loc[1] > 0:
            neighbor_count += self.BOARD[loc[0]][loc[1] - 1].lifestate
        elif loc[1] == 0:
            neighbor_count += self.BOARD[loc[0]][high_bound].lifestate

        if loc[1] < high_bound:
            neighbor_count += self.BOARD[loc[0]][loc[1] + 1].lifestate
        elif loc[1] == high_bound:
            neighbor_count += self.BOARD[loc[0]][0].lifestate

        if loc[0] < high_bound:
            if loc[1] > 0:
                neighbor_count += self.BOARD[loc[0] + 1][loc[1] - 1].lifestate
            elif loc[1] == 0:
                neighbor_count += self.BOARD[loc[0] + 1][high_bound].lifestate

            neighbor_count += self.BOARD[loc[0] + 1][loc[1]].lifestate

            if loc[1] < high_bound:
                neighbor_count += self.BOARD[loc[0] + 1][loc[1] + 1].lifestate
            if loc[1] == high_bound:
                neighbor_count += self.BOARD[loc[0] + 1][0].lifestate
        return neighbor_count

    def die_cell(self, board, loc):
        board[loc[0]][loc[1]].lifestate = 0

    def live_cell(self, board, loc):
        board[loc[0]][loc[1]].lifestate = 1


def main():
    import time
    import os
    board = CreateBoard(30)
    board.generate_board()
    board.draw_board(board.BOARD)
    while True:
        #dummy = raw_input()
        os.system('clear')
        board.iterate_board()
        time.sleep(.05)

if __name__ == "__main__":
    main()
