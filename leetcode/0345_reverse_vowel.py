"""
Reverse Vowels of a String, https://leetcode.com/problems/reverse-vowels-of-a-string/
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb


class Solution(object):
    def reverseVowels(self, s):
        record = OrderedDict()
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', "I", "O", "U"]
        for idx, c in enumerate(s):
            if c in vowels_list:
                record[idx] = c
        idx_list = list(record.keys())
        
        num_vowel = len(idx_list)
        c_list = [c for c in s]
        for i in range(num_vowel//2):
            idx1, idx2 = idx_list[i], idx_list[num_vowel-1-i]
            c_list[idx1], c_list[idx2] = c_list[idx2], c_list[idx1]
        return ''.join(c_list)


def main():
    sol = Solution()
    s = "race a car"
    res = sol.reverseVowels(s)
    print(res)


if __name__ == '__main__':
    main()
