# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        1 -> 2 -> 3 -> 4 -> 5
             i              j
        1 -> 5 -> 2 -> 3 -> 4

        1 -> 5 -> 2 -> 4 -> 3

        1 -> 2 -> 3 -> 4 -> 5 -> 6

        1 -> 6 -> 2 -> 5 -> 3 -> 4

       <- 1  2 -> 3 -> 4
          p  c
        """
        # Find Middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge two halves
        first, second = head, prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2 

        




        
