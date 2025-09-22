"""
https://leetcode.com/problems/minimum-discards-to-balance-inventory/description/
Sliding window
"""

from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import pdb


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        return self.solve(arrivals, w, m)

    def solve(self, arrivals: List[int], w: int, m: int) -> int:
        head = 0

        avals = arrivals
        n = len(arrivals)
        counts = defaultdict(int)
        discards = dict() # which day was discard

        for tail in range(0, n):
            if tail - head == w:
                # shift window
                if head not in discards:
                    val_h = avals[head]
                    counts[val_h] -= 1
                head += 1

            # extend tail
            val_t = avals[tail]
            if counts[val_t] >= m:
                discards[tail] = True
            else:
                counts[val_t] += 1
        
        discard = sum([1 for key in discards])
            
        return discard


def main():
    sol = Solution()

    # arrivals = [1,2,1,3,1]; w = 4; m = 2
    arrivals = [1,2,3,3,3,4]; w = 3; m = 2

    res = sol.minArrivalsToDiscard(arrivals, w, m)
    print(res)


if __name__ == '__main__':
    main()
