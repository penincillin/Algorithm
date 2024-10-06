"""
Remove Duplicates from Sorted List, https://leetcode.com/problems/remove-duplicates-from-sorted-list/
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


class Solution(object):
    def deleteDuplicates(self, head):
        root = ListNode(None)
        root.next = head
        tail = root
        cur = root.next
        while cur is not None:
            if cur.val != tail.val:
                tail.next = cur
                tail = tail.next
            cur = cur.next
        tail.next = None
        return root.next


def main():
    nums = [1,1,2,3,3]
    root = build_linked_list(nums)
    print_linked_list(root)

    sol = Solution()
    res = sol.deleteDuplicates(root)
    print_linked_list(res)


if __name__ == '__main__':
    main()
