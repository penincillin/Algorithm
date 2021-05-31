"""
Decode String, https://leetcode.com/problems/decode-string/
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math


class Solution(object):
    def decodeString(self, s):
        return self.solve(s)

    def solve(self, s):
        stack_s = list()
        stack_n = list()
        cur_n = 0
        cur_s = ''
        for c in s:
            if c.isdigit():
                cur_n = cur_n*10 + int(c)
            elif c == '[':
                stack_s.append(cur_s)
                stack_n.append(cur_n)
                cur_s = ''
                cur_n = 0
            elif c == ']':
                prev_n = stack_n.pop()
                prev_s = stack_s.pop()
                cur_s = prev_s + prev_n * cur_s
            else:
                cur_s += c

        stack_s.append(cur_s) # push the last s
        res = ''.join(stack_s)
        return res


def main():
    sol = Solution()
    s = "3[2[a]]"
    # s = "2[3[a]]"
    # s = "3[2[c]b1[a]]"
    #s = "2[j]e1[f]"
    # s = "2[y]pq4[2[j]e1[f]]"
    # s = "2[2[y]pq4[2[j]e1[f]]]"
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    # s = "2[abc]3[cd]ef"
    # s = "c3[b2[a]]"
    # s = "c3[2[a]]"
    # s = "3[acb]"
    # s = "3[a2[c]]"
    res = sol.decodeString(s)
    print(res)


if __name__ == '__main__':
    main()
