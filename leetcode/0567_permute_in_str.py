"""
Permutation in String, https://leetcode.com/problems/permutation-in-string/
Using sliding window, not hard
"""

import os, sys, shutil
from collections import defaultdict, Counter

class Solution(object):
    def __check_success(self, record1, record2):
        for c in record1:
            if record1[c] != record2[c]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        m = len(s1)
        n = len(s2)
        if m > n:
            return False

        record1 = defaultdict(int)
        for c in s1:
            record1[c] += 1

        record2 = defaultdict(int)
        for i in range(m):
            record2[s2[i]] += 1

        head, tail = 0, m-1
        while(tail < n):
            if self.__check_success(record1, record2):
                return True
            else:
                record2[s2[head]] -= 1
                head, tail = head+1, tail+1
                if tail < n:
                    record2[s2[tail]] += 1
        return False


def main():
    s1 = "abc"
    s2 = "eidbaooo"

    sol = Solution()
    res = sol.checkInclusion(s1, s2)
    print(res)


if __name__ == '__main__':
    main()
