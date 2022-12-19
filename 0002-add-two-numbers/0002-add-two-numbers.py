# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        traversing both linked list at the same time until reach null on one of them
            adding the 2 numbers together and putting it into an array
            if the new number is >= 10, 
            then need to subtract that number by 10
            then that result number is what we push into array and 
            we need to carry over a 1 to add to the next column
        
        (take into account carry-over variable)
        if length of both lists not the same,
        then need to finish traversal of list

        iterate through array and make new list from it

        5 -> 8 -> 9 -> 1
        5 -> 1
        0 -> 0 -> 0 -> 2
        '''
        # Time O(n + m)
        # Space O(n)
        curr1, curr2 = l1, l2
        res = []
        carry_over = 0
        dummy = ListNode()
        curr = dummy
        while curr1 or curr2:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            # curr_sum = curr1.val + curr2.val + carry_over
            curr_sum = v1 + v2 + carry_over

            if curr_sum < 10:
                # res.append(curr_sum)
                curr.next = ListNode(curr_sum)
                carry_over = 0
            else:
                ones_place = curr_sum - 10
                # res.append(ones_place)
                curr.next = ListNode(ones_place)
                carry_over = 1
            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        
        if carry_over:
            # res.append(carry_over)
            curr.next = ListNode(1)
        
        return dummy.next
        
#         i = 0
#         dummy = ListNode()
#         curr = dummy
#         while i < len(res):
#             new_node = ListNode(res[i])
#             curr.next = new_node
            
#             i += 1
#             curr = curr.next
        
#         return dummy.next
            
                
    