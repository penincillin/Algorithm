"""
Number of 1 Bits, https://leetcode.com/problems/number-of-1-bits/
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import copy


class Solution(object):
    def hammingWeight(self, n):
        count = 0
        for i in range(32):
            bit = n % 2
            n = n // 2
            count += (bit==1)
        return count


def main():
    sol = Solution()
    n = 11
    res = sol.hammingWeight(n)
    print(res)


if __name__ == '__main__':
    main()
