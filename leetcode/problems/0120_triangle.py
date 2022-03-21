"""
Triangle, https://leetcode.com/problems/triangle/
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0
        else:
            mid_res = [triangle[0][0]]
            N = len(triangle)
            for i in range(1, N):
                row = triangle[i]
                new_res = list()
                for j in range(i+1):
                    j0 = j-1
                    j1 = j
                    left = mid_res[j0] if j0>=0 else float('inf')
                    right = mid_res[j1] if j1<len(mid_res) else float('inf')
                    left += row[j]
                    right += row[j]
                    new_res.append(min(left, right))
                mid_res = new_res
            res = float('inf')
            for r in mid_res:
                res = min(r, res)
            return res


def main():
    sol = Solution()
    
    # triangle = [[2],[3,4]]
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    res = sol.minimumTotal(triangle)
    print(res)


if __name__ == '__main__':
    main()
