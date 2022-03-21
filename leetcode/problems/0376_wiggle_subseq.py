"""
Range Sum Query 2D - Immutable, https://leetcode.com/problems/range-sum-query-2d-immutable/
DP solution also requires proof (for each dp[j], it should both considers positive and negative cases).
Greedy solution is right, but it also requires proof to get this answer.
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb
from math import sqrt


class Solution(object):
    def wiggleMaxLength(self, nums):
        return self.solve_greedy(nums)
    
    def get_symbol(self, num):
        if num == 0:
            return 0
        elif num < 0:
            return -1
        else:
            return 1

    def solve_dp(self, nums):
        # O(n^2)
        N = len(nums)
        dp = [(1, 0) for i in range(N)] # dp[i] means mid results use nums[i]
        res = 1
        for i in range(1, N):
            mid_res, mid_sym = 0, 0
            for j in range(0, i):
                prev_res, prev_sym = dp[j]
                tmp_sym = self.get_symbol(nums[j]-nums[i])
                if tmp_sym != 0 and tmp_sym != prev_sym and prev_res+1 > mid_res:
                    mid_res = prev_res+1
                    mid_sym = tmp_sym
            dp[i] = (mid_res, mid_sym)
            res = max(mid_res, res)
        return res
    
    def solve_greedy(self, nums):
        if len(nums) < 2:
            return len(nums)
        else:
            prev_sym = self.get_symbol(nums[0]-nums[1])
            res = 2 if prev_sym != 0 else 1
            for i in range(2, len(nums)):
                cur_sym = self.get_symbol(nums[i-1]-nums[i])
                if (cur_sym>0 and prev_sym<=0) or (cur_sym<0 and prev_sym>=0):
                    res += 1
                    prev_sym = cur_sym
            return res



def main():
    sol = Solution()


if __name__ == '__main__':
    main()
