"""
https://leetcode.com/problems/smallest-absent-positive-greater-than-average/description/
"""

from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import pdb


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        return self.solve(nums)

    def solve(self, nums: List[int]) -> int:
        exists = {}
        tot = 0
        for num in nums:
            tot += num
            if num > 0:
                exists[num] = True
    
        ave = tot / len(nums)
        res = max(int(ave) + 1, 1)
        while True:
            if res not in exists:
                break
            else:
                res += 1
        return res


def main():
    sol = Solution()

    # nums = [3,5]
    nums = [-1,1,2]
    res = sol.smallestAbsent(nums)
    print(res)


if __name__ == '__main__':
    main()
