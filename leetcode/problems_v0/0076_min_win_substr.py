"""
Minimum Window Substring, https://leetcode.com/problems/minimum-window-substring/
The key idea is to use the varying size sliding window with head and tail keep change.
"""

import os, sys, shutil
import copy
from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        return self.solve_02(s, t)


    def solve_02(self, s, t):
        N = len(s)
        M = len(t)

        if N == 0 or M == 0:
            return ""
        else:
            t_info = defaultdict(int)
            for c in t:
                t_info[c] += 1

            res = ""
            record = defaultdict(int)
            count = 0
            head, tail = 0, 0

            while(tail < N):
                while(tail < N and count<M):
                    c = s[tail]
                    if t_info[c] > 0:
                        record[c] += 1
                        if record[c] <= t_info[c]:
                            count += 1
                    tail += 1

                if count == M:
                    while(head < tail):
                        c = s[head]
                        head += 1
                        if t_info[c] > 0:
                            record[c] -= 1
                            if record[c] < t_info[c]:
                                count -= 1
                                break

                    tmp_res = s[head-1:tail]
                    if len(tmp_res)<len(res) or len(res)==0:
                        res = tmp_res

            return res

    # {{{
    def solve_01(self, s, t):
        N = len(s)
        M = len(t)
        if N == 0 or M == 0:
            return ""
        else:
            res = ""
            info = [[defaultdict(int) for j in range(N)] for i in range(N)]
            t_info = defaultdict(int)
            for c in t:
                t_info[c] += 1

            for i in range(1, N+1):
                for j in range(N-i+1):
                    if i > 1:
                        info[j][j+i-1] = copy.copy(info[j][j+i-2])
                    info[j][j+i-1][s[j+i-1]] += 1
                    success = True
                    for c in t:
                        if t_info[c] > info[j][j+i-1][c]:
                            success = False
                            break
                    if success:
                        res = s[j:j+i]
                        return res
            return res
    # }}}


def main():
    sol = Solution()
    #s, t = "ADOBECODEBANC", "ABC"
    #s, t = "ab", "a"
    s, t = "a", "aa"
    #s, t = "aabbbbbcdd", "bcdd"
    res = sol.minWindow(s, t)
    print(res)


if __name__ == '__main__':
    main()
