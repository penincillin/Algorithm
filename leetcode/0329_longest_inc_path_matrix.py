"""
Longest Increasing Path in a Matrix, https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Use BFS && Dijkstra shortest path algorithm
"""

import os, sys, shutil
from collections import defaultdict, Counter, OrderedDict
import pdb
import math


class Solution(object):
    def longestIncreasingPath(self, matrix):
        return self.solve(matrix)

    def build_link_info(self, N, M, matrix):
        link_info = defaultdict(list)
        for i in range(N):
            for j in range(M):
                for k in [(-1,0),(1,0),(0,1),(0,-1)]:
                    k0, k1 = k
                    i0 = i + k0
                    j0 = j + k1
                    if i0>=0 and i0<N and j0>=0 and j0<M:
                        if matrix[i][j] < matrix[i0][j0]: # link only valid paths
                            cur = i*M+j
                            child = i0*M+j0
                            link_info[cur].append(child)
        return link_info

    def solve(self, matrix):
        N = len(matrix)
        M = len(matrix[0])
        link_info = self.build_link_info(N, M, matrix)
      
        record = defaultdict(lambda:1) # largest path from current point

        res = 0
        updated = True
        while updated:
            updated = False
            for i in range(N):
                for j in range(M):
                    cur = i*M+j
                    mid_res = record[cur]
                    for child in link_info[cur]:
                        if record[child]+1 > mid_res:
                            mid_res = record[child]+1
                            updated = True
                    record[cur] = mid_res
                    res = max(res, mid_res)
        return res


def main():
    sol = Solution()
    # matrix = [[9,9,4],[6,6,8],[2,1,1]]
    matrix = [[1,6,12,1,3],[8,4,6,10,5],[12,11,7,12,2],[2,3,4,1,13],[14,6,0,14,13]]
    # matrix = [[1,]]
    # matrix = [[17,4,6,11,4,0,17,12,19,12,12,0],[0,6,4,4,5,9,15,1,11,13,18,0],[4,2,13,1,2,7,15,5,14,6,8,6]]
    res = sol.longestIncreasingPath(matrix)
    print(res)


if __name__ == '__main__':
    main()
