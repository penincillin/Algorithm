"""
Design Front Middle Back Queue, https://leetcode.com/problems/design-front-middle-back-queue/
Use two dequeue and balancing the size of these two: len(q0) == len(q1) or len(q0) == len(q1)
A better implementation would be to use double linked list to implement these two dequeues
"""

import os, sys, shutil
from collections import defaultdict, Counter

class FrontMiddleBackQueue(object):

    def __init__(self):
        self.queue0 = list()
        self.queue1 = list()

    def __balance(self): 
        if len(self.queue0) == len(self.queue1):
            pass
        elif len(self.queue0) - len(self.queue1) == 1:
            pass
        else:
            while len(self.queue0) - len(self.queue1) > 1:
                val = self.queue0.pop()
                self.queue1.insert(0, val)
            while len(self.queue1) - len(self.queue0) > 0:
                val = self.queue1.pop(0)
                self.queue0.append(val)

    def pushFront(self, val):
        self.queue0.insert(0, val)
        self.__balance()
        

    def pushMiddle(self, val):
        #self.queue0.append(val)
        if len(self.queue0) == len(self.queue1):
            self.queue0.append(val)
        else:
            val0 = self.queue0.pop()
            self.queue1.insert(0, val0)
            self.queue0.append(val)
        self.__balance()
        

    def pushBack(self, val):
        self.queue1.append(val)
        self.__balance()
        

    def popFront(self):
        if len(self.queue0) > 0:
            val = self.queue0.pop(0)
            self.__balance()
            return val
        else:
            return -1
        

    def popMiddle(self):
        if len(self.queue0) > 0:
            val = self.queue0.pop()
            self.__balance()
            return val
        else:
            return -1
        

    def popBack(self):
        if len(self.queue1) > 0:
            val = self.queue1.pop()
            self.__balance()
            return val
        elif len(self.queue0) > 0:
            val = self.queue0.pop()
            self.__balance()
            return val
        else:
            return -1


def main():
    q = FrontMiddleBackQueue()
    q.pushFront(1);
    q.pushBack(2);    
    q.pushMiddle(3); 
    q.pushMiddle(4);
    print(q.queue0, q.queue1)
    q.popFront();  
    q.popMiddle();
    q.popMiddle();
    q.popBack(); 
    q.popFront();
  

if __name__ == '__main__':
    main()
