"""
https://leetcode.com/problems/add-two-numbers/description/
Remember to keep the last carry.
"""

from typing import List, Dict, Tuple, Optional
from collections import defaultdict, Counter
import pdb


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def gen_list(vals: List[int]) -> ListNode:
    head = ListNode()
    cur = head
    for val in vals:
        cur.next = ListNode(val)
        cur = cur.next
    return head.next


def print_list(node: ListNode):
    vals = []
    while node is not None:
        vals.append(node.val)
        node = node.next
    print(vals)


def main():
    pass


if __name__ == '__main__':
    main()