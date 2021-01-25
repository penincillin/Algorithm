"""
Evaluate Division, https://leetcode.com/problems/evaluate-division/
Use graph and dfs to solve this problem. There are some cases to be careful.
1. use math.isnan() to check nan, instead of x == float('nan')
2. do not visit same node for two times
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import copy
import math


class Solution(object):

    def calcEquation(self, equations, values, queries):
        # build graph
        graph = defaultdict(list)
        for i, (x, y) in enumerate(equations):
            if x != y: # avoid loop
                value = values[i]
                graph[x].append((y, value))
                if value == 0.0:
                    graph[y].append((x, float('nan')))
                else:
                    graph[y].append((x, 1/value))
        # check query one by one
        res = list()
        for query in queries:
            visited = defaultdict(int)
            mid_res = self.solve(graph, query, visited)
            if math.isnan(mid_res):
                mid_res = -1.0
            res.append(mid_res)
        return res
    
    def solve(self, graph, query, visited):
        x, y = query
        if x in graph and y in graph:
            if x == y: # check equal
                return 1.0
            else:
                # check whether y in successors of x 
                for var, value in graph[x]:
                    if var == y:
                        return value
                for var, value in graph[x]:
                    if visited[var] == 0:
                        visited[var] = 1
                        query = (var, y)
                        mid_res = self.solve(graph, query, visited)
                        if not math.isnan(mid_res):
                            return value * mid_res
                        visited[var] = 0
                return float('nan')
        else:
            return float('nan')
                

def main():
    sol = Solution()
    '''
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    '''
    '''
    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    '''
    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    res = sol.calcEquation(equations, values, queries)
    print(res)


if __name__ == '__main__':
    main()
