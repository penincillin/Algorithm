"""
Remove Duplicates from Sorted List II, https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Use additional memory is trivial, the key is to use only O(1) space.
"""

import os, sys, shutil
from collections import defaultdict, OrderedDict


class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        else:
            new_head = ListNode()
            new_node = new_head
            repeat = 0
            cur_val = None
            cur_node = new_head
            node = head
            while(node is not None):
                if node.val == cur_val:
                    repeat += 1
                else:
                    if repeat == 1:
                        new_node.next = cur_node
                        new_node = cur_node
                    cur_node = node
                    cur_val = node.val
                    repeat = 1
                node = node.next

            if repeat == 1:
                new_node.next = cur_node
                new_node = cur_node

            new_node.next = None
            return new_head.next
        

def build_list(nums):
    assert len(nums) > 0
    head = ListNode(nums[0])
    cur = head
    for n in nums[1:]:
        node = ListNode(n)
        cur.next = node
        cur = node
    return head


def print_list(head):
    node = head
    while(node is not None):
        print(node.val, end=' ')
        node = node.next
    print()


def main():
    nums = [1,]
    head = build_list(nums)
    print_list(head)

    sol = Solution()
    head = sol.deleteDuplicates(head)
    print_list(head)


if __name__ == '__main__':
    main()
