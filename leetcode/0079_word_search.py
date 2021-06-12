"""
Word Search, https://leetcode.com/problems/word-search/
DFS
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def exist(self, board, word):
        N = len(board)
        M = len(board[0])
        used = [[False for j in range(M)] for i in range(N)]

        for i in range(N):
            for j in range(M):
                if board[i][j]==word[0]:
                    used[i][j] = True
                    mid_res = self.search(board, word[1:], used, i, j)
                    if mid_res:
                        return True
                    else:
                        used[i][j] = False
        return False

    def search(self, board, word, used, row, col):
        if len(word) == 0:
            return True
        else:
            N = len(board)
            M = len(board[0])
            for i0, j0 in [(-1,0), (1,0), (0,1), (0,-1)]:
                i, j = row+i0, col+j0
                if i >= 0 and i < N and j >=0 and j < M:
                    if board[i][j] == word[0] and not used[i][j]:
                        cur_pos = i*M+j
                        used[i][j] = True
                        mid_res = self.search(board, word[1:], used, i, j)
                        if mid_res:
                            return True
                        else:
                            used[i][j] = False
            return False
            
        

def main():
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCCED"
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "SEE"
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCB"

    sol = Solution()
    res = sol.exist(board, word)
    print(res)


if __name__ == '__main__':
    main()
