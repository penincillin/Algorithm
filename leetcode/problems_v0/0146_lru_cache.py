"""
LRU Cache, https://leetcode.com/problems/lru-cache/
The key idea is to use double linked list to represent the key occurance
"""

import os, sys, shutil


class ListNode():
    # double linked list
    def __init__(self, key=-1, prev=None, next_n=None):
        self.key = key
        self.prev = prev
        self.next = next_n


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict() # key : (value, node)

        # init double linked list
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head


    def __update_linked_list(self, key, value):
        _, node = self.cache[key]
        # remove old node from linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        # add new node into linked list
        new_node = ListNode(key, self.tail.prev, self.tail)
        prev_node = self.tail.prev
        prev_node.next = new_node
        self.tail.prev = new_node
        # add to cache
        self.cache[key] = (value, new_node)


    def get(self, key):
        if key in self.cache:
            value, node = self.cache[key]
            self.__update_linked_list(key, value)
            return value
        else:
            return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.__update_linked_list(key, value)
        else:
            if len(self.cache) == self.capacity:
                # remove least visit node
                first_node = self.head.next 
                second_node = first_node.next
                self.head.next = second_node
                second_node.prev = self.head
                del self.cache[first_node.key]
            # add new node
            new_node = ListNode(key, self.tail.prev, self.tail)
            prev_node = self.tail.prev
            prev_node.next = new_node
            self.tail.prev = new_node
            self.cache[key] = (value, new_node)


def print_list(head):
    node = head
    print('-----start------')
    while(node is not None):
        print(node.key)
        node = node.next
    print('-----end------')


def main():
    '''
    from lru_data import actions, values
    cache = LRUCache(10)

    #for i in range(10):
    for i in range(len(actions)):
        action = actions[i]
        nums = values[i]


        if action == 'put':
            assert len(nums) == 2
            res = cache.put(nums[0], nums[1])
        else:
            assert action == 'get'
            assert len(nums) == 1
            res = cache.get(nums[0])
        #print(i, action, nums, res)
    '''

    lRUCache = LRUCache(2)
    lRUCache.put(1, 1);
    lRUCache.put(2, 2);
    print_list(lRUCache.head)

    res = lRUCache.get(1);   
    print_list(lRUCache.head)

    res = lRUCache.get(1);  
    print_list(lRUCache.head)


if __name__ == '__main__':
    main()
