"""
Repeated DNA Sequences, https://leetcode.com/problems/repeated-dna-sequences/
Hash table resolution. A better way might be convert seq to a Quaternary number.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import copy


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        cur = 0
        N = 10
        record = defaultdict(int)
        res = list()
        while cur <= len(s):
            if cur >= N:
                seq = s[cur-N:cur]
                record[seq] += 1
                if record[seq] == 2: # second time
                    res.append(seq)
            cur += 1
        return res


def main():
    sol = Solution()
    # s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s = "AAAAAAAAAAA"
    res = sol.findRepeatedDnaSequences(s)
    for r in res:
        print(r)


if __name__ == '__main__':
    main()
