"""
Search in Rotated Sorted Array, https://leetcode.com/problems/search-in-rotated-sorted-array/
The key idea is to abondan half each time, so that the overall time complexity is still O(logN)
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def search(self, nums, target):
        N = len(nums)
        return self.solve(nums, target, 0, N)

    def bin_search(self, nums, target, head, tail):
        while head < tail:
            mid = (head+tail)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]<target:
                    head = mid+1
                else:
                    tail = mid
        return -1
    
    def solve(self, nums, target, head, tail):
        if tail-head < 1:
            return -1
        elif tail-head == 1:
            return head if nums[head]==target else -1
        else:
            mid = (head+tail)//2
            # print('mid', mid, nums[mid], target)
            if nums[mid] == target:
                return mid
            else:
                # check whether left-part is sorted
                if head<mid and head>=0 and nums[head] <= nums[mid-1]:
                    # if it is and the target lies in it, then it can only be found in left part
                    if nums[head]<=target and nums[mid-1]>=target:
                        return self.bin_search(nums, target, head, mid)
                    # otherwise, check the right part
                    else:
                        return self.solve(nums, target, mid+1, tail)
                # if left-part is not sorted, then right part must be sorted
                else:
                    # similar to left ...
                    if nums[mid+1]<=target and nums[tail-1]>=target:
                        return self.bin_search(nums, target, mid+1, tail)
                    else:
                        return self.solve(nums, target, head, mid)


def main():
    # nums = [4,5,6,7,0,1,2]; target = 0
    # nums = [4,5,6,7,0,1,2]; target = 3
    # nums = [1, 3]; target = 3
    # nums = [7,8,1,2,3,4,5,6]; target = 2
    sol = Solution()
    res = sol.search(nums, target)
    print(res)


if __name__ == '__main__':
    main()
