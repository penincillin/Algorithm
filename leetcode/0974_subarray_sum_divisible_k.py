"""
Subarray Sums Divisible by K, https://leetcode.com/problems/subarray-sums-divisible-by-k/
Prefix Sum and Hash Table. This problem is a little bit
"""

import os, sys, shutil
from collections import defaultdict


class Solution(object):
    def subarraysDivByK(self, A, K):
        record = defaultdict(int)
        record[0] = 1
        res = 0
        sums = 0
        for num in A:
            sums += num
            mode = sums % K
            res += record[mode] # if sub_sum[i, j] % K == 0, then (sub_sum[0, i]%K) == (sub_sum[0, j]%K)
            record[mode] += 1
        return res


def main():
    A = [4,5,0,-2,-3,1]; K = 5

    sol = Solution()
    res = sol.subarraysDivByK(A, K)
    print(res)


if __name__ == '__main__':
    main()
