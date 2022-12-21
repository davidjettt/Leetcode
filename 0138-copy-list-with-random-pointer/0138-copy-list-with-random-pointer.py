"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
         0     1    2    3
        1:2 -> 2 -> 3 -> 4


        a node's random pointer can point to one other node, itself, or NULL
        a node can be pointed at by multiple nodes

        make a copy of ll w/o random pointers yet
            traversing orig. ll and create nodes with that same value and append to result list

        use hashmap to store idx node as key and random pointer reference as value

        traverse through copy list and use hashmap as ref. to assign random pointers


        {
            0: null,
            1: 0,
            ...
        }
        '''
        # Time O(n)
        # Space O(n)

        old_to_copy = { None: None }

        curr = head
        while curr:
            copy_node = Node(curr.val)
            old_to_copy[curr] = copy_node

            curr = curr.next
        
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]

            curr = curr.next

        return old_to_copy[head]


        # random_pointers = {}
        # dummy = Node(0)
        # copy_curr = dummy
        # orig_curr = head
        # i = 0

        # while orig_curr:
        #     new_node = Node(orig_curr.val)
        #     copy_curr.next = new_node
        #     print('ran', orig_curr.random)
        #     random_pointers[i] = orig_curr.random

        #     orig_curr = orig_curr.next
        #     copy_curr = copy_curr.next
        #     i += 1

        # print('random', random_pointers)

        # curr = dummy.next
        # j = 0
        # while curr:
        #     curr.random = random_pointers[j]

        #     j += 1
        #     curr = curr.next

        # return dummy.next
        

        