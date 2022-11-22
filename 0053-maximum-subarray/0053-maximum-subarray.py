class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # edge case: if length of nums is 1 return nums[0]


        # BRUTE FORCE 
#         max_sub = nums[0]
        
#         for i in range(len(nums)):
#             curr_sum = 0
#             for j in range(i, len(nums)):
                
#                 curr_sum += nums[j]
#                 max_sub = max(max_sub, curr_sum)
        
#         return max_sub
                
                    
        # Time O(n)
        # Space O(1)
        
        max_sub = nums[0] # -2
        curr_sum = 0 # 0
        
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
                
            curr_sum += n
            max_sub = max(max_sub, curr_sum)
        
        return max_sub

