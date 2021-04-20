"""
Factorial Trailing Zeroes, https://leetcode.com/problems/factorial-trailing-zeroes/
Use brutal way to run from 1 to 100, check 5, 10, 25, 50, 100, 125; the rule is easy to be observed.
"""

import os, sys, shutil


class Solution(object):
    def __fact(self, n):
        if n == 0:
            return 0
        else:
            res = 1
            for i in range(2, n+1):
                res *= i
            return res

    def __num_zero(self, n):
        if n == 0:
            return 1
        else:
            res = 0
            while n > 0:
                tail = n % 10
                n //= 10
                if tail == 0:
                    res += 1
                else:
                    return res

    def solve_brutal(self, n):
        fact = self.__fact(n)
        num_zero = self.__num_zero(fact)
        return fact, num_zero

    def trailingZeroes(self, n):
        res = 0
        cur = 5
        while n // cur > 0:
            res += (n//cur)
            cur *= 5
        return res

def main():
    sol = Solution()

    for i in range(1, 201):
        fact, num_zero = sol.solve_brutal(i)
        res = sol.trailingZeroes(i)
        print(i, num_zero, res)


if __name__ == '__main__':
    main()
