"""
Happy Number, https://leetcode.com/problems/happy-number/
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb


class Solution(object):
    def num2digits(self, n):
        if n == 0:
            return [0,]
        else:
            digits = list()
            while (n > 0):
                d = n % 10
                n = n // 10
                digits.append(d)
            return digits


    def isHappy(self, n):
        appear = dict()
        while n not in appear:
            appear[n] = 1
            digits = self.num2digits(n)
            n = sum(d**2 for d in digits)
            if n == 1:
                return True
        return False


def main():
    sol = Solution()
    n = 2
    res = sol.isHappy(n)
    print(res)


if __name__ == '__main__':
    main()
