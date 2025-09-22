"""
"""

from typing import List, Dict
from collections import defaultdict, Counter
import pdb


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(list(set(nums)))[::-1]
        return nums[:k]


def main():
    sol = Solution()
    nums, k = [84,93,100,77,90], 3
    res = sol.maxKDistinct(nums, k)
    print(res)


if __name__ == '__main__':
    main()
