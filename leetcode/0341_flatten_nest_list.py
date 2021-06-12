"""
Flatten Nested List Iterator, https://leetcode.com/problems/flatten-nested-list-iterator/
The straight-forward idea to flatten and store all the values is easy, but contradicts with the idea of next / hasNext, which requires not to store all the values.
The correct solution is to use Stack, which check the values one-by-one.
Using queue seems to be possible but actually the operation in hasNext() does not follow the rule of queue which first in last out
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class NestedInteger(object):

    def __init__(self, element):
        self.element = element

    def isInteger(self):
        return type(self.element) == int

    def getInteger(self):
        if self.isInteger():
            return self.element
        else:
            return None

    def getList(self):
        if not self.isInteger():
            return self.element
        else:
            return None


class NestedIterator_Flatten_All(object):

    def __init__(self, nestedList):
        # self.nestedList = nestedList
        # self.nlist = list()
        self.nlist = self.flatten(nestedList)


    def flatten(self, nestedList):
        nlist = list()
        for nI in nestedList:
            if nI.isInteger():
                nlist.append(nI.getInteger())
            else:
                nlist += self.flatten(nI.getList())
        return nlist

        
    def next(self):
        res = self.nlist[0]
        self.nlist = self.nlist[1:]
        return res
        

    def hasNext(self):
        return len(self.nlist) > 0


class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        res = self.stack.pop().getInteger()
        return res
        
    def hasNext(self):
        while len(self.stack) > 0:
            if self.stack[-1].isInteger():
                return True
            else:
                top_nI = self.stack.pop()
                for nI in top_nI.getList()[::-1]:
                    self.stack.append(nI)
        return False
        

def main():
    NI = NestedInteger
    i0 = NI(1)
    i1 = NI([NI(2), NI(3)])
    i20 = NI(4)
    i21 = NI([NI(5), NI(6)])
    i2 = NI([i20, i21])

    nlist = [i0, i1, i2]
    niter = NestedIterator(nlist)

    res = list()
    while niter.hasNext():
        res.append(niter.next())
    print(res)


if __name__ == '__main__':
    main()
