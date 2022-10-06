# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse through linked list and add 1 to count at each iteration
        # make count variable, set it equal to 1 because we start at one
        # node to reach is count divided by 2 + 1 ( count // 2 + 1 )
        
        # traverse through list again and if node is count then return node
        
        count, curr, res = 0, head, head
        
        while curr:
            if curr is not None:
                count += 1
            
            curr = curr.next
            
        goal, final = count // 2 + 1, 1
        
        
        while final != goal:
            final += 1
            res = res.next
        
        return res