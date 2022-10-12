# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # traverse through list
        # if curr.next.val == val, reassign curr.next = curr.next.next
        # if curr.next.next is None then node we want to remove is the last node so just say curr.next = None
        # return curr
        
        # Time O(n) traversing through n nodes
        # Space O(1)
            
        dummy = ListNode()
        curr = head
        prev = dummy
        prev.next = curr
        
        while curr:
            new_curr = curr.next
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = new_curr
        
        return dummy.next
            