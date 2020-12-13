"""
Surrounded Regions, https://leetcode.com/problems/surrounded-regions/
Suppose no 'O' on board, then all the other 'O's can be captured.
If there are some 'O' on board, then the 'O' surronding it can not be captured. And so on.
This process should be repeated until no more 'O'.
"""
import os, sys, shutil


class Solution(object):
    def solve(self, board):
        if len(board) == 0:
            return
        elif len(board[0]) == 0:
            return
        else:
            N = len(board)
            M = len(board[0])
            flip = [[True for j in range(M)] for i in range(N)] # whether one can be flipped
            checked = [[False for j in range(M)] for i in range(N)] # whether one can be flipped

            queue = list()

            # check border first
            for j in range(M):
                for i in [0, N-1]:
                    if board[i][j] == 'O':
                        flip[i][j] = False
                        queue.append( (i, j) )
            for i in range(N):
                for j in [0, M-1]:
                    if board[i][j] == 'O':
                        flip[i][j] = False
                        queue.append( (i, j) )

            while(len(queue)>0):
                i, j = queue.pop(0)
                flip[i][j] = False
                for di, dj in [(-1,0), (1,0), (0,1), (0,-1)]:
                        i0 = i + di
                        j0 = j + dj
                        if i0 > 0 and i0 < N-1 and j0 > 0 and j0 < M-1:
                            if (not checked[i0][j0]) and board[i0][j0] == 'O':
                                queue.append( (i0, j0) )
                                checked[i0][j0] = True

            for i in range(N):
                for j in range(M):
                    if board[i][j]=='O' and flip[i][j]:
                        board[i][j] = 'X'


def print_board(board):
    for row in board:
        print(row)


def main():
    board = [
        ['X', 'X', 'X', 'X',],
        ['X', 'O', 'O', 'X',],
        ['X', 'O', 'O', 'X',],
        ['X', 'O', 'X', 'X',]
    ]
    print_board(board)
    sol = Solution()
    sol.solve(board)
    print('------------------')
    print_board(board)


if __name__ == '__main__':
    main()
