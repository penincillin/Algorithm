"""
Remove Duplicate Letters, 
Start from a simple example "bcabc" and use stack
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def removeDuplicateLetters(self, s):
        # init
        stat = defaultdict(int)
        used = dict()
        for c in s:
            stat[c] += 1
            used[c] = False

        stack = list()
        for c in s:
            stat[c] -= 1
            if not used[c]:
                while(len(stack)>0 and stack[-1]>c and stat[stack[-1]]>0):
                    used[stack[-1]] = False
                    stack.pop()
                used[c] = True
                stack.append(c)

        res = ''.join(stack)
        return res


def main():
    sol = Solution()
    s = "cdadabcc"
    # s = "cbacdcbc"
    res = sol.removeDuplicateLetters(s)
    print(res)


if __name__ == '__main__':
    main()
