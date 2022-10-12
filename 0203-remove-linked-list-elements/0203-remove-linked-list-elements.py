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
            
        dummy = ListNode()
        curr = head
        prev = dummy
        prev.next = curr
        
        while curr:
            if curr.next == None and curr.val == val:
                prev.next = None
            if curr.val == val:
                new_curr = curr.next
                prev.next = curr.next
                curr = new_curr
            
            else:
                prev = curr
                curr = curr.next
            
    
            
        # while curr:
        #     if curr.val == val and curr.next == None:
        #         curr = None
        #     elif curr.val == val:
        #         new_curr = curr.next
        #         curr.next = None
        #         curr = new_curr
        #     elif curr.next.next == None and curr.next.val == val:
        #         curr.next = None
        #         curr = curr.next
        #     elif curr.next and curr.next.val == val: 
        #         curr.next = curr.next.next
        #         curr = curr.next
        #     else:
        #         curr = curr.next
            # curr = curr.next
        
        return dummy.next
            