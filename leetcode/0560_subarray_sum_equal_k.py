"""
"""

import os, sys, shutil
from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        record = defaultdict(int)
        record[0] = 1 # padding 0
        sums = 0
        res = 0
        for i, num in enumerate(nums):
            sums += num
            if sums-k in record:
                res += record[sums-k]
            record[sums] += 1
        return res


def main():
    nums = [1,1,1]; k = 2

    sol = Solution()
    res = sol.subarraySum(nums, k)
    print(res)


if __name__ == '__main__':
    main()
