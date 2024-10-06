"""
Maximal Rectangle, https://leetcode.com/problems/maximal-rectangle/
The most brutal force method takes O(N^6) time complexity.
A better way implemented as solve_brutal takes O(N^4) time complexity.
A good idea is to convert this problem into max_hist_rectangle problem of (https://leetcode.com/problems/largest-rectangle-in-histogram/), the time complexity is O(N^2)
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


def print_matrix(matrix):
    N = len(matrix) # number of rows
    M = len(matrix[0]) # number of columns
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end=' ')
        print()


class Solution(object):
    def maximalRectangle(self, matrix):
        N = len(matrix)
        if N == 0:
            return 0
        else:
            M = len(matrix[0])
            if M == 0:
                return 0
            else:
                return self.solve(matrix)


    def solve_brutal(self, matrix):
        """
        suppose N rows and M cols, the time complexity of this solution is (NM)^2
        """
        N = len(matrix) # number of rows
        M = len(matrix[0]) # number of columns
        # accumulating sums
        sums = [[0 for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                sum_0 = sums[i-1][j] if i > 0 else 0
                sum_1 = sums[i][j-1] if j > 0 else 0
                sum_2 = sums[i-1][j-1] if (i > 0 and j > 0) else 0
                sums[i][j] = sum_0 + sum_1 - sum_2 + int(matrix[i][j])
        # check each rectangle and check whether the sum equals to the number of cells
        res = 0
        for i0 in range(N):
            for j0 in range(M):
                for i1 in range(i0, N):
                    for j1 in range(j0, M):
                        sum_0 = sums[i1][j1]
                        sum_1 = sums[i0-1][j1] if i0 > 0 else 0
                        sum_2 = sums[i1][j0-1] if j0 > 0 else 0
                        sum_3 = sums[i0-1][j0-1] if (i0 > 0 and j0 > 0) else 0
                        area = sum_0 + sum_3 - sum_1 - sum_2
                        if area == (i1-i0+1)*(j1-j0+1):
                            res = max(area, res)
        return res


    def max_hist(self, height):
        """
        This function implements this, https://leetcode.com/problems/largest-rectangle-in-histogram/
        The time complexity is O(M)
        """
        height.append(0) # add zero to tail
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1 # this operation is important, since
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

    def solve(self, matrix):
        N = len(matrix)
        M = len(matrix[0])
        height = [0 for i in range(M)]
        res = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j]=='1':
                    height[j] += 1
                else:
                    height[j] = 0
            res = max(self.max_hist(height), res)
        return res
   

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # matrix = [["1"]]

    sol = Solution()
    res = sol.maximalRectangle(matrix)
    print(res)


if __name__ == '__main__':
    main()
