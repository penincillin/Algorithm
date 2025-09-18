"""
Sliding Window Maximum, https://leetcode.com/problems/sliding-window-maximum/
The key is to use deque and update deque according to the value comparison.
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
import pdb


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        return self.solve(nums, k)

    def solve(self, nums, k):
        dq = deque()
        res = list()
        for idx, num in enumerate(nums):
            while len(dq) > 0 and nums[dq[-1]] <= num: # from tail to head, only keep the large value
                dq.pop()
            dq.append(idx)

            if dq[0] == idx-k: # remove the invalid value
                dq.popleft()

            if idx >= k-1:
                res.append(nums[dq[0]]) # the left-most value would always be the current largest value
        return res


def main():
    nums = [1,3,-1,-3,5,3,6,7]; k = 3
    sol = Solution()
    res = sol.maxSlidingWindow(nums, k)
    print(res)


if __name__ == '__main__':
    main()
