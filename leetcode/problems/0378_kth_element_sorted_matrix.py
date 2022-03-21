"""
Kth Smallest Element in a Sorted Matrix, https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"Row-first, then updating per-column". This idea can be extended to more sorted matrix problems.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import heapq
import pdb


class Solution(object):
    def kthSmallest(self, matrix, k):
        return self.solve(matrix, k)
    
    def solve(self, matrix, k):
        n = len(matrix)
        visited = [[False for j in range(n)] for i in range(n)]
        
        heap = list()
        heapq.heapify(heap)

        # Add first row to the heap
        for i in range(n):
            heapq.heappush(heap, (matrix[0][i], i) )
            visited[0][i] = True

        count = 0
        while(len(heap)>0):
            value, idx = heapq.heappop(heap)
            count += 1
            if count == k:
                return value
            else:
                # for each poped top, check the column value
                col = idx%n
                for i in range(0, n):
                    if not visited[i][col]:
                        heapq.heappush(heap, (matrix[i][col], i*n+col) )
                        visited[i][col] = True
        

def main():
    sol = Solution()
    matrix = [[1,5,9],[10,11,13],[12,13,15]]; k = 8
    res = sol.kthSmallest(matrix, k)
    print(res)


if __name__ == '__main__':
    main()
