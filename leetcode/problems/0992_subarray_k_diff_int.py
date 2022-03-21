"""
Subarrays with K Different Integers, https://leetcode.com/problems/subarrays-with-k-different-integers/
The idea of two sliding windows, refer to this solution: https://leetcode.com/problems/subarrays-with-k-different-integers/solution/
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def subarraysWithKDistinct(self, nums, K):
        N = len(nums)
        p0, p1 = 0, 0
        rec0, rec1 = defaultdict(int), defaultdict(int)
        valid0, valid1 = 0, 0
        res = 0
        
        for num in nums:
            # rec0
            rec0[num] += 1
            if rec0[num] == 1:
                valid0 += 1
            # rec1
            rec1[num] += 1
            if rec1[num] == 1:
                valid1 += 1

            while valid0 > K and p0 < N:
                rec0[nums[p0]] -= 1
                if rec0[nums[p0]] == 0:
                    valid0 -= 1
                p0 += 1

            while valid1 >= K and p1 < N:
                rec1[nums[p1]] -= 1
                if rec1[nums[p1]] == 0:
                    valid1 -= 1
                p1 += 1

            res += (p1-p0)

        return res


def main():
    A = [1, 2, 1, 2, 3]
    k = 2

    sol = Solution()
    res = sol.subarraysWithKDistinct(A, k)
    print(res)


if __name__ == '__main__':
    main()
