class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time O(n) where n is length of input array
        # Space O(1)
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