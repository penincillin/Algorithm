"""
Network Delay Time, https://leetcode.com/problems/network-delay-time/
Use Dijkstra shortest path algorithm.
Use heap to maintain the uncompleted node, visit to maintain the complete node.
When there is still unvisited nodes in heap, always continue the algorithm.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import heapq
import pdb


class Solution(object):
    def networkDelayTime(self, times, n, k):
        return self.solve(times, n, k)

    def solve(self, times, n, k):
        # build graphs
        graphs = defaultdict(dict)
        for u, v, w in times:
            graphs[u][v] = w

        delay = defaultdict(lambda :float('inf'))
        delay[k] = 0
        visit = [False for i in range(n)]

        heap = list()
        heapq.heapify(heap)
        for i in range(1, n+1):
            heapq.heappush(heap, (delay[i], i) )

        while len(heap) > 0:
            # find the smallest unvisited node
            u_delay, u = heapq.heappop(heap)
            if visit[u-1]:
                continue
            # update the targets
            for v in graphs[u]:
                tmp_delay = u_delay + graphs[u][v]
                if tmp_delay < delay[v]:
                    delay[v] = tmp_delay
                    heapq.heappush(heap, (tmp_delay, v))
            visit[u-1] = True

        res = -1
        for i in range(1, n+1):
            res = max(res, delay[i])
        if res < float('inf'):
            return res
        else:
            return -1
        

def main():
    sol = Solution()

    times = [[2,1,1],[2,3,1],[3,4,1]]
    n, k = 4, 2
    res = sol.networkDelayTime(times, n, k)
    print(res)


if __name__ == '__main__':
    main()
