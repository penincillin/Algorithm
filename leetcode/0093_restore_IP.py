"""
Restore IP Addresses, https://leetcode.com/problems/restore-ip-addresses/
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def restoreIpAddresses(self, s):
        return self.solve(s, 0)

    def check_valid(self, cur):
        if len(cur) == 0:
            return False
        elif cur[0] == '0':
            return len(cur) == 1
        else:
            return int(cur)>=0 and int(cur)<=255


    def solve(self, s, order):
        if order == 3: # the last one
            cur = s
            if self.check_valid(cur):
                return [cur,]
            else:
                return []
        else:
            result = list()
            for i in range(1, 4):
                if i <= len(s):
                    print(len(s), i)
                    cur = s[:i]
                    if self.check_valid(cur):
                        mid_res = self.solve(s[i:], order+1)
                        for mr in mid_res:
                            result.append(cur + '.' + mr)
            return result
                

def main():
    sol = Solution()
    # s = "25525511135"
    # s = "0000"
    s = "010010"
    res = sol.restoreIpAddresses(s)
    for r in res:
        print(r)


if __name__ == '__main__':
    main()
