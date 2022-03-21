"""
Pascal's Triangle, https://leetcode.com/problems/pascals-triangle/
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb

class Solution(object):
    def generate(self, numRows):
        N = numRows
        result = list()
        if N == 0:
            return []
        else:
            result.append([1,])
            for i in range(1, N):
                mid_res = list()
                for j in range(i+1):
                    j0 = j-1
                    j1 = j
                    left = result[i-1][j0] if j0>=0 else 0
                    right = result[i-1][j1] if j1<len(result[i-1]) else 0
                    mid_res.append(left + right)
                result.append(mid_res)
            return result


def main():
    sol = Solution()

    N = 5
    res = sol.generate(N)
    for r in res:
        print(r)


if __name__ == '__main__':
    main()
