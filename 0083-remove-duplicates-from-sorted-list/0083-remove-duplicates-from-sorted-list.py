# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # set prev to none
        # set curr to head
        
        # as long as curr is not null
            # if prev and curr are not the same
            # set prev to curr
            # set curr to curr.next
            
            # if prev and curr are the same
            # save curr.next to temp var
            # prev.next = curr.next
            # curr = temp var
            # don't move prev
            
            
            
        prev = None
        curr = head
        
        while curr:
            
            if prev:
                if prev.val == curr.val:
                    temp = curr.next
                    prev.next = curr.next
                    curr = temp
                else:
                    prev = curr
                    curr = curr.next
            
            else:
                prev = curr
                curr = curr.next
                
        return head