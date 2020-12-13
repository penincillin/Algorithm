"""
Longest Repeating Character Replacement, https://leetcode.com/problems/longest-repeating-character-replacement/
The key idea is to get max_count of a substr, if the length_of_substr - max_count <= k, then this substr is totally valid, otherwise, we need to change this substr.
"""

from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        head, tail = 0, 0
        count = defaultdict(int)
        max_count = 0
        res = 0
        while(tail < n):
            count[s[tail]] += 1
            max_count = max(count[s[tail]], max_count)
            while(tail-head+1 - max_count > k):
                count[s[head]] -= 1
                max_count = 0
                for c in count:
                    max_count = max(max_count, count[c])
                head += 1
            res = max((tail-head+1), res)
            tail += 1
        return res

def main():
    s = "ABBB"
    k = 2

    sol = Solution()
    res = sol.characterReplacement(s, k)
    print(res)


if __name__ == '__main__':
    main()
