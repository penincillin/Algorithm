"""
Implement Stack using Queues, https://leetcode.com/problems/implement-stack-using-queues/
Using two queue, q1, q2. First push value to q1, when top / pop is called, pop elements from q1 to q2 and return the last value.
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class MyStack(object):

    def __init__(self):
        self.q1 = list()
        self.q2 = list()
        

    def push(self, x):
        self.q1.append(x)
        

    def pop(self):
        val = None
        while(len(self.q1)>0):
            val = self.q1.pop(0)
            if len(self.q1)>0: # val is not the last element
                self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1 # exchange q1, q2
        return val
        

    def top(self):
        val = None
        while(len(self.q1)>0):
            val = self.q1.pop(0)
            self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1 # exchange q1, q2
        return val
        

    def empty(self):
        return len(self.q1) == 0


def main():
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    val1 = obj.pop()
    val2 = obj.top()
    val3 = obj.empty()
    print(val1, val2, val3)


if __name__ == '__main__':
    main()
