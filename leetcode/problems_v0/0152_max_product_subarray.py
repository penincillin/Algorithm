"""
Maximum Product Subarray, https://leetcode.com/problems/maximum-product-subarray/
Brutal force O(N^3) and DP O(N^2) will all lead to time exceed limit.
The O(N) solution is a little bit tricky. It requires to simultaneously maintain max / min value and exchange them when encounter negative value.
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb


class Solution(object):
    def maxProduct(self, nums):
        return self.solve_dp(nums)

    def solve(self, nums):
        # tricky solution, 
        res = nums[0]
        cur_max, cur_min = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(cur_max*nums[i], nums[i])
            cur_min = min(cur_min*nums[i], nums[i])
            res = max(cur_max, res)
        return res
    
    def solve_dp(self, nums):
        # DP, O(N^2)
        N = len(nums)
        dp = [[0 for j in range(N)] for i in range(N)]
        res = float('-inf')
        for i in range(N):
            dp[i][i] = nums[i]
            res = max(res, dp[i][i])

        for l in range(2, N+1):
            for i in range(N):
                j = i+l-1
                if j < N:
                    if j-1 >= 0:
                        dp[i][j] = dp[i][j-1] * nums[j] 
                    else:
                        dp[i][j] = dp[i+1][j] * nums[i]
                    res = max(res, dp[i][j])

        return res
    

def main():
    sol = Solution()
    # nums = [100,4,200,1,3,2]
    # nums = [2,3,-2,4]
    # nums = [-2,0,-1]
    nums = [2,-5,-2,-4,3]
    res = sol.maxProduct(nums)
    print(res)


if __name__ == '__main__':
    main()
