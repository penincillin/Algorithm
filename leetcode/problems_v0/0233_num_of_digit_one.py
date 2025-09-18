"""
First solve 1, 10, 100 ...
Then solve normal numbers, check the code for details, the idea is divide and analysis && DP.
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math


class Solution(object):

    def solve_10(self, n):
        # solve results for 1, 10, 100
        mid_res = self.record[n//10] # results for n//10
        res = 1 # 1 digit in 100
        res += 8 * (mid_res - 1) # 99 to 20
        res += n//10 # 19 -> 10 has 10 numbers, each has 1 digit
        res += mid_res - 1 # additional 1 digit in 11 (the first 1 has been considered line above)
        res += mid_res - 1 # results for 0 to 9
        return res

    def solve(self, n):
        if n in self.record:
            return self.record[n]
        else:
            digits = [int(c) for c in str(n)]
            d0 = digits[0]
            if d0 == 1:
                # for example, 121
                next_num = int(str(n)[1:]) if len(digits)>1 else 0 # 21
                mid_res = self.solve(10 ** (len(digits)-1)) - 1 # consider number of 1 in 0~99
                res = next_num + 1 # consider 0~21, 100, 101, ... 121
                res += self.solve(next_num) # consider number of 1 in 0~21
                res += mid_res # 0~99
            else:
                # for example 421
                next_num = int(str(n)[1:]) if len(digits)>1 else 0 # 21
                mid_res = self.solve(10 ** (len(digits)-1)) - 1 # consider number of 1 in 0~99
                res = self.solve(next_num) # 400 ~ 421
                res += (d0-2) * mid_res # 300~399, 200~299
                res += 10 ** (len(digits)-1) # 199 ~ 100, only consider first 1
                res += mid_res # 100~199, neglecting the first 1
                res += mid_res # 0~99

            self.record[n] = res
            return res


    def build_ref(self, n):
        # build record table for results 1, 10, 100 ..
        self.record = dict()
        self.record[0] = 0
        self.record[1] = 1

        cur = 1
        num_digit = len(str(n))
        for i in range(1, num_digit):
            cur = cur * 10
            res = self.solve_10(cur)
            self.record[cur] = res


    def countDigitOne(self, n):
        self.build_ref(n)
        return self.solve(n)
   

def main():
    sol = Solution()
    n = 19
    res = sol.countDigitOne(n)
    print(res)


if __name__ == '__main__':
    main()
