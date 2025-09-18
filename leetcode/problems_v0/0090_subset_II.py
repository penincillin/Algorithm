"""
Subsets II, https://leetcode.com/problems/subsets-ii/
Since there is duplicate, the key idea is to process integer by integer, instead of number by number.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def subsetsWithDup(self, nums):
        return self.solve(nums)

    def solve(self, nums):
        num_stat = defaultdict(int)
        for num in nums:
            num_stat[num] += 1

        res = [[],]
        for num in num_stat:
            freq = num_stat[num]

            mid_res = list() # suppose we have 3 '1', then the subset composed of '1' is [], [1], [1,1], [1,1,1]
            for i in range(0, freq+1):
                mid_res.append([num,] * i)

            new_res = list()
            for r in res:
                for mr in mid_res:
                    new_res.append(r + mr)
            res = new_res
        return res


def main():
    sol = Solution()
    # nums = [1, 2, 2]
    nums = [1, 1, 2, 2]
    res = sol.subsetsWithDup(nums)
    for num in res:
        print(num)


if __name__ == '__main__':
    main()
