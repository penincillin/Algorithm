"""
Merge k Sorted Lists, https://leetcode.com/problems/merge-k-sorted-lists/
"""
from queue import PriorityQueue
import heapq

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    #def __lt__(self, val

class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        else:
            pq = list()
            heapq.heapify(pq)
            n = len(lists)
            count = 0
            for i in range(n):
                node = lists[i]
                if node is not None:
                    # add count here, because the heapq compare tuple one by one, 
                    # without count, error will be raised if node.val are equal
                    heapq.heappush(pq, (node.val, count, node))
                    count += 1

            head = ListNode(-1)
            node = head
            while(len(pq) > 0):
                cur = heapq.heappop(pq)[2]
                node.next = cur
                node = cur
                if node is not None:
                    node_next = node.next
                    if node_next is not None:
                        heapq.heappush(pq, (node_next.val, count, node_next))
                    count += 1
            return head.next


def build_list(value_lists):
    num_list = len(value_lists)
    res_list = []
    for i in range(num_list):
        lists = value_lists[i]
        if len(lists) == 0:
            return []
        else:
            node = ListNode(lists[0])
            head = node
            for j in range(1, len(lists)):
                new_node = ListNode(lists[j])
                node.next = new_node
                node = new_node
            res_list.append(head)
    return res_list


def main():
    value_lists = [
        [1,4,5],[1,3,4],[2,6]   
    ]
    node_list = build_list(value_lists)
    sol = Solution()
    node = sol.mergeKLists(node_list)
    res = ''
    while(node != None):
        res += f'{node.val} '
        node = node.next
    print(res)


if __name__ == '__main__':
    main()
