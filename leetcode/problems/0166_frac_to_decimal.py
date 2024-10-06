"""
Fraction to Recurring Decimal, https://leetcode.com/problems/fraction-to-recurring-decimal/
"""

import os, sys, shutil


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        sign = '-' if numerator*denominator < 0 else '+'
        if sign == '-':
            res = [sign,]
        else:
            res = []

        numerator = abs(numerator)
        denominator = abs(denominator)
        n, m = divmod(numerator, denominator)
        res.append(str(n))

        if m > 0:
            res.append('.')
            dot_idx = len(res)
            appear = dict()
            # loop
            while m not in appear and m > 0:
                appear[m] = len(res)
                n, m = divmod(m*10, denominator)
                res.append(str(n))
            if m > 0:
                idx = appear[m]
                res.insert(idx, '(')
                res.insert(len(res), ')')

        return ''.join(res)


def main():
    sol = Solution()
    numerator, denominator = 1314, -9999
    #numerator, denominator = 4,333 
    res = sol.fractionToDecimal(numerator, denominator)
    print(res)


if __name__ == '__main__':
    main()

