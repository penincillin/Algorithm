"""
Minimum Height Trees, https://leetcode.com/problems/minimum-height-trees/
The key idea is to use the idea of topology sorting. And another property of tree.  Refer to the solution for details: https://leetcode.com/problems/minimum-height-trees/solution/
"""

import os, sys, shutil
from collections import defaultdict
import copy


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        return self.solve_topology(n, edges)


    # {{{
    def solve(self, n, edges):
        graph = defaultdict(list)
        record = defaultdict(dict)
        nums = defaultdict(int)

        if n == 1:
            return [0,]
        else:
            result = list()
            # init
            for i, j in edges:
                graph[i].append((j,1))
                graph[j].append((i,1))
                nums[i] += 1
                nums[j] += 1
                record[i][j] = 1
                record[j][i] = 1
                if nums[i] == n-1:
                    result.append(i)
                if nums[j] == n-1:
                    result.append(j)
            if len(result) > 0:
                return result

            result = defaultdict(list)
            for cur_h in range(2, n):
                for i in graph:
                    i_neighbors = copy.copy(graph[i])
                    for j, j_h in i_neighbors:
                        if j_h < cur_h:
                        #if True:
                            j_neighbors = copy.copy(graph[j])
                            for k, k_h in j_neighbors:
                                if (k_h + j_h) == cur_h:
                                #if True:
                                    if (i != k) and (i not in record[k]) and (k not in record[i]):
                                        record[i][k] = 1
                                        record[k][i] = 1
                                        graph[i].append((k, j_h + k_h))
                                        graph[k].append((i, j_h + k_h))
                                        nums[i] += 1
                                        nums[k] += 1
                                        if nums[i] == n-1:
                                            result[j_h+k_h].append(i)
                                        if nums[k] == n-1:
                                            result[j_h+k_h].append(k)
                if len(result[cur_h]) > 0:
                    return result[cur_h]
        # }}}

    def solve_topology(self, n, edges):
        # special case, n = 1
        if n == 1:
            return [0,]
        
        # n >= 2
        degrees = defaultdict(int)
        record = defaultdict(dict)
        for i, j in edges:
            degrees[i] += 1
            degrees[j] += 1
            record[i][j] = 1
            record[j][i] = 1

        queue = list()
        for node in degrees:
            if degrees[node] == 1:
                queue.append(node)
        
        while(len(degrees) > 2):
            new_queue = list()
            while (len(queue) > 0):
                node = queue.pop(0)
                for neighbor in record[node]:
                    degrees[neighbor] -= 1
                    del record[neighbor][node]
                    if degrees[neighbor] == 1:
                        new_queue.append(neighbor)
                del degrees[node]
            queue = new_queue

        return list(degrees)


def main():
    # n = 4; edges = [[1,0], [1,2], [1,3]]
    n = 6; edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    # n = 3; edges = [[0,1],[1,2]]
    # n = 4; edges = [[0,1], [0,2], [2,3]]
    sol = Solution()
    res = sol.findMinHeightTrees(n, edges)
    print(res)


if __name__ == '__main__':
    main()
