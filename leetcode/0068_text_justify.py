"""
Text Justification, https://leetcode.com/problems/text-justification/
"""

import os, sys, shutil
from collections import defaultdict


class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = list()
        mid = list()
        cur = 0
        for word in words:
            if cur + len(mid) + len(word) > maxWidth:
                if len(mid) == 1:
                    margin = maxWidth - cur
                    mid_str = mid[0] + ' ' * margin
                else:
                    num = len(mid)-1
                    margin = maxWidth - cur
                    mid_str = ''
                    if margin % num == 0:
                        margin = margin // num 
                        mid_str = (' '*margin).join(mid)
                    else:
                        margin0 = margin // num
                        addition = margin-(margin // num) * num
                        for w in mid[:-1]:
                            if addition > 0:
                                mid_str += (w + ' '*(margin0 + 1))
                                addition -= 1
                            else:
                                mid_str += (w + ' '*margin0)
                        mid_str += mid[-1]
                result.append(mid_str)
                mid = list()
                cur = 0
            mid.append(word)
            cur += len(word)
        
        mid_str = ' '.join(mid)
        mid_str += ' '*(maxWidth-len(mid_str))
        result.append(mid_str)
        return result


def main():
    sol = Solution()

    # words = ["This", "is", "an", "example", "of", "text", "justification."]; maxWidth = 16
    # words = ["What","must","be","acknowledgment","shall","be"]; maxWidth = 16
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]; maxWidth = 20
    res = sol.fullJustify(words, maxWidth)
    for s in res:
        print(s, len(s))
    #print(res)


if __name__ == '__main__':
    main()
