"""
House Robber II, https://leetcode.com/problems/house-robber-ii/
DP, similar to House Robber (https://leetcode.com/problems/house-robber/), the only difference is the constrain on circle.
To solve this, just divide the whole program into two cases, use the first element and do not use the first element.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import copy
import pdb
import time


class Solution(object):
    def solve(self, nums): # without consider the constrain of circle
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
    
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        else:
            res1 = self.solve(nums[1:])
            res2 = self.solve(nums[2:-1]) + nums[0]
            return max(res1, res2)


def main():
    sol = Solution()

    # nums = [2,7,9,3,1]
    # nums = [2, 3, 2]
    nums = [1,]
    res = sol.rob(nums)
    print(res)


if __name__ == '__main__':
    main()
