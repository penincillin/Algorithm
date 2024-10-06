"""
Count Primes, https://leetcode.com/problems/count-primes/
Use Sieve algorithm: https://oi-wiki.org/math/sieve/
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math


class Solution(object):
    def countPrimes(self, n):
        is_prime = [True for i in range(n)]
        # is_prime[1] = False

        upper_bound = min(int(math.sqrt(n))+1, n)
        for i in range(2, upper_bound):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        res = 0
        for i in range(2, n):
            if is_prime[i]:
                res += 1
        return res


def main():
    sol = Solution()
    n = 1
    res = sol.countPrimes(n)
    print(res)


if __name__ == '__main__':
    main()
