"""
Range Sum Query 2D - Immutable, https://leetcode.com/problems/range-sum-query-2d-immutable/
Prefix sum of matrix version.
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb
from math import sqrt


class NumMatrix(object):

    def __init__(self, matrix):
        N = len(matrix)
        M = len(matrix[0])
        dp = [[0 for j in range(M)] for i in range(N)]

        # first row
        res = 0
        for j in range(M):
            dp[0][j] = (res + matrix[0][j])
            res = dp[0][j]

        # first column
        res = dp[0][0]
        for i in range(1, N): # skip 0 becase is already calculated
            dp[i][0] = (res + matrix[i][0])
            res = dp[i][0]

        # remain results
        for i in range(1, N):
            for j in range(1, M):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
        self.dp = dp
            
        

    def sumRegion(self, row1, col1, row2, col2):
        i1, j1 = row1-1, col1-1
        i2, j2 = row2, col2
        res1 = self.dp[i2][j2]
        res2 = self.dp[i1][j2] if i1 >= 0 else 0
        res3 = self.dp[i2][j1] if j1 >=0 else 0
        res4 = self.dp[i1][j1] if i1 >= 0 and j1 >= 0 else 0
        res = res1 - res2 -res3 + res4
        # print(res1, res2, res3, res4)
        return res


def main():
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    nm = NumMatrix(matrix)

    res = nm.sumRegion(2, 1, 4, 3)
    print(res)

    res = nm.sumRegion(1, 1, 2, 2)
    print(res)

    res = nm.sumRegion(1, 2, 2, 4)
    print(res)


if __name__ == '__main__':
    main()
