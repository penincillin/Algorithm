"""
Find Minimum in Rotated Sorted Array, https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
The basic idea is still binary search
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math
import heapq


class Solution(object):
    def findMin(self, nums):
        return self.solve(nums)
    
    def solve(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            start, end = 0, len(nums)
            while start < end:
                mid = (start + end) // 2
                if nums[mid] == nums[end-1]: # start 0, end 2; start 1, end 3:
                    return min(nums[start], nums[end-1])
                elif nums[mid] < nums[end-1]:
                    if mid==0 or nums[mid] < nums[mid-1]: # mid could be exactly the smallest one.
                        return nums[mid]
                    else:
                        end = mid
                else:
                    start = mid + 1
            return nums[start]
        

def main():
    sol = Solution()
    nums = [1]
    res = sol.findMin(nums)
    print(res)


if __name__ == '__main__':
    main()

