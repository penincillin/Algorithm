"""
The Skyline Problem, https://leetcode.com/problems/the-skyline-problem/
Check this for solution: https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms
"""

import os, sys, shutil
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
import pdb


class Solution(object):
    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res = [[0, 0]] # [x, height]
        hp = [(0, float("inf"))] # [-height, ending position]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heappop(hp)
            if negH: 
                heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]


def main():
    buildings = [[1,2,3]]

    sol = Solution()
    res = sol.getSkyline(buildings)

 #   print(res)


if __name__ == '__main__':
    main()
