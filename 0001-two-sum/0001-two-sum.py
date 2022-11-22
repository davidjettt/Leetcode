class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         lookup = {}
        
#         for index, num in enumerate(nums):
#             if target - num in lookup:
#                 return [index, lookup[target - num]]
#             else:
#                 lookup[num] = index

        for i in range(len(nums) - 1):
            for j in range(len(nums)):
                if j != i:
                    if nums[i] + nums[j] == target:
                        return i, j
        
        # Time O(n)
        # Space O(n)
#         lookup = {}
        
#         for i, num in enumerate(nums):
#             if target - num in lookup:
#                 return [i, lookup[target - num]]
#             else:
#                 lookup[num] = i
                
    
            
        
        