"""
Reconstruct Itinerary, https://leetcode.com/problems/reconstruct-itinerary/
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import copy


class Solution(object):
    def findItinerary(self, tickets):
        # build graph
        record = defaultdict(int) # number of (src, dst) pairs
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            record[(src,dst)] += 1
        for src in graph:
            graph[src] = sorted(graph[src])
        # add padding
        for src, dst in tickets:
            if dst not in tickets:
                graph[dst].append(None)
                record[(dst, None)] += 1
        N = len(tickets) + 1
        return self.solve(graph, record, 'JFK', N)

    def solve(self, graph, record, src, N):
        if N == 0:
            return []
        else:
            for dst in graph[src]:
                if record[(src, dst)] > 0:
                    record[(src, dst)] -= 1
                    mid_res = self.solve(graph, record, dst, N-1)
                    if mid_res is not None and len(mid_res) == N-1:
                        return [src,] + mid_res
                    else:
                        record[(src, dst)] += 1
            return None


def main():
    sol = Solution()
    # tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    # tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
    # JFK -> ANU, ANU -> EZE, EZE -> AXA, AXA -> TIA, 
    res = sol.findItinerary(tickets)
    print(res)


if __name__ == '__main__':
    main()
