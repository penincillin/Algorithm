"""
H-Index, https://leetcode.com/problems/h-index/
O(nlogn) is straightforward. The o(n) method, should start from tail to head
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math
import heapq


class Solution(object):
    def hIndex(self, citations):
        return self.solve_hash(citations)

    def solve_sort(self, citations):
        cites = sorted(citations)
        N = len(cites)
        res = 0
        for i, c in enumerate(cites):
            mid_res = min(c, N-i)
            res = max(mid_res, res)
        return res
    
    def solve_hash(self, cites):
        N = len(cites)
        record = [0 for _ in range(N)]
        for c in cites:
            if c<N and c>0:
                record[c-1] += 1
            elif c>=N:
                record[N-1] += 1
            else: # c <= 0
                pass

        count = 0
        for i in range(N-1, -1, -1):
            count += record[i]
            if count >= i+1:
                return i+1
        return 0



def main():
    sol = Solution()
    citations = [3,0,6,1,5]
    res = sol.hIndex(citations)
    print(res)


if __name__ == '__main__':
    main()
