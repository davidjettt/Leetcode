# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        [5]
        
       <- 1  2 -> 3 -> None   n = 1
        
          p   c     
        
        [5]
        [1,2,3,5]
        
        
        traverse to the end of the linked list
        
        [1,2]
         c
        
        
        '''
        # prev = None
        # curr = head
        
#         count = 1
#         curr = head
#         while curr.next:
#             curr = curr.next
#             count += 1
            
#         target = count - n
#         curr = head

#         while target != 1 and curr:
            
#             curr = curr.next
#             target -= 1
        
#         curr.next = curr.next.next
            
#         return head
    
        dummy = ListNode(0, head)
        
        left, right = dummy, head
        
        
        while n > 0 and right:
            right = right.next
            n -= 1
            
            
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        
        return dummy.next
        
            
        
        
        
#         nodes = []
        
#         while n > 1:
#             prev = None
#             curr = head
#             while curr.next:
                
#                 prev = curr
#                 curr = curr.next
                
#             nodes.append(curr)
#             prev.next = None
            
#             n -= 1
            
#         prev = None
#         curr = head
        
#         while curr.next:
#             prev = curr
#             curr = curr.next
        

#         prev.next = None

#         for i in range(len(nodes) - 1, -1, -1):
#             curr = nodes[i]
#             prev.next = curr

#             prev = curr
#             curr = curr.next

#         return head
        
                
        