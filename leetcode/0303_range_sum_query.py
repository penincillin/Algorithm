"""
Range Sum Query - Immutable, https://leetcode.com/problems/range-sum-query-immutable/
Prefix Sum.
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb
from math import sqrt


class NumArray(object):

    def __init__(self, nums):
        N = len(nums)
        self.dp = [0 for i in range(N)]
        res = 0
        for i, num in enumerate(nums):
            self.dp[i] = (res + num)
            res = self.dp[i]
        self.dp = [0,] + self.dp # padding zero to avoid boundary check.
        

    def sumRange(self, left, right):
        res = self.dp[right+1]-self.dp[left]
        return res
        

def main():
    nums = [-2, 0, 3, -5, 2, -1]
    na = NumArray(nums)
    
    res = na.sumRange(0, 2)
    print(res)

    res = na.sumRange(2, 5)
    print(res)

    res = na.sumRange(0, 5)
    print(res)


if __name__ == '__main__':
    main()
