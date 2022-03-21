"""
House Robber, https://leetcode.com/problems/house-robber/
DP
"""

import os, sys, shutil
from collections import defaultdict, Counter
import copy
import pdb
import time


class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        else:
            money = [0 for i in range(n+1)]
            money[0] = 0
            money[1] = nums[0]
            for i in range(2, n+1):
                money[i] = max(money[i-1], money[i-2]+nums[i-1])
            return money[n]


def main():
    sol = Solution()

    nums = [2,7,9,3,1]
    res = sol.rob(nums)
    print(res)


if __name__ == '__main__':
    main()
