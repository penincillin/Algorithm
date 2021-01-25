"""
Copy List with Random Pointer, https://leetcode.com/problems/copy-list-with-random-pointer/
"""

import os, sys, shutil
from collections import defaultdict, Counter


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        res_head = Node(-1)
        res_cur = res_head
        cur = head
        nodes = dict()
        nodes[None] = None

        while cur is not None:
            new_node = Node(cur.val)
            res_cur.next = new_node
            res_cur = new_node
            nodes[cur] = new_node # old -> new
            cur = cur.next

        res_cur = res_head.next
        cur = head
        while cur is not None:
            res_cur.random = nodes[cur.random]
            res_cur = res_cur.next
            cur = cur.next

        return res_head.next


def build_list():
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node1.random = node2
    node2.random = node2
    return node1
        

def main():
    sol = Solution()
    node = build_list()
    res = sol.copyRandomList(node)
    #print(hash(node))


if __name__ == '__main__':
    main()
