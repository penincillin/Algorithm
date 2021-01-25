"""
Top K Frequent Elements, https://leetcode.com/problems/top-k-frequent-elements/
Use heap
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import heapq


class Solution(object):
    def topKFrequent(self, nums, K):
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = list()
        heapq.heapify(heap)
        for num in count:
            freq = count[num]
            heapq.heappush(heap, (freq, num))
            if len(heap) > K:
                heapq.heappop(heap)
        res = list()
        for freq, num in heap:
            res.append(num)
        return res


def main():
    nums = [1,1,1,2,2,3]
    k = 2
    sol = Solution()
    res = sol.topKFrequent(nums, k)
    print(res)


if __name__ == '__main__':
    main()
