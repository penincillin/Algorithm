"""
Bitwise AND of Numbers Range, https://leetcode.com/problems/bitwise-and-of-numbers-range/
The idea is to convert m and n to bits, for example m,n=5,7, bits_m = [1,0,1,0], bits_n = [1,1,1,0] (from left to right).
Then from lower to higher, compare bit of m and bit of n, if they are not both 1, then this bit will be 0 without doubt.
If both bits are 1, then we check whether there will be 0 from m to n in this position, the way to check it is to compare whether 2^pos >= (n-m+1).
if that does not hold, the bit in this position will definitely flipped.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import copy


class Solution(object):
    def get_bits(self, n):
        bits = list()
        for i in range(32):
            bit = n % 2
            n = n // 2
            bits.append(bit)
        return bits

    def rangeBitwiseAnd(self, m, n):
        bits_m = self.get_bits(m)
        bits_n = self.get_bits(n)
        diff = n - m + 1
        high = 1
        res = 0
        for i in range(32):
            bit = 0
            if bits_m[i]==1 and bits_n[i]==1:
                if high >= diff:
                    bit = 1
            res += bit * high
            high *= 2
        return res
                


def main():
    sol = Solution()
    m, n = 5, 7
    res = sol.rangeBitwiseAnd(m, n)
    print(res)


if __name__ == '__main__':
    main()
