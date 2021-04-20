"""
Rectangle Area, https://leetcode.com/problems/rectangle-area/
The idea is to calculate as area1 + area2 - overlap. The key lies in how to obtain overlap. The whole can be divied into two cases:
    1) No overlap.
    2) Exist overlap, then the area can be calculated as line 31 ~ 33.
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        rec1 = (A,B,C,D) # (x0, y0, x1, y1)
        rec2 = (E,F,G,H) # (x0, y0, x1, y1)

        # set leftmost rect to be rec1
        if rec1[0] > rec2[0]:
            rec2, rec1 = rec1, rec2

        area1 = (rec1[2]-rec1[0]) * (rec1[3]-rec1[1])
        area2 = (rec2[2]-rec2[0]) * (rec2[3]-rec2[1])

        # two rects have no overlaps. 
        if rec1[2] <= rec2[0] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1]:
            overlap_area = 0
            return area1 + area2
        else:
            xs = sorted([rec1[0], rec1[2], rec2[0], rec2[2]])
            ys = sorted([rec1[1], rec1[3], rec2[1], rec2[3]])
            overlap_area = (xs[2]-xs[1]) * (ys[2]-ys[1])
        
        res = area1 + area2 - overlap_area
        return res


def main():
    sol = Solution()
    # A=-3; B=0; C=3; D=4; E=0; F=-1; G=9; H = 2
    A=-2; B=-2; C=2; D=2; E=-2; F=-2; G=2; H=2
    res = sol.computeArea(A, B, C, D, E, F, G, H)
    print(res)


if __name__ == '__main__':
    main()
