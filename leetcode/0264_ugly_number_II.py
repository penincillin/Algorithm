"""
Ugly Number II, https://leetcode.com/problems/ugly-number-ii/
Use heap and prime number
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def nthUglyNumber(self, n):
        prime_list = [2,3,5]
        nums = [1,]
        res = list()
        heapq.heapify(nums)
        exists = dict()
        for i in range(n):
            cur = heapq.heappop(nums)
            res.append(cur)
            for p in prime_list:
                nnn = cur * p
                if not nnn in exists:
                    heapq.heappush(nums, cur * p)
                    exists[nnn] = 1
        return cur


def main():
    sol = Solution()


if __name__ == '__main__':
    main()
