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


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.solve(l1, l2)

    def solve(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_node = ListNode()
        cur_node = res_node
        carry = 0

        while (l1 is not None or l2 is not None or carry > 0):
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2 is not None:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            cur_node.next = ListNode(val)
            cur_node = cur_node.next
        
        return res_node.next
        

def main():
    # l1 = [2,4,3]; l2 = [5,6,4]
    # l1 = [0]; l2 = [0]
    l1 = [9,9,9,9,9,9,9]; l2 = [9,9,9,9]
    l1 = gen_list(l1); l2 = gen_list(l2)
    
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    print_list(res)


if __name__ == '__main__':
    main()