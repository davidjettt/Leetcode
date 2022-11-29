class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Time O(n)
        # Space O(n)
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [i, lookup[target - num]]
            else:
                lookup[num] = i
                

    
        # Time O(nlogn)
        # Space O(1)
#         nums.sort()
        
#         l, r = 0, len(nums) - 1
        
#         while l < r:
#             curr_sum = nums[l] + nums[r]
            
#             if curr_sum < target:
#                 l += 1
#             elif curr_sum > target:
#                 r -= 1
#             else:
#                 return [l, r]


        # Brute Force Approach
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
                
        

                
    
            
        
        