"""
Reverse Words in a String, https://leetcode.com/problems/reverse-words-in-a-string/
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    '''
    def reverseWords(self, s):
        words = s.strip().split()
        res_word = ' '.join(words[::-1])
        return res_word
    '''
    def reverseWords(self, s):
        res = ''
        n = len(s)
        i = n-1
        while i >= 0:
            while s[i]==' ' and i>=0:
                i -= 1
            end = i
            while s[i]!=' ' and i>=0:
                i -= 1
            start = i
            if start < end:
                res += (s[start+1:end+1] + ' ')
        if len(res)>0 and res[-1] == ' ':
            res = res[:-1]
        return res


def main():
    sol = Solution()
    # s = "the sky is blue"
    # s = "world"
    s = "a good   example"
    res = sol.reverseWords(s)
    print(res)


if __name__ == '__main__':
    main()
