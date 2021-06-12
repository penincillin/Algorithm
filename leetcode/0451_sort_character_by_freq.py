"""
Sort Characters By Frequency, https://leetcode.com/problems/sort-characters-by-frequency/
Straight-forward idea is to use sort with O(nlong) time complexity.
A faster idea is to use bucket sort, since there will be only len(s)
"""

import os, sys, shutil
from collections import defaultdict, Counter
import heapq
import pdb


class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        count_sort = sorted(count.items(), key=lambda a:a[1], reverse=True)
        res = ""
        for c, num in count_sort:
            res += c*num
        return res
        

def main():
    sol = Solution()
    s  = "tree"
    res = sol.frequencySort(s)
    print(res)


if __name__ == '__main__':
    main()
