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
        curr1, curr2 = l1, l2
        res = []
        carry_over = 0
        while curr1 and curr2:
            curr_sum = curr1.val + curr2.val + carry_over

            if curr_sum < 10:
                res.append(curr_sum)
                carry_over = 0
            else:
                ones_place = curr_sum - 10
                res.append(ones_place)
                carry_over = 1
            
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            curr_sum = curr1.val + carry_over

            if curr_sum < 10:
                res.append(curr_sum)
                carry_over = 0
            else:
                ones_place = curr_sum - 10
                res.append(ones_place)
                carry_over = 1
            curr1 = curr1.next
            
        while curr2:
            curr_sum = curr2.val + carry_over

            if curr_sum < 10:
                res.append(curr_sum)
                carry_over = 0
            else:
                ones_place = curr_sum - 10
                res.append(ones_place)
                carry_over = 1
            curr2 = curr2.next
        
        if carry_over:
            res.append(carry_over)
        
        print(res)
        
        i = 0
        dummy = ListNode()
        final = dummy
        while i < len(res):
            new_node = ListNode(res[i])
            
            final.next = new_node
            
            i += 1
            final = final.next
        
        return dummy.next
            
                
    