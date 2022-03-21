"""
Gray Code, https://leetcode.com/problems/gray-code/
Say for have n = 2, we want to get n = 3; Then we can fix the first digit to be zero and traverse [00, 01, 11, 10]
000
001
011
010.
Then we can change the first digit to 1 and, traverse n = 2 result in reverse order, [10, 11, 01, 00]
110
011
101
100
In this way, the requirement (only 1 digit diff always hold)
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def grayCode(self, n):
        return self.solve(n)

    def get_first(self, n):
        res = 1
        for i in range(n-1):
            res *= 2
        return res

    def solve(self, n):
        if n == 0:
            return [0,]
        elif n == 1:
            return [0, 1]
        else:
            nums = self.solve(n-1)
            res = list()
            add = self.get_first(n)
            for num in nums:
                res.append(num) # 0 + num
            for num in nums[::-1]: # 1 + num, but traverse from tail to head
                res.append(add + num)
            return res


def main():
    sol = Solution()
    n = 3
    res = sol.grayCode(n)
    print(res)


if __name__ == '__main__':
    main()
