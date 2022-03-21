"""
Bulls and Cows, https://leetcode.com/problems/bulls-and-cows/
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math
import heapq


class Solution(object):
    def getHint(self, secret, guess):

        record = defaultdict(int)
        for c in secret:
            record[c] += 1
        miss_c = defaultdict(int)

        # bulls
        n_b = 0
        for i in range(len(guess)):
            match = False
            c = guess[i]
            if i < len(secret):
                if c == secret[i]:
                    n_b += 1
                    record[c] -= 1
                else:
                    miss_c[c] += 1

        # cows
        n_c = 0
        for c in miss_c:
            n_c += min(miss_c[c], record[c])

        return str(n_b) + "A" + str(n_c) + "B"
        

def main():
    sol = Solution()
    secret="1807"; guess="7810"
    res = sol.getHint(secret, guess)
    print(res)


if __name__ == '__main__':
    main()
