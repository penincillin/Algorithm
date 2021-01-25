"""
Linked List Cycle, https://leetcode.com/problems/linked-list-cycle-ii/
Refer to https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/ for prove
"""

import os, sys, shutil
import pdb


class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def build_linked_list(nums):
    root = ListNode(-1)
    node = root
    N, n = len(nums), 0
    while(n < N):
        node.next = ListNode(nums[n])
        node = node.next
        n += 1
    return root.next


def print_linked_list(root):
    nums = list()
    while(root):
        nums.append(root.val)
        root = root.next
    print(nums)


def build_linked_list():
    root = ListNode(3)
    node1 = ListNode(2)
    root.next = node1
    node2 = ListNode(0)
    node1.next = node2
    node3 = ListNode(-4)
    node2.next = node3
    node3.next = node1
    return root


class Solution(object):
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast is not None and slow is not None:
            fast = fast.next
            slow = slow.next
            if slow:
                slow = slow.next
                if fast == slow:
                    return fast
                else:
                    pass
            else:
                return None
        return None

    def detectCycle(self, head):
        meet_node = self.hasCycle(head)
        if meet_node is not None:
            node1 = head
            node2 = meet_node
            while node1 != node2:
                node1 = node1.next
                node2 = node2.next
            return node1
        else:
            return None
   

def main():
    root = build_linked_list()
    sol = Solution()
    res = sol.detectCycle(root)
    print(res.val)


if __name__ == '__main__':
    main()
