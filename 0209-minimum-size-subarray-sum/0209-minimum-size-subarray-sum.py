class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time O(n)
        # Space O(1)
        if target in nums: return 1
        
        l, r = 0, 0
        result = float('inf')
        window_sum = 0
        while r < len(nums):
            window_sum += nums[r]
            
            while window_sum >= target:
                result = min(result, r - l + 1)
                window_sum -= nums[l]
                l += 1
            
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
            