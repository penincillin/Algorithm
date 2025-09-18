"""
Longest Turbulent Subarray, https://leetcode.com/problems/longest-turbulent-subarray/
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        sign = 0
        head, tail = 0, 0
        res = 0
        while tail < n:
            if tail-head == 0:
                res = max(res, 1)
                tail += 1
            else:
                diff = arr[tail]-arr[tail-1]
                if diff == 0: # shouldn't be equal
                    sign = 0
                    head = tail
                else:
                    cur_sign = 1 if diff > 0 else -1
                    if sign == 0 or sign * cur_sign < 0:
                        sign = cur_sign
                        res = max(res, tail-head+1)
                        tail += 1
                    else:
                        sign = cur_sign
                        head = tail-1
                        tail = tail+1
        return res


def main():
    sol = Solution()

    arr = [9,4,2,10,7,8,8,1,9]
    # arr = [100]
    res = sol.maxTurbulenceSize(arr)
    print(res)


if __name__ == '__main__':
    main()
