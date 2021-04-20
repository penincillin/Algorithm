"""
Pascal's Triangle II, https://leetcode.com/problems/pascals-triangle-ii/
The key to only use O(N) space is to update from end to start
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def getRow(self, rowIndex):
        res = [0 for _ in range(rowIndex+1)]
        res[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1): # from end to start
                res[j] = res[j] + res[j-1]
        return res
        


def main():
    sol = Solution()
    rowIndex = 3
    res = sol.getRow(rowIndex)
    print(res)


if __name__ == '__main__':
    main()
