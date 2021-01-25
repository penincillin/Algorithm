"""
Redundant Connection, https://leetcode.com/problems/redundant-connection/
Use DFS to search the result. The key is that, use visited to track the visited node, more important, consider 1->2->3->4->2, 
node 2 is the enter of the loop, and node 2 is the only node has visited value for 2, therefore, we know that 1->2 is not in the loop
In short, we use visit to find the entrance of the loop.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import copy
import math


class Solution(object):
    def findRedundantConnection(self, edges):
        graph = defaultdict(list)
        order = dict()
        for i, (u, v) in enumerate(edges):
            graph[u].append(v)
            graph[v].append(u)
            order[(u,v)] = i
        visit = defaultdict(int)
        visit[1] = 1
        res = self.solve(graph, order, visit, cur=1, prev=-1)
        return res[0]
    
    def solve(self, graph, order, visit, cur, prev):
        for node in graph[cur]:
            if node != prev: # avoid self-loop, e.g. 1->2, 2->1
                edge = (cur, node) if cur<node else (node, cur)
                if visit[node] == 1:
                    visit[node] = 2 # important, help us to determine the entrance of the loop
                    return edge, False
                else:
                    visit[node] = 1
                    mid_res = self.solve(graph, order, visit, node, cur)
                    if mid_res is not None:
                        mid_edge, mid_find = mid_res
                        if not mid_find:
                            if visit[node] == 2:
                                mid_find = True
                            if order[edge] > order[mid_edge] and not mid_find:
                                mid_edge = edge
                        return mid_edge, mid_find
        return None
                

def main():
    sol = Solution()
    # edges = [[1,2], [1,3], [2,3]]
    # edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    # edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
    edges = [[20,24],[3,17],[17,20],[8,15],[14,17],[6,17],[15,23],[6,8],[15,19],[16,22],[7,9],[8,22],[2,4],[4,11],[22,25],[6,24],[13,19],[15,18],[1,9],[4,9],[4,19],[5,10],[4,21],[4,12],[5,6]]

    res = sol.findRedundantConnection(edges)
    print(res)


if __name__ == '__main__':
    main()
