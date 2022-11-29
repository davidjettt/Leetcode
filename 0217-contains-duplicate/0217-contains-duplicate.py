class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        [ 1, 2, 3, 4 ]
                    
        iterate through the array
        if nums[i - 1] == nums[i]
        
        '''
        # time O(nlogn)
        # space O(1)
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                return True
        
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
            
            