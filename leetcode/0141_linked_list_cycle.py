"""
Linked List Cycle, https://leetcode.com/problems/linked-list-cycle/
Two pointer solution, refer to https://leetcode.com/problems/linked-list-cycle/solution/ for prove.
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
                    return True
                else:
                    pass
            else:
                return False
        return False


def main():
    root = build_linked_list()
    sol = Solution()
    res = sol.hasCycle(root)
    print(res)


if __name__ == '__main__':
    main()
