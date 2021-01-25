"""
Partition List, https://leetcode.com/problems/partition-list/
Maintain two sub linke list, small and large, add small node to small and large node to large, then concat these two linked list.
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
    def partition(self, head, x):
        small_head, large_head = ListNode(-1), ListNode(-1)
        small_node, large_node = small_head, large_head
        node = head
        while node:
            if node.val < x:
                small_node.next = node
                small_node = small_node.next
            else:
                large_node.next = node
                large_node = large_node.next
            node = node.next
        large_node.next = None
        small_node.next = large_head.next
        return small_head.next


def main():
    nums = [1, 4, 3, 2, 5, 2]; x = 3
    root = build_linked_list(nums)
    print_linked_list(root)

    sol = Solution()
    root = sol.partition(root, x)
    print_linked_list(root)


if __name__ == '__main__':
    main()
