"""
Compare Version Numbers, https://leetcode.com/problems/compare-version-numbers/
The only challenge of this problem lies in handle different details.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def compareVersion(self, version1, version2):
        nums1 = list(map(int, version1.split('.')))
        nums2 = list(map(int, version2.split('.')))
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(n1):
            if i >= n2:
                if nums1[i] > 0: # consider 1.0 & 1. In this case, the algorithm go to line 33
                    return 1
            else:
                if nums1[i] < nums2[i]:
                    return -1
                elif nums1[i] > nums2[i]:
                    return 1
                else: # nums[n1] == nums[n2]
                    pass
        if n1 < n2:
            for i in range(n1, n2):
                if nums2[i] > 0: # consider 1 1.0.0, In this case, the algorithm goes to line 31
                    return -1
            return 0
        else:
            return 0


def main():
    sol = Solution()
    version1="1"; version2="1.1"
    res = sol.compareVersion(version1, version2)
    print(res)


if __name__ == '__main__':
    main()
