class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # SUBARRAY SUM MUST BE GREATER THAN OR EQUAL
        
        # [2,3,1,2,4,3]
        #    l   r
        
        l, r = 0, 0
        result = float('inf')
        window_sum = 0
        while r < len(nums):
            window_sum += nums[r]
            
            while window_sum >= target:
                result = min(result, r - l + 1)
                window_sum -= nums[l]
                l += 1
                
                if result == 1:
                    return 1
            
            r += 1
        return 0 if result == float('inf') else result
    
    
#         # BRUTE FORCE SOLUTION
#         shortest = float('inf')
        
#         for i in range(len(nums)):
#             length = 0
#             curr_sum = 0
#             for j in range(i, len(nums)):
#                 if curr_sum < target:
#                     curr_sum += nums[j]
#                     length += 1
#                 # else:
#                 #     shortest = min(shortest, length)
            
#             if curr_sum >= target:
#                 shortest = min(shortest, length)
                
#         return 0 if shortest == float('inf') else shortest
            
        
        
        
#         n = len(nums)
#         prefix = [0] * (n + 1)
#         for i in range(n):
#             prefix[i + 1] = prefix[i] + nums[i]
#             # prefix.append(prefix[i - 1] + nums[i - 1]) 

            
#         print(prefix)
        
#         i, j = 0, 0
#         count = 0
#         min_length = float('inf')
#         while j < len(prefix[1:]):
            
#             if prefix[j] == target:
#                 return 1
            
#             if count == target:
#                 min_length = min(min_length, j - i + 1)
                
#             elif count < target:
#                 count += prefix[j]
#             else:
#                 i += 1
                
            
#             j += 1
#         return 0 if min_length == float('inf') else min_length
            