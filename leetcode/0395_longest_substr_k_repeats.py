"""
Longest Substring with At Least K Repeating Characters, https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Refer to solution: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/
"""

import os, sys, shutil
import heapq
from collections import defaultdict, Counter


class Solution(object):
    def longestSubstring(self, s, k):
        if k == 1:
            return len(s)
        else:
            # we assume k > 1 in the follow, this can ease the coding
            counter = Counter(s)
            n_unique = len(counter)
            N = len(s)

            res = 0
            for cur_unique in range(1, n_unique+1):
                head, tail = 0, 0
                record = defaultdict(int)
                record[s[0]] += 1
                while(tail < N):
                    if len(record) > cur_unique:
                        record[s[head]] -= 1
                        if record[s[head]] == 0:
                            del record[s[head]]
                        head += 1
                    else:
                        tail += 1
                        if tail < N:
                            record[s[tail]] += 1
                            success = True
                            for c in record:
                                if record[c] < k:
                                    success = False
                                    break
                            if success:
                                res = max(res, tail-head+1)
            return res

def main():
    s = "ababbc"; k = 2
    sol = Solution()
    res = sol.longestSubstring(s, k)
    print(res)


if __name__ == '__main__':
    main()
