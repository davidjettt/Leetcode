# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Time O(n) traversing through n nodes
        # Space O(1)
            
#         dummy = ListNode()
#         curr = head
#         prev = dummy
#         prev.next = curr
        
#         while curr:
#             new_curr = curr.next
#             if curr.val == val:
#                 prev.next = curr.next
#             else:
#                 prev = curr
            
#             curr = new_curr
        
#         return dummy.next
        
        
        prev, curr = None, head
        
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        
        return head