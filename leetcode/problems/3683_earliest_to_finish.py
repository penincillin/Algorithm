"""
"""

from typing import List, Dict
from collections import defaultdict, Counter
import pdb


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = 999999999
        for task in tasks:
            res = min(task[0] + task[1], res)
        return res


def main():
    sol = Solution()
    tasks = [[1,6],[2,3]]
    res = sol.earliestTime(tasks)
    print(res)


if __name__ == '__main__':
    main()
