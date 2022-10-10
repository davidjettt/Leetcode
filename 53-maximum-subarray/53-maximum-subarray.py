class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # edge case: if length of nums is 1 return nums[0]
        
#           0         4        8
#         [-2,1,-3,4,-1,2,1,-5,4]
#          lr   
            
#         res = nums[0]
#         curr_sum = nums[0]
#         curr_sum2 = 0
        
#         for i in range(len(nums)):
#             for j in range(len(nums)):
                
#                 # print(nums[i], nums[j])
                
#                 # curr_sum2 = 0
#                 if curr_sum < curr_sum2 + nums[j]:
#                     curr_sum2 += nums[j]
#                     curr_sum = curr_sum2
            
#             curr_sum2 = 0
            
#         return curr_sum
                    
                
        max_sub = nums[0]
        curr_sum = 0
        
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
                
            curr_sum += n
            max_sub = max(max_sub, curr_sum)
        
        return max_sub

