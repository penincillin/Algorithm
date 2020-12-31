"""
Scramble String, https://leetcode.com/problems/scramble-string/
Recursion solving the problem. Using memory and pruning.
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def isScramble(self, s1, s2):
        record = dict()
        return self.solve(s1, s2, record)

    def compare_chars(self, s1, s2):
        c1 = Counter(s1)
        c2 = Counter(s2)
        for key in c1:
            if key not in c2:
                return False
            else:
                if c1[key] != c2[key]:
                    return False
        for key in c2:
            if key not in c1:
                return False
            else:
                if c1[key] != c2[key]:
                    return False
        return True

    def solve(self, s1, s2, record):
        N = len(s1)
        key = s1 + '_' + s2
        if key in record:
            return record[key]
        else:
            if N == 1:
                res = s1[0] == s2[0]
            else:
                if not self.compare_chars(s1, s2):
                    res = False
                else:
                    res = False
                    for pivot in range(1, N):
                        key1 = s1[:pivot] + '_' + s2[:pivot]
                        key2 = s1[pivot:] + '_' + s2[pivot:]
                        if key1 in record:
                            val1 = record[key1]
                        else:
                            val1 = self.isScramble(s1[:pivot], s2[:pivot])
                            record[key1] = val1
                        if key2 in record:
                            val2 = record[key2]
                        else:
                            val2 = self.isScramble(s1[pivot:], s2[pivot:])
                            record[key2] = val2
                        if val1 and val2:
                            res = True
                            break
                        else:
                            key1 = s1[:pivot] + '_' + s2[N-pivot:]
                            key2 = s1[pivot:] + '_' + s2[:N-pivot]
                            if key1 in record:
                                val1 = record[key1]
                            else:
                                val1 = self.isScramble(s1[:pivot], s2[N-pivot:])
                                record[key1] = val1
                            if key2 in record:
                                val2 = record[key2]
                            else:
                                val2 = self.isScramble(s1[pivot:], s2[:N-pivot])
                                record[key2] = val2
                            if val1 and val2:
                                res = True
                                break
            record[key] = res
            return res


def main():
    # s1 = "abcdbdacbdac"; s2 = "bdacabcdbdac"
    # s1 = "ab"; s2 = "ba"
    # s1 = "great"; s2 = "rgeat"
    #s1 = "abcde"; s2 = "caebd"
    sol = Solution()
    res = sol.isScramble(s1, s2)
    print(res)
  

if __name__ == '__main__':
    main()
