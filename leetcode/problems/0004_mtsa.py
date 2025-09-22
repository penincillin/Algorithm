"""
"""

from typing import List, Dict
from collections import defaultdict, Counter
import pdb


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return self.solve_recursive(nums1, nums2)
        return self.solve_linear(nums1, nums2)
    
    def solve_linear(self, nums1: List[int], nums2: List[int]) -> float:
        """
        linear scan the sequence to find the target
        """
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            tgts = [(m + n) // 2 + 1]
        else:
            tgts = [
                (m + n) // 2,
                (m + n) // 2 + 1,
            ]
        
        inf = 9999999999999
        val1, val2 = inf, inf
        i1, i2, k = 0, 0, 0
        vals = []

        while(len(tgts) > 0):
            if i1 <= m-1:
                val1 = nums1[i1]
            else:
                val1 = inf
            if i2 <= n-1:
                val2 = nums2[i2]
            else:
                val2 = inf

            # select (k+1)-th value
            cur = inf
            if val1 <= val2:
                i1 += 1
                cur = val1
            else:
                i2 += 1
                cur = val2
            k += 1

            if tgts[0] == k:
                vals.append(cur)
                tgts = tgts[1:]
        
        return sum(vals) / len(vals)

    
    def solve_recursive(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (n + m) % 2 == 1:
            idx = (n + m) // 2 + 1
            res = self.findK(nums1, nums2, idx)
            return res
        else:
            idx0 = (n + m) // 2
            idx1 = (n + m) // 2 + 1
            res0 = self.findK(nums1, nums2, idx0)
            res1 = self.findK(nums1, nums2, idx1)
            return (res0 + res1) / 2

    def findK(self, nums1: List[int], nums2: List[int], k: int) -> float:
        """
        k starts from 1, not 0
        """
        # make sure nums1 <= nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            return self.findK(nums1, nums2, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])

        m, n = len(nums1), len(nums2)
        i1 = min(k // 2, m)
        i2 = k - i1
        # print(i1, i2, k, m, n)

        if nums1[i1-1] == nums2[i2-1]:
            return nums1[i1-1]
        elif nums1[i1-1] < nums2[i2-1]:
            return self.findK(nums1[i1:], nums2, k-i1)
        else:
            return self.findK(nums1, nums2[i2:], k-i2)


def main():
    sol = Solution()
    # nums1, nums2 = [1, 2, 3], [4, 5, 6]
    nums1, nums2 = [10], [4, 5, 6]
    res = sol.findMedianSortedArrays(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
