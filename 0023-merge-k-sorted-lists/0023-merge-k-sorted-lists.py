# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        {
            1: [node, node] ,
            2: [node, node],
            3: [node, node]
        }


        loop through input array
            traverse list and put node into hashmap

        sort hashmap based on key

        loop through values of hashmap and make new list

        '''
        # Time O(nlogk)
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists
        return lists[0]





        # Time O(k * n)
        # Space O(n)
        nodes = {}
        for ll in lists:
            curr = ll
            while curr:
                if curr.val in nodes:
                    nodes[curr.val].append(curr)
                else:
                    nodes[curr.val] = [curr]
                # nodes[curr.val] = 1 + nodes.get(curr.val, 0)
                curr = curr.next

        sorted_nodes = collections.OrderedDict(sorted(nodes.items()))

        dummy = ListNode()
        curr = dummy

        for key, nodes in sorted_nodes.items():
            for i in range(len(nodes)):
                # print('node', nodes[i])
                # curr.next = ListNode(key, None)
                curr.next = nodes[i]
                curr = curr.next
        
        return dummy.next


