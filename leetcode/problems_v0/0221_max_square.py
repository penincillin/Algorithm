"""
Maximal Square, https://leetcode.com/problems/maximal-square/
Use DP, the key is to consider based on lower-right corner, instead of upper-left corner
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb


class Solution(object):
    def maximalSquare(self, matrix):
        return self.solve_dp(matrix)

    def solve_dp(self, matrix):
        N = len(matrix)
        M = len(matrix[0])
        dp = [[0 for j in range(M)] for i in range(N)]
        res = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "1":
                    if i>0 and j>0: # first row and first column will be no large than 1
                        res1 = dp[i-1][j]
                        res2 = dp[i][j-1]
                        res3 = dp[i-1][j-1]
                        dp[i][j] = min(min(res1, res2), res3) + 1
                        res = max(res, dp[i][j])
                    else:
                        dp[i][j] = 1
                        res = max(res, dp[i][j])
        return res * res
    

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    sol = Solution()
    res = sol.maximalSquare(matrix)
    print(res)


if __name__ == '__main__':
    main()
