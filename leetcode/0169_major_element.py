"""
Majority Element, https://leetcode.com/problems/majority-element/
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def majorityElement(self, nums):
        record = defaultdict(int)
        N = len(nums)
        thresh = N//2 if N%2==0 else N//2+1
        for num in nums:
            record[num] += 1
            if record[num] == thresh:
                return num


def main():
    nums = [3, 2, 3]

    sol = Solution()
    res = sol.majorityElement(nums)
    print(res)


if __name__ == '__main__':
    main()
