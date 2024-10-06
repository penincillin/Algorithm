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
    def findPeakElement(self, nums):
        return self.solve(nums)
    
    def solve(self, nums):
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            left_peak = (mid>0 and nums[mid]>nums[mid-1]) or mid==0
            right_peak = (mid+1<end and nums[mid]>nums[mid+1]) or mid+1==end
            if left_peak and right_peak:
                return mid
            elif left_peak and not right_peak:
                # e.g. [... 1, 2, 3 ...], if can be easily improved that there must exist a peak in right half 
                # if the array keep increasing from 3, then the last element is the peak
                # else, the point the array start to decrease is the peak
                # it's also possible that the left half also exist a peak, but this cannot be guaranted.
                start = mid+1
            else: # similar to above
                end = mid 
        return start        


def main():
    sol = Solution()
    nums = [1]
    res = sol.findMin(nums)
    print(res)


if __name__ == '__main__':
    main()

