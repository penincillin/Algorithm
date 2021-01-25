"""
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import copy


class Solution:
    def reverseBits(self, n):
        bits = list()
        for i in range(32):
            bit = n % 2
            n = n // 2
            bits.append(bit)
        bits.reverse()
        res = 0
        high = 1
        for bit in bits:
            res += bit * high
            high *= 2
        return res


def main():
    sol = Solution()
    n = 43261596
    res = sol.reverseBits(n)
    print(res)


if __name__ == '__main__':
    main()
