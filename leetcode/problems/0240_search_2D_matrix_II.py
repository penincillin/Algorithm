"""
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def searchMatrix(self, matrix, target):
        return self.solve_02(matrix, target)


    def bin_search(self, search_type, matrix, target, i, start, end):
        assert search_type in [0, 1]
        while start < end:
            mid = (start + end) // 2
            value = matrix[i][mid] if search_type==0 else matrix[mid][i]
            if value == target:
                return True
            elif value < target:
                start = mid + 1
            else:
                end = mid
        return False


    def solve_01(self, matrix, target):
        # the time complexity if n * log(m)
        # do bin_search row by row
        m = len(matrix)        
        n = len(matrix[0])
        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                if self.bin_search(0, matrix, target, i, 0, n):
                    return True
        return False
    

    def solve_02(self, matrix, target):
        # starts from left bottom or right top, then discard one row or one column each time
        m = len(matrix)        
        n = len(matrix[0])
        i = m-1; j = 0
        while( i>=0 and j<n): # to be determined
            value = matrix[i][j]
            if value == target:
                return True
            elif value < target:
                j += 1
            else:
                i -= 1
        return False


def main():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]; 
    target = 22

    sol = Solution()
    res = sol.searchMatrix(matrix, target)
    print(res)


if __name__ == '__main__':
    main()
