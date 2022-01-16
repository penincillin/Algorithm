"""
Implement Rand10() Using Rand7(), https://leetcode.com/problems/implement-rand10-using-rand7/
Extend 7 to 49 (7 * 7) and only keep the mod 10 part. (1 ~ 40)
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb
import numpy as np


def rand7():
    return np.random.randint(1, 8)


class Solution(object):
    def rand10(self):
        success = False
        while not success:
            num1 = rand7()
            num2 = rand7()
            num = num1 + (num2-1)*7

            if num <= 40:
                res = num // 4
                res = 10 if res==0 or res==10 else res
                return res
        

def main():
    sol = Solution()

    total = 100000
    stat = defaultdict(int)
    for i in range(total):
        randn = sol.rand10()
        stat[randn] += 1

    for i in sorted(stat.keys()):
        print(i, stat[i]/total)


if __name__ == '__main__':
    main()
