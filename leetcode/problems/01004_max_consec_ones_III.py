"""
Max Consecutive Ones III, https://leetcode.com/problems/max-consecutive-ones-iii/
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def longestOnes(self, A, K):
        N = len(A)
        head, tail = 0, 0
        res = 0
        while(tail < N):
            if A[tail] == 1:
                tail += 1
            else:
                if K > 0:
                    K -= 1
                    tail += 1
                else:
                    if K == 0 and head == tail:
                        head += 1
                        tail += 1
                    while K == 0 and head <= tail and head<N:
                        if A[head] == 0:
                            K += 1
                        head += 1
            res = max(res, tail-head)
        return res


def main():
    #A = [1,1,1,0,0,0,1,1,1,1,0]; K = 2
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]; K = 3
    
    sol = Solution()
    res = sol.longestOnes(A, K)
    print(res)


if __name__ == '__main__':
    main()
