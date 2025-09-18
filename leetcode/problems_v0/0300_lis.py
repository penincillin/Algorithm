"""
Longest Increasing Subsequence, https://leetcode.com/problems/longest-increasing-subsequence/
The key lies in how to define the state transition. DP[i] means the LIS that ends with nums[i] (must include nums[i])
"""
import os, sys, shutil
import pdb


class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        else:
            dp = [1 for _ in nums]
            res = 1 
            N = len(nums)
            for i in range(N):
                mid_res = 1
                for j in range(i):
                    if nums[j] < nums[i]:
                        mid_res = max(dp[j] + 1, mid_res)
                dp[i] = mid_res
                res = max(res, mid_res)
            return res


def main():
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    #nums = [10,9,2,5]
    #nums = [10,]
    res = sol.lengthOfLIS(nums)
    print(res)


if __name__ == '__main__':
    main()
