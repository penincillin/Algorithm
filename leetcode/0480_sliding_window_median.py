"""
Sliding Window Median, https://leetcode.com/problems/sliding-window-median/
Similar to No.295, Find Median from Data Stream, The difference is that it requires delete, so using heap might not be optimal.
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def get_median(self, win, k):
        if k%2==1:
            return win[k//2]
        else:
            return (win[k//2] + win[k//2-1]) / 2.0

    def get_idx(self, win, num):
        head, tail = 0, len(win)
        while(head < tail):
            mid = (head + tail) // 2
            if win[mid] < num:
                head = mid + 1
            else:
                tail = mid
        return head
        
    def medianSlidingWindow(self, nums, k):
        return self.solve_bin_search(nums, k)

    def solve_bin_search(self, nums, k)
        win = list()
        for i in range(k):
            win.append(nums[i])
        win = sorted(win)

        n = len(nums)
        res = list()
        for i in range(n-k+1):
            res.append(self.get_median(win, k))
            if i+k < n:
                idx1 = self.get_idx(win, nums[i])
                win.pop(idx1)
                idx2 = self.get_idx(win, nums[i+k])
                win.insert(idx2, nums[i+k])
        return res


def main():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    sol = Solution()
    res = sol.medianSlidingWindow(nums, k)
    print(res)


if __name__ == '__main__':
    main()
