"""
37. Valid Sudoku, https://leetcode.com/problems/sudoku-solver/
Simple back-trace DFS
"""
import sys
import copy
import numpy as np

class Solution(object):
    def check_board(self, board):
        self.board = [[-1 for _ in range(9)] for _ in range(9)]
        self.ori_fill = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value.isdigit():
                    self.ori_fill[i][j] = 1
                    self.board[i][j] = int(value) - 1

    def get_choices(self, depth):
        x = (depth % 9)
        y = (depth // 9)
        box_x = (x//3)*3
        box_y = (y//3)*3
        exist = [0 for _ in range(9)]

        # col
        for i in range(9):
            value = self.board[i][x]
            if value >= 0:
                exist[value] = True

        # row
        for i in range(9):
            value = self.board[y][i]
            if value >= 0:
                exist[value] = True

        # bbox
        for i in range(9):
            d_x = i // 3
            d_y = i % 3
            value = self.board[box_y+d_y][box_x+d_x]
            if value >= 0:
                exist[value] = True

        choices = list()
        for i in range(9):
            if not exist[i]:
                choices.append(i)
        return choices

        
    def solve(self, depth):
        if depth>80: 
            return True
        else:
            x = (depth % 9)
            y = (depth // 9)
            if self.ori_fill[y][x]:
                return self.solve(depth+1)
            else:
                choices = self.get_choices(depth)
                for num in choices:
                    self.board[y][x] = num
                    res = self.solve(depth+1)
                    if res:
                       return True
                    else:
                        self.board[y][x] = -1
                return False


    def solveSudoku(self, board):
        self.check_board(board)
        res = self.solve(0)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(self.board[i][j]+1)


if __name__ == '__main__':

    board = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"] ]
    

    sol = Solution()
    sol.solveSudoku(board)
    for i in range(9):
        print(board[i])
    '''
    for i in range(len(board)):
        print(board[i])
    '''
