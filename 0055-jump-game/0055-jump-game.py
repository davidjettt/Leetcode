class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # have pointer start at beginning and end of array
        # if the value at the index before end is greater than 1,
        # that means it is possible to reach the end
        # so if that is true shift the end pointer to the left by 1 (decrement)
        # else short circuit and return false
        # and then do the same comparison
        # if right pointer meets left pointer then true
        
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0
                
            
            
        
#         start = 0
#         end = len(nums) - 1
        
#         if nums[start] == end:
#             return True
        
#         while end > start:
#             if nums[end - 1] >= 1:
#                 end -= 1
#             else:
#                 return False
        
#         return True