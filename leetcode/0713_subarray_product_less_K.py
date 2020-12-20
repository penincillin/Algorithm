"""
Subarray Product Less Than K, https://leetcode.com/problems/subarray-product-less-than-k/
Using sliding window to stat, the key is to add result for each valid end
"""

import os, sys, shutil
from collections import defaultdict


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        N = len(nums)
        if N == 0:
            return 0
        else:
            start, end = 0, 1
            product = nums[0]
            res = 0
            while(end < N):
                if product < k and start < end:
                    res += (end-start) # instead of 1
                if (product < k or start == end):
                    product *= nums[end]
                    end += 1
                else:
                    if start < end:
                        product /= nums[start]
                        start += 1
            while(start < end):
                if product < k:
                    res += (end-start)
                    break
                else:
                    product /= nums[start]
                    start += 1
            return res

def main():
    nums = [10, 5, 2, 6]; K = 100
    #nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]; K = 19

    sol = Solution()
    res = sol.numSubarrayProductLessThanK(nums, K)
    #res = sol.brutal_force(nums, K)
    print(res)


if __name__ == '__main__':
    main()
