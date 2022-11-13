class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        
        for n in nums:
            if n in vals:
                return True
            else:
                vals.add(n)
        return False
        
        
        
        
        
        
        
        # Time O(n)
        # Space O(n)
#         nums2 = set(nums)
        
#         if len(nums2) < len(nums):
#             return True
#         else:
#             return False

        
#         nums.sort()
#         windowStart = 0
#         for windowEnd in range(1, len(nums)):
#             if nums[windowStart] == nums[windowEnd]:
#                 return True
#             else:
#                 windowStart += 1
                
#         return False
            
        

#  Time O(n)
# Space O(1)
#         unique = set()
        
#         for num in nums:
            
#             if num in unique:
#                 return True
            
#             else:
#                 unique.add(num)
        
#         return False
            
            