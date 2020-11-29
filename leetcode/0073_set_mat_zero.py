"""
Set Matrix Zeroes, https://leetcode.com/problems/set-matrix-zeroes/
1. Use inplace storage, set flag to indicate row, column information.
2. When update results, be aware of the correct order.
"""

import os, sys, shutil


class Solution(object):
    def setZeroes(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        else:
            N = len(matrix)
            M = len(matrix[0])
            zero_first_column = False
            for i in range(N):
                for j in range(M):
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        if j != 0:
                            matrix[0][j] = 0
                        else:
                            zero_first_column = True

            # update column first
            for j in range(1, M):
                if matrix[0][j] == 0:
                    for i in range(N):
                        matrix[i][j] = 0
            
            # update row then
            for i in range(N):
                if matrix[i][0] == 0:
                    for j in range(M):
                        matrix[i][j] = 0

            # update first column in the end
            if zero_first_column:
                for i in range(N):
                    matrix[i][0] = 0


def main():
    sol = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
