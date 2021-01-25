"""
Peeking Iterator, https://leetcode.com/problems/peeking-iterator/
The idea is to store the next value first, then cal next() or peek()
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb
import copy


class Iterator(object):

     def __init__(self, nums):
         self.nums = nums

     def hasNext(self):
         return len(self.nums)>0

     def next(self):
         val = self.nums[0]
         self.nums = self.nums[1:]
         return val


class PeekingIterator(object):

    def __init__(self, iterator):
        self.iter = iterator
        self.__next()

    def __next(self):
        if self.iter.hasNext():
            self.element = self.iter.next()
        else:
            self.element = None
        

    def peek(self):
        return self.element
        

    def next(self):
        val = self.element
        self.__next()
        return val
        

    def hasNext(self):
        return self.element is not None


def main():
    nums = [1,2,3]
    iter = PeekingIterator(Iterator(nums))
    '''
    while iter.hasNext():
        val = iter.peek()  
        print(val)
        iter.next()       
    '''
    val1 = iter.peek()
    val2 = iter.peek()
    val3 = iter.next()
    val4 = iter.peek()
    print(val1, val2, val3, val4)


if __name__ == '__main__':
    main()
