"""
Single Number,https://leetcode.com/problems/single-number/ 
use xor operation, 
0 xor 0 = 0
0 xor 1 = 1
1 xor 0 = 1
1 xor 1 = 0
therefore, 
a xor 0 = a
a xor a = a
"""

import os, sys, shutil
from collections import defaultdict


class Solution(object):
    def singleNumber(self, nums):
        return self.solve_2(nums)


    def solve_1(self, nums):
        record = defaultdict(int)
        for n in nums:
            record[n] += 1

        for n in record:
            if record[n] == 1:
                return n


    def solve_2(self, nums):
        res = 0
        for n in nums:
            res ^= n
        return res


def main():
    nums = [2, 2, 1]
    sol = Solution()
    res = sol.singleNumber(nums)
    print(res)


if __name__ == '__main__':
    main()
