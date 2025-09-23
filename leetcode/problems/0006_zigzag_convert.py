"""
https://leetcode.com/problems/zigzag-conversion/description/
Write down some example and check the law carefully.
Suppose there are 4 rows, the law is
1st row: 0, +6,    +6, ...
2nd row: 1, +4,+2, +4,+2, ...
3nd row: 2, +2,+4, +2,+4, ...
4th row: 0, +6,    +6, ...
"""

from typing import List, Dict, Tuple, Optional
from collections import defaultdict, Counter
import pdb


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return self.solve(s, numRows)
        
    def solve(self, s: str, numRows: int) -> str:
        N = len(s)
        interval = max((numRows - 1) * 2, 1) # when numRows=1, the interval should be 1, w/o max(...), it will be 0
        res = []
        for start in range(numRows):
            cur = start
            if cur < N: # corner case: s = "A", numRows = 2
                delta1 = start * 2
                delta0 = interval - delta1
                res.append(s[cur])
                while cur < N:
                    for delta in (delta0, delta1):
                        cur += delta
                        if delta > 0 and cur < N: # don't add 0
                            res.append(s[cur])
        res = "".join(res)
        return res


def main():
    # s = "PAYPALISHIRING"; numRows = 4
    s = "A"; numRows = 2
    sol = Solution()
    res = sol.convert(s, numRows)
    print(res)


if __name__ == '__main__':
    main()