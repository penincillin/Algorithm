"""
Longest Consecutive Sequence, https://leetcode.com/problems/longest-consecutive-sequence/
First straightforward idea is sorting and O(nlogn). Actually can pass the test.
The O(n) solution uses hash table. The key idea is to only stat the head of each segment.
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb


class Solution(object):
    def longestConsecutive(self, nums):
        # return self.solve_sort(nums)
        return self.solve(nums)

    def solve_sort(self, nums):
        # O(nlog)
        nums = sorted(nums)
        res = 0
        mid_res = 0
        cur_num = None

        for num in nums:
            if cur_num is None:
                cur_num = num
                mid_res = 1
            else:
                if num == cur_num+1:
                    mid_res += 1
                    cur_num = num
                elif num == cur_num:
                    continue
                else:
                    cur_num = num
                    mid_res = 1
            res = max(mid_res, res)
        return res
    
    def solve(self, nums):
        # O(n)
        nums = set(nums)
        res = 0
        mid_res = 0
        for num in nums:
            cur_num = num
            if cur_num-1 not in nums:
                mid_res = 1
                while cur_num+1 in nums:
                    cur_num = cur_num + 1
                    mid_res += 1
                res = max(res, mid_res)
        return res
                    

def main():
    sol = Solution()
    nums = [100,4,200,1,3,2]
    # nums = [0,3,7,2,5,8,4,6,0,1]
    # nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    res = sol.longestConsecutive(nums)
    print(res)


if __name__ == '__main__':
    main()
