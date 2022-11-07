# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # need to keep track of prev, curr, curr.next
        # traverse through linked list while curr is truthy
        # save curr.next to a temp var
        # curr.next points to curr
        # curr points to prev
        # prev points to temp var
        
#         prev = None
#         curr = head
        
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
            
#         return prev
        
        # Time O(n)
        # Space O(1)
        
        # RECURSIVE
#         if not head:
#             return None
        
#         newHead = head
        
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
        
        # return newHead
        
        return self.reverse(head, None)
    
    def reverse(self, cur, prev):
        if cur is None:
            return prev
        else:
            next = cur.next
            cur.next = prev
            return self.reverse(next, cur)

  
            
    
        
        
        