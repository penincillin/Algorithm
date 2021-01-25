"""
Implement Queue using Stacks, https://leetcode.com/problems/implement-queue-using-stacks/
Similar to implement stack using queue, the difference is that stack will reverse the order, so need to recover correct order after call pop / peek
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class MyQueue(object):

    def __init__(self):
        self.s1 = list()
        self.s2 = list()
        

    def push(self, x):
        self.s1.append(x)
        

    def pop(self):
        val = None
        while len(self.s1)>0:
            val = self.s1.pop()
            if len(self.s1)>0:
                self.s2.append(val)
        self.restore()
        return val
        

    def peek(self):
        val = None
        while len(self.s1)>0:
            val = self.s1.pop()
            self.s2.append(val)
        self.restore()
        return val
    

    def restore(self):
        while len(self.s2)>0:
            val = self.s2.pop()
            self.s1.append(val)
        

    def empty(self):
        return len(self.s1) == 0


def main():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    val1 = obj.pop()
    val2 = obj.peek()
    val3 = obj.empty()
    obj.push(4)
    val4 = obj.pop()
    val5 = obj.pop()
    val6 = obj.pop()
    print(val4, val5, val6)


if __name__ == '__main__':
    main()
