"""
Super Ugly Number, https://leetcode.com/problems/super-ugly-number/
Use heap and prime number
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        # prime_list = [2,3,5]
        primes = sorted(primes)
        nums = [1,]
        res = list()
        heapq.heapify(nums)
        exists = dict()
        for i in range(n):
            cur = heapq.heappop(nums)
            res.append(cur)
            for p in primes:
                nnn = cur * p
                if not nnn in exists:
                    heapq.heappush(nums, cur * p)
                    exists[nnn] = 1
        return cur


def main():
    n = 12
    primes = [2,7,13,19]
    sol = Solution()
    res = sol.nthSuperUglyNumber(n, primes)
    print(res)


if __name__ == '__main__':
    main()
