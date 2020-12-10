"""
Find Median from Data Stream, https://leetcode.com/problems/find-median-from-data-stream/
"""

import os, sys, shutil
import heapq


class MedianFinder_list(object):
    # this idea recording a sorted list 
    # the time complexity of each insertion is O(n), since it takes O(logn) to locate position and O(n) to move the list
    def __init__(self):
        self.nums = list()

    def __get_index(self, num):
        start, end = 0, len(self.nums)
        while start < end:
            mid = (start + end) // 2
            if self.nums[mid] < num:
                start = mid + 1
            else:
                end = mid
        return start

    def addNum(self, num):
        idx = self.__get_index(num)
        self.nums.insert(idx, num)
        
    def findMedian(self):
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        else:
            return (self.nums[n//2] + self.nums[n//2-1]) / 2.0 # leetcode default python intepreter is py2


class MedianFinder(object):
    # the time complexity of each insertion is O(logn), since the operation is perfomed on heap
    # the key idea is to use two heap (max root and min root) to store the data and balancing the lenght of two heap)
    def __init__(self):
        self.n = 0
        self.median = None
        self.l_heap = list()
        self.r_heap = list()
        heapq.heapify(self.l_heap)
        heapq.heapify(self.r_heap)

    def addNum(self, num):
        if self.n == 0:
            # (l_heap is max root heap, so use -num as query,  
            # self.n is to avoid duplicate value, since heapq does not support equal value
            heapq.heappush( self.l_heap, (-num, self.n, num) ) 
            self.n = 1
            self.median = num
        else:
            if num <= self.median:
                heapq.heappush( self.l_heap, (-num, self.n, num) ) 
            else:
                heapq.heappush( self.r_heap, (num, self.n, num) ) 
            self.n += 1

            # balance
            if len(self.l_heap)-len(self.r_heap) > 1:
                value = heapq.heappop( self.l_heap )
                v0, v1, v2 = value
                heapq.heappush(self.r_heap, (-v0, v1, v2) )
            elif len(self.r_heap)-len(self.l_heap) > 1:
                value = heapq.heappop( self.r_heap )
                v0, v1, v2 = value
                heapq.heappush(self.l_heap, (-v0, v1, v2) )
            else:
                pass

            if len(self.l_heap) == len(self.r_heap):
                self.median = (self.l_heap[0][2] + self.r_heap[0][2]) / 2.0
            elif len(self.l_heap) > len(self.r_heap):
                    self.median = self.l_heap[0][2]
            else:
                self.median = self.r_heap[0][2]

    def findMedian(self):
        return self.median

def main():
    mf = MedianFinder()
    mf.addNum(1)
    print(mf.findMedian())
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())
    mf.addNum(4)
    print(mf.findMedian())


if __name__ == '__main__':
    main()
