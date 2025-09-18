"""
Gas Station, https://leetcode.com/problems/gas-station/
Start from 0th and check each one whether (gas[i]-cost[i]+remain)>=0, if it is, then continue accumulating, otherwise, reset.
The thought is that, first, we should start with some point that have gas[i]-cost[i] >= 0;
Then, if i+1, i+2 ... also satisfies this condition, then we can accumulate, but what if they does not ?
When this happens, we should still keep going as along as we can, since this 'minus' point can only be reached from previous positive point
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        res = -1
        N = len(gas)
        cover = 0
        remain = 0
        for ii in range(2*N):
            i = ii % N
            if -cost[i]+gas[i]+remain >= 0:
                if res == -1:
                    res = i
                remain += (-cost[i]+gas[i])
                cover += 1
                if cover == N:
                    return res
            else:
                cover = 0
                remain = 0
                res = -1
        return -1
        

def main():
    sol = Solution()
    gas  = [1,2,3,4,5]; cost = [3,4,5,1,2]
    # gas  = [2,3,4]; cost = [3,4,3]
    res = sol.canCompleteCircuit(gas, cost)
    print(res)


if __name__ == '__main__':
    main()
